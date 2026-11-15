
# Research Task 1: Descriptive Statistics with and without Pandas

Analysis of the professor-provided 2024 Facebook political advertising dataset using two independent approaches: Python's standard library and Pandas.

## Files

- `pure_python_stats.py` — descriptive statistics without third-party packages
- `pandas_stats.py` — corresponding Pandas analysis
- `requirements.txt` — dependency installation
- `FINDINGS.md` — narrative interpretation of the data
- `COMPARISON.md` — methodological comparison and validation notes

## Dataset

**File:** `fb_ads_president_scored_anon.csv`

**Source:** Syracuse University research assignment, *Google Drive: 2024 Facebook Political Ads* (professor-provided dataset). Replace this description with the original shared source URL if you have permission to share it.

The dataset is **not included in this public repository**. Obtain it through the authorized course/research distribution and place it in the project folder locally. The analyzed version has 246,745 rows and 40 columns.

## Run locally

Python 3.11 or newer is recommended.

```bash
python -m pip install -r requirements.txt
python pure_python_stats.py fb_ads_president_scored_anon.csv > pure_python_results.txt
python pandas_stats.py fb_ads_president_scored_anon.csv > pandas_results.txt
```

Run the commands from the folder containing the scripts and the downloaded CSV. The `.txt` outputs are generated locally; do not publish the dataset itself.

## Findings at a glance

- The most frequent `page_name` is **Kamala Harris** (55,503 records), followed by **Donald J. Trump** (23,988).
- The most common ad creation date is **2024-10-27** (8,619 records).
- The most frequent reported spending band is **0–99** in the record's currency (135,950 records). These are **ranges**, not exact spend totals.
- Missing entries occur in `ad_delivery_stop_time` (2,159), `bylines` (1,009), and `estimated_audience_size` (579).

See [FINDINGS.md](FINDINGS.md) for interpretation and limitations.

## Comparing the approaches

The generated outputs agree on row and column counts, missing-value totals, major categorical frequencies, and numeric summaries at displayed precision. Both methods use sample standard deviation for numeric fields. The scripts deliberately leave spend, impressions, and audience bounds as categorical strings rather than inventing exact values. See [COMPARISON.md](COMPARISON.md).

## Limitations and reproducibility

The current analysis summarizes ad-record counts and binary classification fields; it does not estimate total spending or causal effects. `page_name` counts are not spending rankings. The results depend on the supplied dataset version and the scripts' missing-value/type-detection conventions. For strict reproducibility, retain the dataset privately and record its provenance and checksum in your local research notes.
