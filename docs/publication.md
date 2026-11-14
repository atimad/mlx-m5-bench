# Publication checkpoint

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

Final validation results, implementation commit and canonical measurement references are appended after the local verification pass. Independent estimator-level GPU trace verification remains open. Current results label library-reported GPU, mixed execution, CPU paths and unknown index construction.
