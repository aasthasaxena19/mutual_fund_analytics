# Data Quality & Anomaly Report

## 01_fund_master.csv

* No missing values detected.
* All 15 columns contain complete records.
* No anomaly identified from initial profiling.

### Fund Master Exploration

**Unique Fund Houses (10)**

* SBI Mutual Fund
* HDFC Mutual Fund
* ICICI Prudential MF
* Nippon India MF
* Kotak Mahindra MF
* Axis Mutual Fund
* Aditya Birla Sun Life MF
* UTI Mutual Fund
* Mirae Asset MF
* DSP Mutual Fund

**Categories (2)**

* Equity
* Debt

**Sub-Categories (12)**

* Large Cap
* Mid Cap
* Small Cap
* Flexi Cap
* Value
* ELSS
* Index
* Index/ETF
* Liquid
* Gilt
* Short Duration
* Large & Mid Cap

**Risk Categories**

* Low
* Moderate
* Moderately High
* High
* Very High

### AMFI Scheme Code Structure

Each mutual fund scheme is identified using a unique AMFI code. The AMFI code acts as the primary key across datasets and APIs and is used to:

* Link fund master and NAV history datasets
* Fetch NAV data from mfapi.in
* Support analytics and reporting in SQLite

Example AMFI Codes:

* 125497 → HDFC Top 100 Fund Direct Growth
* 119551 → SBI Bluechip Fund Regular Growth
* 120503 → ICICI Prudential Bluechip Fund Regular Growth

---

## 02_nav_history.csv

* No missing values detected.
* NAV history records appear complete.
* No anomaly identified from initial profiling.

### AMFI Code Validation

* Total schemes in fund_master.csv: 40
* Total AMFI codes in NAV history: 40
* Missing AMFI codes: 0

**Result:** All AMFI codes present in fund_master.csv were successfully found in nav_history.csv. No referential integrity issues were detected.

---

## 03_aum_by_fund_house.csv

* No missing values detected.
* AUM and scheme count fields are complete.
* No anomaly identified from initial profiling.

---

## 04_monthly_sip_inflows.csv

### Anomaly: Missing YoY Growth Values

* Column: `yoy_growth_pct`
* Missing Records: 12
* Severity: Low
* Explanation: The first 12 months of the dataset do not have corresponding prior-year observations required for Year-over-Year (YoY) growth calculation. Therefore, null values are expected and do not indicate a data quality issue.

---

## 05_category_inflows.csv

* No missing values detected.
* No anomaly identified from initial profiling.

---

## 06_industry_folio_count.csv

* No missing values detected.
* No anomaly identified from initial profiling.

---

## 07_scheme_performance.csv

* No missing values detected.
* All return metrics were successfully interpreted as numeric values.
* Expense ratios fall within the expected range of 0.1%–2.5%.
* No performance anomalies detected.

---

## 08_investor_transactions.csv

* No missing values detected.
* Transaction types are standardized.
* Transaction amount fields are complete and valid.
* No anomaly identified from initial profiling.

---

## 09_portfolio_holdings.csv

* No missing values detected.
* No anomaly identified from initial profiling.

---

## 10_benchmark_indices.csv

* No missing values detected.
* No anomaly identified from initial profiling.

---

# Summary

* Total datasets reviewed: 10
* Datasets with anomalies: 1
* Total anomaly observations: 12 missing values in `yoy_growth_pct`
* AMFI Code Validation: Passed
* Fund Master Exploration: Completed
* Assessment: Dataset quality is generally good. The identified missing values are expected because YoY calculations require prior-year data. All AMFI scheme codes were successfully validated and the datasets are suitable for downstream analytics and database loading.

## SQLite Data Load Validation

The cleaned datasets were successfully loaded into SQLite using SQLAlchemy.

### Row Count Verification

| Table | Rows |
|---------|---------|
| dim_fund | 40 |
| fact_nav | 46000 |
| fact_transactions | 32000 |
| fact_performance | 40 |
| fact_aum | 90 |

Result: Row counts successfully matched the source CSV datasets. No data loss was observed during database loading.