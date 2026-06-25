from sqlalchemy import create_engine
import pandas as pd

# ---------------------------------
# Create SQLite Database
# ---------------------------------

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

print("Database created successfully")

# ---------------------------------
# Load dim_fund
# ---------------------------------

fund = pd.read_csv(
    "data/processed/01_fund_master.csv"
)

fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"dim_fund loaded: {len(fund)} rows"
)

# ---------------------------------
# Load fact_nav
# ---------------------------------

nav = pd.read_csv(
    "data/processed/02_nav_history.csv"
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_nav loaded: {len(nav)} rows"
)

# ---------------------------------
# Load fact_aum
# ---------------------------------

aum = pd.read_csv(
    "data/processed/03_aum_by_fund_house.csv"
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_aum loaded: {len(aum)} rows"
)

# ---------------------------------
# Load monthly_sip_inflows
# ---------------------------------

sip = pd.read_csv(
    "data/processed/04_monthly_sip_inflows.csv"
)

sip.to_sql(
    "monthly_sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"monthly_sip_inflows loaded: {len(sip)} rows"
)

# ---------------------------------
# Load category_inflows
# ---------------------------------

category = pd.read_csv(
    "data/processed/05_category_inflows.csv"
)

category.to_sql(
    "category_inflows",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"category_inflows loaded: {len(category)} rows"
)

# ---------------------------------
# Load industry_folio_count
# ---------------------------------

folio = pd.read_csv(
    "data/processed/06_industry_folio_count.csv"
)

folio.to_sql(
    "industry_folio_count",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"industry_folio_count loaded: {len(folio)} rows"
)

# ---------------------------------
# Load fact_performance
# ---------------------------------

perf = pd.read_csv(
    "data/processed/07_scheme_performance.csv"
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_performance loaded: {len(perf)} rows"
)

# ---------------------------------
# Load fact_transactions
# ---------------------------------

txn = pd.read_csv(
    "data/processed/08_investor_transactions.csv"
)

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"fact_transactions loaded: {len(txn)} rows"
)

# ---------------------------------
# Load portfolio_holdings
# ---------------------------------

holdings = pd.read_csv(
    "data/processed/09_portfolio_holdings.csv"
)

holdings.to_sql(
    "portfolio_holdings",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"portfolio_holdings loaded: {len(holdings)} rows"
)

# ---------------------------------
# Load benchmark_indices
# ---------------------------------

bench = pd.read_csv(
    "data/processed/10_benchmark_indices.csv"
)

bench.to_sql(
    "benchmark_indices",
    engine,
    if_exists="replace",
    index=False
)

print(
    f"benchmark_indices loaded: {len(bench)} rows"
)

# ---------------------------------
# Verification
# ---------------------------------

tables = [
    "dim_fund",
    "fact_nav",
    "fact_aum",
    "monthly_sip_inflows",
    "category_inflows",
    "industry_folio_count",
    "fact_performance",
    "fact_transactions",
    "portfolio_holdings",
    "benchmark_indices"
]

print("\n===== ROW COUNTS =====")

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) as rows FROM {table}",
        engine
    )

    print(
        f"{table}: {count['rows'][0]} rows"
    )

print("\nAll tables loaded successfully!")