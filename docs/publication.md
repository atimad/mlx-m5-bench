# Initial publication checkpoint

This record describes the original pre-publication review. The repository is now public at [atimad/mlx-m5-bench](https://github.com/atimad/mlx-m5-bench). See [GitHub Actions](https://github.com/atimad/mlx-m5-bench/actions) for hosted CI, [results](results.md) for the subsequent Metal evidence, and the [release roadmap](roadmap.md) for the release sequence.

The intended owner is atimad, repository name mlx-m5-bench and visibility public. The intended URL is https://github.com/atimad/mlx-m5-bench. The read-only GitHub CLI lookup could not resolve an existing repository on 2026-11-14.

The repository description is "Reproducible CPU vs Apple Silicon GPU benchmarks for classical machine learning, starting with scikit-learn and mlx-learn."

## Planned content

Include original source, packaged YAML profiles, pyproject.toml, uv.lock, Python version, tests, original MIT license, README, contributing guidelines, methodology, reproducibility, upstream review, limitations, phase record, redacted measurement evidence and least-privilege CI/issue templates.

Git exclusions cover local virtual environments, generated datasets, raw results, package distributions, caches and credentials. Curated evidence is reviewed separately for private paths and secrets. Git LFS is unnecessary for this repository.

## Intended actions after explicit approval

```sh
gh repo create atimad/mlx-m5-bench --public --source=. --remote=origin \
  --description "Reproducible CPU vs Apple Silicon GPU benchmarks for classical machine learning, starting with scikit-learn and mlx-learn."
git push -u origin main
gh repo view atimad/mlx-m5-bench --json nameWithOwner,visibility,url
```

Then inspect public file contents, verify the repository URL and observe the first CPU CI run. Public release creation would require a separate requested action.

## Validation record

- The 44 default tests passed, including CPU adapters, failure and timeout handling, reporting, dashboard rendering and filtering, schemas and CLI smoke. Four separately marked Apple Silicon estimator-pair integration tests passed.
- Ruff lint and format, mypy, lock validation and source distribution/wheel builds passed.
- A temporary Python 3.13.18 environment outside the checkout installed locked dependencies and the built wheel. The functional Metal probe and all four quick estimator pairs passed.
- The localhost dashboard opened in the browser and loaded stored standard results. Streamlit AppTest also verified the saved-data and filter paths.
- Canonical quick, standard, full and CPU thread sensitivity runs reference clean benchmark implementation commit 2da33001222d0f6faf649a0512c71735d966b9e8. Subsequent report and dashboard presentation edits preserve the raw measurements. See [results](results.md).
- One standard multiclass logistic workload remains INCONCLUSIVE due to a repeatable line-search warning. Full skipped three workloads as designed. Independent estimator-level GPU traces and GitHub-hosted CI are open.
