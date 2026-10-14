"""Research Task 1: Pandas descriptive statistics, matched to pure_python_stats.py.

Usage: python pandas_stats.py path/to/fb_ads_president_scored_anon.csv
"""
import argparse
import math
from pathlib import Path

import pandas as pd

MISSING = {'', 'n/a', 'na', 'null', 'none', 'nan'}


def clean(value):
    if pd.isna(value):
        return None
    value = str(value).strip()
    return None if value.lower() in MISSING else value


def parse_number(value):
    if value is None:
        return None
    try:
        number = float(value.replace(',', '').replace('$', ''))
        return number if math.isfinite(number) else None
    except ValueError:
        return None


def analyze(path):
    # Read as strings to match the pure Python script's inference rules.
    df = pd.read_csv(path, dtype=str, keep_default_na=False, encoding='utf-8-sig')
    print(f'Dataset: {path.name}')
    print(f'Total rows: {df.shape[0]:,} | Total columns: {df.shape[1]}')
    print('\nRaw Pandas dtypes:')
    print(df.dtypes.to_string())
    print('\nDataFrame info:')
    df.info(verbose=True, show_counts=True)

    cleaned = df.apply(lambda col: col.map(clean))
    missing = cleaned.isna().sum()
    print('\nMissing values per column:')
    for name in cleaned.columns:
        count = int(missing[name])
        print(f'  {name}: {count:,} ({count / len(df) * 100:.2f}%)' if len(df)
              else f'  {name}: {count} (N/A%)')

    for name in cleaned.columns:
        values = cleaned[name].dropna()
        numbers = values.map(parse_number)
        numeric = not values.empty and numbers.notna().all()
        kind = 'numeric' if numeric else ('empty' if values.empty else 'categorical/text')
        print(f'\n--- {name} ({kind}) ---')
        print(f'Nonmissing: {len(values):,} | Missing: {int(missing[name]):,}')
        if numeric:
            series = numbers.astype(float)
            summary = series.describe()  # sample std: ddof=1
            print('Pandas describe():')
            print(summary.to_string())
            print(f'Median: {series.median():,.4f}')
            print(f'Min: {series.min():,.4f} | Max: {series.max():,.4f}')
        else:
            print('Pandas describe(include="all") for categorical values:')
            if not values.empty:
                print(values.describe().to_string())
            else:
                print('  No nonmissing values')
            counts = values.value_counts(dropna=True)
            # Deterministic tie-break matching the pure Python script.
            ranked = sorted(((str(v), int(n)) for v, n in counts.items()),
                            key=lambda item: (-item[1], item[0]))
            print(f'Unique: {values.nunique(dropna=True):,}')
            print(f'Mode and frequency: {ranked[0] if ranked else None}')
            print('Top 5 values by frequency:')
            for label, count in ranked[:5]:
                print(f'  {label[:110]}: {count:,}')
    print('\nNOTE: Structured ranges (spend, impressions, audience) are treated as')
    print('categorical; lower/upper bounds are not exact observed amounts.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file', type=Path, help='Path to professor-provided CSV')
    args = parser.parse_args()
    if not args.csv_file.is_file():
        parser.error(f'File not found: {args.csv_file}')
    analyze(args.csv_file)


if __name__ == '__main__':
    main()
