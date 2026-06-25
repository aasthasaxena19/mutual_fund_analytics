# Data Quality & Anomaly Report

## 01_fund_master.csv

* No missing values detected.
* All 15 columns contain complete records.
* No anomaly identified from initial profiling.

## 02_nav_history.csv

* No missing values detected.
* NAV history records appear complete.
* No anomaly identified from initial profiling.

## 03_aum_by_fund_house.csv

* No missing values detected.
* AUM and scheme count fields are complete.
* No anomaly identified from initial profiling.

## 04_monthly_sip_inflows.csv

### Anomaly: Missing YoY Growth Values

* Column: `yoy_growth_pct`
* Missing Records: 12
* Severity: Low
* Explanation: The first 12 months of the dataset do not have corresponding prior-year observations required for Year-over-Year (YoY) growth calculation. Therefore, null values are expected and do not indicate a data quality issue.

## 05_category_inflows.csv

* No missing values detected.
* No anomaly identified from initial profiling.

## 06_industry_folio_count.csv

* No missing values detected.
* No anomaly identified from initial profiling.

## 07_scheme_performance.csv

* No missing values detected.
* No anomaly identified from initial profiling.

## 08_investor_transactions.csv

* No missing values detected.
* No anomaly identified from initial profiling.

## 09_portfolio_holdings.csv

* No missing values detected.
* No anomaly identified from initial profiling.

## 10_benchmark_indices.csv

* No missing values detected.
* No anomaly identified from initial profiling.

## Summary

* Total datasets reviewed: 10
* Datasets with anomalies: 1
* Total anomaly observations: 12 missing values in `yoy_growth_pct`
* Assessment: Dataset quality is generally good. The identified missing values are expected because YoY calculations require prior-year data.
