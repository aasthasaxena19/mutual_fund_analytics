CREATE TABLE dim_fund(
    fund_id INTEGER PRIMARY KEY,
    amfi_code INTEGER UNIQUE,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    sub_category TEXT
);

CREATE TABLE dim_date(
    date_id INTEGER PRIMARY KEY,
    full_date DATE
);

CREATE TABLE fact_nav(
    nav_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    nav REAL,
    FOREIGN KEY(fund_id)
    REFERENCES dim_fund(fund_id)
);

CREATE TABLE fact_transactions(
    txn_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    date_id INTEGER,
    amount REAL
);

CREATE TABLE fact_performance(
    performance_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    return_1yr REAL,
    return_3yr REAL,
    return_5yr REAL
);

CREATE TABLE fact_aum(
    aum_id INTEGER PRIMARY KEY,
    fund_id INTEGER,
    aum REAL
);