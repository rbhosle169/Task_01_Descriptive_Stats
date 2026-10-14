"""Research Task 1: descriptive statistics using Python's standard library only.

Usage: python pure_python_stats.py path/to/fb_ads_president_scored_anon.csv
"""
import argparse
import csv
import math
from collections import Counter
from pathlib import Path

MISSING = {'', 'n/a', 'na', 'null', 'none', 'nan'}


def is_missing(value):
    return value is None or value.strip().lower() in MISSING


def as_number(value):
    """Parse ordinary numeric values; leave range/dict/list strings categorical."""
    try:
        number = float(value.strip().replace(',', '').replace('$', ''))
        return number if math.isfinite(number) else None
    except (AttributeError, ValueError):
        return None


def numeric_stats(numbers):
    numbers = sorted(numbers)
    n = len(numbers)
    if not n:
        return None
    mean = sum(numbers) / n
    mid = n // 2
    median = numbers[mid] if n % 2 else (numbers[mid - 1] + numbers[mid]) / 2
    variance = sum((x - mean) ** 2 for x in numbers) / (n - 1) if n > 1 else 0.0
    return {'count': n, 'mean': mean, 'min': numbers[0], 'max': numbers[-1],
            'median': median, 'std_dev_sample': math.sqrt(variance)}


def categorical_stats(values):
    counts = Counter(values)
    top = sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))[:5]
    return {'count': len(values), 'unique': len(counts),
            'mode': top[0] if top else None, 'top_5': top}


def analyze(path):
    with path.open('r', encoding='utf-8-sig', newline='') as handle:
        reader = csv.DictReader(handle)
        columns = reader.fieldnames
        if not columns:
            raise ValueError('The CSV has no header columns.')
        values = {name: [] for name in columns}
        total_rows = 0
        for row in reader:
            total_rows += 1
            for name in columns:
                values[name].append(row.get(name))

    print(f'Dataset: {path.name}')
    print(f'Total rows: {total_rows:,} | Total columns: {len(columns)}')
    print('Numeric columns use sample standard deviation (ddof=1).')
    print('Structured ranges (spend, impressions, audience) remain categorical here;')
    print('their lower/upper bounds are NOT assumed to be exact spending amounts.\n')

    for name in columns:
        nonmissing = [v.strip() for v in values[name] if not is_missing(v)]
        missing_count = total_rows - len(nonmissing)
        parsed = [as_number(v) for v in nonmissing]
        # A column is numeric only if every nonmissing value parses as numeric.
        numeric = bool(nonmissing) and all(n is not None for n in parsed)
        kind = 'numeric' if numeric else ('empty' if not nonmissing else 'categorical/text')
        print(f'\n--- {name} ({kind}) ---')
        print(f'Nonmissing: {len(nonmissing):,} | Missing: {missing_count:,}')
        if numeric:
            for metric, result in numeric_stats(parsed).items():
                print(f'  {metric}: {result:,.4f}' if isinstance(result, float)
                      else f'  {metric}: {result:,}')
        else:
            stats = categorical_stats(nonmissing)
            print(f"  Unique: {stats['unique']:,}")
            print(f"  Mode and frequency: {stats['mode']}")
            print('  Top 5 values by frequency:')
            for label, count in stats['top_5']:
                print(f'    {label[:110]}: {count:,}')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv_file', type=Path, help='Path to professor-provided CSV')
    args = parser.parse_args()
    if not args.csv_file.is_file():
        parser.error(f'File not found: {args.csv_file}')
    analyze(args.csv_file)


if __name__ == '__main__':
    main()
