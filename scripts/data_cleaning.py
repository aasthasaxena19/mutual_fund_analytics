import pandas as pd
import os

os.makedirs(
    "data/processed",
    exist_ok=True
)

os.makedirs(
    "reports",
    exist_ok=True
)
fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

fund = fund.drop_duplicates()

fund['expense_ratio_pct'] = pd.to_numeric(
    fund['expense_ratio_pct'],
    errors='coerce'
)

fund = fund[
    fund['expense_ratio_pct'] >= 0
]

fund.to_csv(
    "data/processed/01_fund_master.csv",
    index=False
)
nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

nav['date'] = pd.to_datetime(nav['date'])

nav = nav.sort_values(
    ['amfi_code','date']
)

nav['nav'] = nav.groupby(
    'amfi_code'
)['nav'].ffill()

nav = nav.drop_duplicates()

nav = nav[
    nav['nav'] > 0
]

nav.to_csv(
    "data/processed/02_nav_history.csv",
    index=False
)
aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

aum['date'] = pd.to_datetime(
    aum['date']
)

aum = aum.drop_duplicates()

aum = aum[
    aum['aum_crore'] > 0
]

aum.to_csv(
    "data/processed/03_aum_by_fund_house.csv",
    index=False
)
sip = pd.read_csv(
    "data/raw/04_monthly_sip_inflows.csv"
)

sip = sip.drop_duplicates()

sip['yoy_growth_pct'] = (
    sip['yoy_growth_pct']
    .fillna(0)
)

sip.to_csv(
    "data/processed/04_monthly_sip_inflows.csv",
    index=False
)
cat = pd.read_csv(
    "data/raw/05_category_inflows.csv"
)

cat = cat.drop_duplicates()

cat['net_inflow_crore'] = pd.to_numeric(
    cat['net_inflow_crore'],
    errors='coerce'
)

cat.to_csv(
    "data/processed/05_category_inflows.csv",
    index=False
)
folio = pd.read_csv(
    "data/raw/06_industry_folio_count.csv"
)

folio = folio.drop_duplicates()

folio.to_csv(
    "data/processed/06_industry_folio_count.csv",
    index=False
)
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

returns_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct'
]

for col in returns_cols:

    if col in perf.columns:

        perf[col] = pd.to_numeric(
            perf[col],
            errors='coerce'
        )

# Expense ratio validation

if 'expense_ratio_pct' in perf.columns:

    anomalies = perf[
        (perf['expense_ratio_pct'] < 0.1) |
        (perf['expense_ratio_pct'] > 2.5)
    ]

    print(
        f"Expense Ratio Anomalies: {len(anomalies)}"
    )

    anomalies.to_csv(
        "reports/performance_anomalies.csv",
        index=False
    )

perf.to_csv(
    "data/processed/07_scheme_performance.csv",
    index=False
)
tx = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

tx['transaction_type'] = (
    tx['transaction_type']
    .astype(str)
    .str.upper()
    .str.strip()
)

allowed = [
    'SIP',
    'LUMPSUM',
    'REDEMPTION'
]

tx = tx[
    tx['transaction_type'].isin(
        allowed
    )
]

tx['amount_inr'] = pd.to_numeric(
    tx['amount_inr'],
    errors='coerce'
)

tx = tx[
    tx['amount_inr'] > 0
]

tx['transaction_date'] = pd.to_datetime(
    tx['transaction_date'],
    errors='coerce'
)

# KYC Validation

if 'kyc_status' in tx.columns:

    tx['kyc_status'] = (
        tx['kyc_status']
        .astype(str)
        .str.upper()
        .str.strip()
    )

    valid_kyc = [
        'VERIFIED',
        'PENDING',
        'REJECTED'
    ]

    invalid_kyc = tx[
        ~tx['kyc_status'].isin(
            valid_kyc
        )
    ]

    print(
        f"Invalid KYC Rows: {len(invalid_kyc)}"
    )

tx.to_csv(
    "data/processed/08_investor_transactions.csv",
    index=False
)
portfolio = pd.read_csv(
    "data/raw/09_portfolio_holdings.csv"
)

portfolio = portfolio.drop_duplicates()

portfolio['weight_pct'] = pd.to_numeric(
    portfolio['weight_pct'],
    errors='coerce'
)

portfolio = portfolio[
    portfolio['weight_pct'] > 0
]

portfolio.to_csv(
    "data/processed/09_portfolio_holdings.csv",
    index=False
)
benchmark = pd.read_csv(
    "data/raw/10_benchmark_indices.csv"
)

benchmark['date'] = pd.to_datetime(
    benchmark['date']
)

benchmark = benchmark.drop_duplicates()

benchmark = benchmark[
    benchmark['close_value'] > 0
]

benchmark.to_csv(
    "data/processed/10_benchmark_indices.csv",
    index=False
)