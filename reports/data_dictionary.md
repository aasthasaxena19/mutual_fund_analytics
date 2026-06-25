# Data Dictionary

## dim_fund

| Column       | Type    | Description               |
| ------------ | ------- | ------------------------- |
| fund_id      | INTEGER | Unique fund identifier    |
| amfi_code    | INTEGER | Official AMFI scheme code |
| scheme_name  | TEXT    | Mutual fund scheme name   |
| fund_house   | TEXT    | Asset Management Company  |
| category     | TEXT    | Fund category             |
| sub_category | TEXT    | Fund sub-category         |

## fact_nav

| Column  | Type    | Description     |
| ------- | ------- | --------------- |
| nav_id  | INTEGER | NAV record id   |
| fund_id | INTEGER | Fund reference  |
| date_id | INTEGER | Date reference  |
| nav     | REAL    | Net Asset Value |

## fact_transactions

| Column  | Type    | Description        |
| ------- | ------- | ------------------ |
| txn_id  | INTEGER | Transaction ID     |
| fund_id | INTEGER | Fund reference     |
| date_id | INTEGER | Date reference     |
| amount  | REAL    | Transaction amount |

## fact_performance

| Column     | Type | Description       |
| ---------- | ---- | ----------------- |
| return_1yr | REAL | One-year return   |
| return_3yr | REAL | Three-year return |
| return_5yr | REAL | Five-year return  |

## fact_aum

| Column | Type | Description             |
| ------ | ---- | ----------------------- |
| aum    | REAL | Assets Under Management |
