"""Read-only dashboard over persisted runs."""

import json
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(page_title="Apple Silicon ML benchmarks", layout="wide")
st.title("Apple Silicon ML benchmarks")
st.caption("Stored measurements · GPU evidence and correctness are reported separately")
root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("results")
runs = sorted((p.parent for p in root.glob("*/summary.json")), reverse=True)
if not runs:
    st.info(f"No stored runs under {root}. Execute mlx-m5-bench run --profile quick.")
    st.stop()
selected = st.selectbox("Run", runs, format_func=lambda p: p.name)
manifest = json.loads((selected / "manifest.json").read_text())
st.caption(
    f"{manifest['profile']} · {manifest['timestamp']} · "
    f"{manifest.get('chip', manifest['machine'])} · {manifest['state']}"
)
data = pd.DataFrame(json.loads((selected / "summary.json").read_text()))
for column, label in (
    ("algorithm", "Algorithm"),
    ("samples", "Dataset size"),
    ("backend", "Execution backend"),
    ("phase", "Measurement phase"),
    ("operation", "Operation"),
):
    choices = sorted(data[column].unique())
    defaults = (
        [phase for phase in ("steady", "unmeasured") if phase in choices]
        if column == "phase"
        else choices
    )
    chosen = st.sidebar.multiselect(label, choices, default=defaults)
    data = data[data[column].isin(chosen)]
profile = st.sidebar.multiselect(
    "Experiment profile", [manifest["profile"]], default=[manifest["profile"]]
)
if not profile:
    data = data.iloc[:0]
st.warning(
    "Library-reported GPU and mixed paths are independently unverified. "
    "Ineligible timings have no CPU/candidate ratio. Empty timings identify unmeasured cases."
)
st.dataframe(data, hide_index=True, width="stretch")
if not data.empty and "time_median_s" in data:
    chart = data.copy()
    chart["evidence"] = (
        chart["implementation"]
        + " · "
        + chart["operation"]
        + " · "
        + chart["correctness"]
        + " · "
        + chart["backend"]
    )
    st.bar_chart(chart, x="case", y="time_median_s", color="evidence", stack=False)
with st.expander("Raw correctness and failure records"):
    raw = json.loads((selected / "measurements.json").read_text())
    st.json([row for row in raw if row["case"] in set(data["case"])])
with st.expander("Reproducibility manifest"):
    st.json(manifest)
st.download_button("Download filtered CSV", data.to_csv(index=False), "benchmarks.csv", "text/csv")
