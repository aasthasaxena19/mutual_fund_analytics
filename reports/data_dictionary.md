# Mutual Fund Analytics Project - Data Dictionary

## Dataset 01: Fund Master

| Column             | Data Type | Business Definition                 | Source     |
| ------------------ | --------- | ----------------------------------- | ---------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier       | AMFI India |
| fund_house         | Text      | Asset Management Company (AMC) name | AMFI India |
| scheme_name        | Text      | Mutual fund scheme name             | AMFI India |
| category           | Text      | High-level scheme category          | AMFI India |
| sub_category       | Text      | Detailed scheme classification      | AMFI India |
| plan               | Text      | Regular or Direct plan              | AMFI India |
| launch_date        | Date      | Scheme launch date                  | AMFI India |
| benchmark          | Text      | Benchmark index used for comparison | AMFI India |
| expense_ratio_pct  | Decimal   | Annual expense ratio (%)            | AMFI India |
| exit_load_pct      | Decimal   | Exit load charged on redemption     | AMFI India |
| min_sip_amount     | Integer   | Minimum SIP investment amount       | AMFI India |
| min_lumpsum_amount | Integer   | Minimum lump sum investment         | AMFI India |
| fund_manager       | Text      | Scheme fund manager                 | AMFI India |
| risk_category      | Text      | Risk classification of scheme       | AMFI India |
| sebi_category_code | Text      | SEBI category code                  | AMFI India |

---

## Dataset 02: NAV History

| Column    | Data Type | Business Definition      | Source   |
| --------- | --------- | ------------------------ | -------- |
| amfi_code | Integer   | AMFI scheme identifier   | mfapi.in |
| date      | Date      | NAV date                 | mfapi.in |
| nav       | Decimal   | Net Asset Value per unit | mfapi.in |

---

## Dataset 03: AUM by Fund House

| Column     | Data Type | Business Definition               | Source       |
| ---------- | --------- | --------------------------------- | ------------ |
| fund_house | Text      | AMC name                          | AMFI Reports |
| date       | Date      | Quarter-end date                  | AMFI Reports |
| aum_crore  | Decimal   | Assets Under Management (₹ Crore) | AMFI Reports |

---

## Dataset 04: Monthly SIP Inflows

| Column                    | Data Type | Business Definition              | Source            |
| ------------------------- | --------- | -------------------------------- | ----------------- |
| month                     | Date      | Reporting month                  | AMFI Monthly Note |
| sip_inflow_crore          | Decimal   | Monthly SIP inflow (₹ Crore)     | AMFI Monthly Note |
| active_sip_accounts_crore | Decimal   | Active SIP accounts              | AMFI Monthly Note |
| new_registrations_lakh    | Decimal   | New SIP registrations            | AMFI Monthly Note |
| sip_aum_crore             | Decimal   | SIP Assets Under Management      | AMFI Monthly Note |
| yoy_growth_pct            | Decimal   | Year-over-Year growth percentage | Derived           |

---

## Dataset 05: Category Inflows

| Column           | Data Type | Business Definition           | Source            |
| ---------------- | --------- | ----------------------------- | ----------------- |
| category         | Text      | Fund category                 | AMFI Monthly Note |
| month            | Date      | Reporting month               | AMFI Monthly Note |
| net_inflow_crore | Decimal   | Net category inflow (₹ Crore) | AMFI Monthly Note |

---

## Dataset 06: Industry Folio Count

| Column            | Data Type | Business Definition        | Source     |
| ----------------- | --------- | -------------------------- | ---------- |
| date              | Date      | Reporting date             | AMFI India |
| category          | Text      | Equity/Debt/Hybrid         | AMFI India |
| folio_count_crore | Decimal   | Total folio count in crore | AMFI India |

---

## Dataset 07: Scheme Performance

| Column            | Data Type | Business Definition                  | Source      |
| ----------------- | --------- | ------------------------------------ | ----------- |
| amfi_code         | Integer   | Scheme identifier                    | Derived     |
| scheme_name       | Text      | Mutual fund scheme                   | Derived     |
| return_1yr_pct    | Decimal   | One-year return (%)                  | Derived     |
| return_3yr_pct    | Decimal   | Three-year return (%)                | Derived     |
| return_5yr_pct    | Decimal   | Five-year return (%)                 | Derived     |
| alpha             | Decimal   | Alpha performance metric             | Derived     |
| beta              | Decimal   | Beta performance metric              | Derived     |
| sharpe_ratio      | Decimal   | Risk-adjusted return metric          | Derived     |
| sortino_ratio     | Decimal   | Downside-risk adjusted return metric | Derived     |
| std_dev_ann_pct   | Decimal   | Annualized volatility (%)            | Derived     |
| max_drawdown_pct  | Decimal   | Maximum drawdown (%)                 | Derived     |
| expense_ratio_pct | Decimal   | Expense ratio (%)                    | Fund Master |

---

## Dataset 08: Investor Transactions

| Column           | Data Type | Business Definition        | Source    |
| ---------------- | --------- | -------------------------- | --------- |
| investor_id      | Integer   | Unique investor identifier | Simulated |
| amfi_code        | Integer   | Scheme identifier          | Simulated |
| transaction_date | Date      | Transaction date           | Simulated |
| transaction_type | Text      | SIP, Lumpsum, Redemption   | Simulated |
| amount_inr       | Decimal   | Transaction amount (₹)     | Simulated |
| state            | Text      | Investor state             | Simulated |
| age_group        | Text      | Investor demographic group | Simulated |
| kyc_status       | Text      | KYC verification status    | Simulated |

---

## Dataset 09: Portfolio Holdings

| Column     | Data Type | Business Definition  | Source                   |
| ---------- | --------- | -------------------- | ------------------------ |
| amfi_code  | Integer   | Scheme identifier    | AMC Portfolio Disclosure |
| stock_name | Text      | Equity holding name  | AMC Portfolio Disclosure |
| sector     | Text      | Industry sector      | AMC Portfolio Disclosure |
| weight_pct | Decimal   | Portfolio weight (%) | AMC Portfolio Disclosure |

---

## Dataset 10: Benchmark Indices

| Column      | Data Type | Business Definition  | Source    |
| ----------- | --------- | -------------------- | --------- |
| date        | Date      | Trading date         | NSE / BSE |
| index_name  | Text      | Benchmark index name | NSE / BSE |
| close_value | Decimal   | Closing index value  | NSE / BSE |

---

# Source References

* AMFI India ([www.amfiindia.com](http://www.amfiindia.com))
* mfapi.in
* mfdata.in
* NSE India
* BSE India
* AMFI Monthly Notes

# Purpose

This data dictionary documents all major datasets, columns, data types, business meanings, and source references used in the Mutual Fund Analytics Capstone Project.
