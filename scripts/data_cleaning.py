import pandas as pd
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

nav = nav[nav['nav'] > 0]
nav.to_csv(
    "data/processed/02_nav_history.csv",
    index=False
)
tx = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

tx['transaction_type'] = (
    tx['transaction_type']
    .str.upper()
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
    tx['transaction_date']
)

tx.to_csv(
    "data/processed/08_investor_transactions.csv",
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

    perf[col] = pd.to_numeric(
        perf[col],
        errors='coerce'
    )

anomalies = perf[
    perf['expense_ratio_pct'] > 2.5
]

print(anomalies)