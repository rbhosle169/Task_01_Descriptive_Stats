# Research Task 1 — Pure Python vs. Pandas

## Objective

Two scripts independently analyzed `fb_ads_president_scored_anon.csv`: `pure_python_stats.py` uses only Python's standard library, while `pandas_stats.py` uses Pandas. Their outputs were reviewed to assess agreement and implementation tradeoffs.

## Agreement in the generated outputs

Both scripts report **246,745 rows and 40 columns**. They also agree on the principal missing-value counts: `ad_delivery_stop_time` = **2,159**, `bylines` = **1,009**, and `estimated_audience_size` = **579**. Major categorical results agree as well: `page_name` has **4,546** distinct nonmissing values and **Kamala Harris** occurs **55,503** times; `spend` has **44** distinct range strings, with the **0–99** band occurring **135,950** times.

Numeric summaries are consistent at the displayed precision. For instance, the pure Python output reports `illuminating_msg_type_advocacy` mean **0.5486** and sample standard deviation **0.4976**, while Pandas reports mean **0.548631** and standard deviation **0.497630**. The differing number of displayed decimals is formatting, not evidence of a substantive discrepancy. This review compares printed outputs; it is **not** a machine-precision, column-by-column automated assertion test.

## Type inference and missing data

Pandas initially reads all 40 columns as `object` according to its raw `dtypes` and `info()` output. The analysis script subsequently recognizes the binary indicator columns as numeric for summary calculations. The pure Python implementation likewise explicitly distinguishes numeric flags from text, identifiers, dates, and structured range strings. This illustrates that loading a CSV does not guarantee meaningful automatic typing.

A useful example is `spend`: values are dictionary-like strings containing `lower_bound` and `upper_bound`. Neither script treats the band as a precise observed amount. Both summarize its categories instead. Similarly, `impressions` and `estimated_audience_size` are ranges, not scalar numeric columns. A future analysis could extract bounds but would need to state whether it uses minimums, maximums, or midpoint estimates.

The scripts agree on missing values because they apply comparable rules to empty or missing-like entries. Pandas' raw `info()` display alone is not a reliable missingness report in this implementation: the raw DataFrame displays object columns as fully non-null, while the script's later cleaned missing-value summary correctly identifies missing entries. This is a reminder to check the cleaning logic rather than rely on the first dtype or non-null display.

## Development tradeoffs

**Pure Python** makes parsing, type decisions, frequency counting, missing-value handling, and statistical formulas explicit. This helps explain how summary statistics work and makes the handling of unusual strings visible, but requires more code and careful edge-case testing.

**Pandas** offers concise operations such as `describe()`, `value_counts()`, `nunique()`, and missing-value summaries. It makes exploratory analysis faster, but the analyst still needs to inspect inferred types and choose appropriate conversions. Pandas is not a substitute for understanding what a column represents.

Both implementations use **sample standard deviation** (`ddof=1`) for numeric columns, which supports a like-for-like comparison. Printed values have different rounding precision; any future automated comparison should use an explicit numeric tolerance and record its threshold.

## Conclusion

The two approaches support the same main descriptive conclusions on this dataset. Pure Python provides transparency into the mechanics; Pandas improves convenience and readability. The most important shared decision is semantic rather than technical: reported spending and impression *ranges* should not be misrepresented as exact values.
