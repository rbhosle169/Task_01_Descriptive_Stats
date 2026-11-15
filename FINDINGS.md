# Research Task 1 — Findings

## Scope and approach

This analysis examines `fb_ads_president_scored_anon.csv`, a dataset of 246,745 records and 40 columns concerning political advertising around the 2024 U.S. presidential election. Two independently implemented scripts—one using only the Python standard library and another using Pandas—summarized each field. The figures below are based on their generated output files. Each row represents an ad record; counts should not be interpreted as unique individuals reached or dollars spent.

## Advertising pages and sponsoring organizations

The dataset contains 4,546 distinct `page_name` values. The most frequent page name is **Kamala Harris** (55,503 records), followed by **Donald J. Trump** (23,988), **Joe Biden** (14,822), **The Daily Scroll** (10,461), and **Kamala HQ** (7,564). These are counts of records associated with page names, not spending rankings. A page may have many ads, and the number of ads does not establish its total expenditure.

The `bylines` field, which identifies ad disclaimers/sponsors, has 3,786 distinct nonmissing values. Its most frequent entries are **HARRIS FOR PRESIDENT** (49,788), **HARRIS VICTORY FUND** (32,612), **BIDEN VICTORY FUND** (15,539), **DONALD J. TRUMP FOR PRESIDENT 2024, INC.** (15,112), and **Trump National Committee JFC** (7,279). The difference between `page_name` and `bylines` illustrates why an advertising page and a sponsoring organization should not automatically be treated as the same entity.

## Timing of ad activity

Ad creation dates are concentrated around late October 2024. The most frequent `ad_creation_time` is **2024-10-27** (8,619 records), followed by October 28 (7,356), October 26 (6,414), October 23 (5,021), and October 25 (4,769). The most frequent delivery start date is **2024-10-28** (10,089 records). The most frequent nonmissing delivery stop date is **2024-11-05** (14,222 records). These patterns are consistent with heightened activity near Election Day, but the descriptive results alone cannot establish why individual campaigns chose those dates.

## Spending, impressions, and platforms

The `spend`, `impressions`, and `estimated_audience_size` fields contain **reported ranges**, not exact numeric measurements. The most common spend band is **0–99** in the stated currency (135,950 records), followed by 100–199 (24,593) and 200–299 (13,797). Because the dataset includes 18 currency values, even range-based expenditure comparisons require currency-aware filtering or conversion. **USD** is the dominant currency (246,599 records). No total dollar-spend ranking is claimed here: adding categorical ranges or treating their bounds as exact amounts would be misleading.

The most frequent impressions band is **0–999** (80,822 records). Most records list both Facebook and Instagram as publisher platforms (214,434), while 23,259 list Facebook alone and 8,395 Instagram alone. These are platform-list combinations, not mutually exclusive reach totals.

## Message categories and topics

The numeric 0/1 classification fields offer a different perspective on the records. For example, `illuminating_msg_type_cta` has a mean of approximately **0.5728**, `illuminating_msg_type_advocacy` **0.5486**, `illuminating_msg_type_issue` **0.3816**, and `illuminating_msg_type_attack` **0.2719**. If these are binary flags as their values indicate, their means correspond to the proportion of records flagged in each category. Categories may overlap and should not be added to 100%.

Among topic flags, `illuminating_topic_economy` averages **0.1221**, `illuminating_topic_health` **0.1092**, and `illuminating_topic_social_and_cultural` **0.1058**. These summarize classifications present in the supplied data; they do not establish the effectiveness or factual accuracy of the advertisements.

## Data quality and limitations

Three fields have missing entries: `ad_delivery_stop_time` (2,159; approximately 0.87%), `bylines` (1,009; approximately 0.41%), and `estimated_audience_size` (579; approximately 0.23%). The other fields have no missing values under the scripts' missing-value rules. The `illuminating_mentions` field is a list-like string: its most common value is `[]` (73,205 records), so a blank mention list must not be confused with a missing cell. Candidate mentions can also use variants such as “Donald Trump” and “President Trump”; a robust candidate-level comparison would normalize these labels.

The present analysis is descriptive. It does not infer causation, assess ad effectiveness, identify unique viewers, or calculate precise spending totals. Further work could parse spending bounds, normalize candidate mentions, and compare ad volumes by date and sponsor using documented assumptions.
