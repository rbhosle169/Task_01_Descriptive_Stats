
# Research Task 1 — Pure Python vs. Pandas

## Objective

Two scripts independently analyzed `fb_ads_president_scored_anon.csv`: `pure_python_stats.py` uses only Python's standard library, while `pandas_stats.py` uses Pandas. Their outputs were reviewed to assess agreement and implementation tradeoffs.

The purpose of this comparison is to evaluate the consistency of descriptive statistics generated using two different approaches and identify the advantages, limitations, and practical considerations of each implementation.

## Agreement in the generated outputs

Both scripts report **246,745 rows and 40 columns**. They also agree on the principal missing-value counts: `ad_delivery_stop_time` = **2,159**, `bylines` = **1,009**, and `estimated_audience_size` = **579**.

Major categorical results agree as well: `page_name` has **4,546** distinct nonmissing values and **Kamala Harris** occurs **55,503** times; `spend` has **44** distinct range strings, with the **0–99** band occurring **135,950** times.

Numeric summaries are consistent at the displayed precision. For instance, the pure Python output reports `illuminating_msg_type_advocacy` mean **0.5486** and sample standard deviation **0.4976**, while Pandas reports mean **0.548631** and standard deviation **0.497630**.

The differing number of displayed decimals is formatting, not evidence of a substantive discrepancy. This review compares printed outputs; it is **not** a machine-precision, column-by-column automated assertion test.

## Type inference and missing data

Pandas initially reads all 40 columns as `object` according to its raw `dtypes` and `info()` output. The analysis script subsequently recognizes the binary indicator columns as numeric for summary calculations.

The pure Python implementation likewise explicitly distinguishes numeric flags from text, identifiers, dates, and structured range strings. This illustrates that loading a CSV does not guarantee meaningful automatic typing.

A useful example is `spend`: values are dictionary-like strings containing `lower_bound` and `upper_bound`. Neither script treats the band as a precise observed amount. Both summarize its categories instead.

Similarly, `impressions` and `estimated_audience_size` are ranges, not scalar numeric columns. A future analysis could extract bounds but would need to state whether it uses minimums, maximums, or midpoint estimates.

The scripts agree on missing values because they apply comparable rules to empty or missing-like entries.

Pandas' raw `info()` display alone is not a reliable missingness report in this implementation: the raw DataFrame displays object columns as fully non-null, while the script's later cleaned missing-value summary correctly identifies missing entries.

This is a reminder to check the cleaning logic rather than rely on the first dtype or non-null display.

## Summary comparison

| Feature | Pure Python | Pandas |
|---|---|---|
| Dataset size | 246,745 rows, 40 columns | 246,745 rows, 40 columns |
| Dependencies | Python standard library | Pandas |
| Data loading | CSV reader | DataFrame |
| Missing-value handling | Explicit checks | Cleaning and missing-value operations |
| Numeric statistics | Explicit calculations | Built-in statistical methods |
| Categorical frequencies | Counter-based counting | value_counts() |
| Unique-value counting | Set-based counting | nunique() |
| Mean and median | Explicit calculations | Built-in methods |
| Standard deviation | Sample standard deviation | Sample standard deviation (ddof=1) |
| Spending ranges | Treated as categories | Treated as categories |
| Main results | Consistent at displayed precision | Consistent at displayed precision |

The two approaches produce matching descriptive conclusions while differing in implementation complexity and convenience.

## Development tradeoffs

### Pure Python

The pure Python implementation makes parsing, type decisions, frequency counting, missing-value handling, and statistical formulas explicit.

**Advantages:**

- Does not require external libraries.
- Provides greater visibility into statistical calculations.
- Makes data-cleaning and type-conversion decisions easier to inspect.
- Helps develop a deeper understanding of descriptive statistics.

**Limitations:**

- Requires more code to perform repetitive operations.
- Needs explicit handling of missing values and unusual strings.
- Requires careful testing of statistical formulas and edge cases.
- Can become harder to maintain as the analysis expands.

### Pandas

The Pandas implementation uses DataFrames and built-in operations such as `describe()`, `value_counts()`, `nunique()`, and missing-value summaries.

**Advantages:**

- Reduces the amount of code required for descriptive analysis.
- Simplifies categorical and numerical summaries.
- Provides convenient DataFrame operations for exploring large datasets.
- Makes it easier to extend the analysis with filtering and grouping.

**Limitations:**

- Requires installing and maintaining an external dependency.
- Automatic type inference may not reflect the meaning of the data.
- Data-cleaning decisions still require explicit validation.
- Analysts must understand the statistical assumptions behind built-in methods.

Both implementations use **sample standard deviation** (`ddof=1`) for numeric columns, supporting a like-for-like comparison.

Printed values have different rounding precision; any future automated comparison should use an explicit numeric tolerance and record its threshold.

## Potential improvements

Although both implementations produced consistent descriptive results, several improvements could strengthen the analysis.

### 1. Automated statistical validation

A future validation script could compare the results of both implementations programmatically rather than relying only on printed output.

For numeric columns, comparisons could use an explicit floating-point tolerance to account for minor computational differences.

This would provide stronger evidence that both approaches produce equivalent statistics.

### 2. Additional data validation

The analysis could introduce further checks for:

- Unexpected or malformed numeric values.
- Invalid or incomplete spending and impression ranges.
- Duplicate advertising identifiers.
- Inconsistent categorical labels.
- Unusual or extreme values.

These checks would help identify potential data-quality issues before statistical calculations.

### 3. Performance benchmarking

Execution time and memory consumption could be measured for both scripts.

This would allow a more systematic comparison of their efficiency when processing large datasets.

No performance advantage is claimed in the current research because execution-time and memory benchmarks were not conducted.

### 4. Expanded analysis of structured ranges

The spending, impression, and audience-size fields could be parsed into separate lower-bound and upper-bound columns.

However, the analysis would need to preserve the uncertainty of reported ranges.

Using a midpoint or other estimate would require a documented assumption and should not be presented as an exact observed value.

### 5. Reproducibility and testing

Additional unit tests could verify how both scripts handle empty columns, missing values, single-value numeric columns, and mixed data types.

Recording the Python and Pandas versions would also improve reproducibility.

These improvements could extend the project without changing its original descriptive-statistics objective.

## Conclusion

The two approaches support the same main descriptive conclusions on this dataset.

Pure Python provides transparency into the underlying statistical calculations and data-processing logic, while Pandas improves convenience, readability, and flexibility for exploratory analysis.

The comparison demonstrates that reliable statistical analysis depends not only on the programming tools used but also on consistent data-cleaning rules, correct type interpretation, and appropriate statistical assumptions.

The most important shared decision is semantic rather than technical: reported spending and impression **ranges should not be misrepresented as exact values**.

Overall, the project demonstrates how two different Python-based approaches can produce consistent descriptive results while offering different benefits for implementation, learning, and future research.
