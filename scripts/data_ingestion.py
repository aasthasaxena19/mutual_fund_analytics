import pandas as pd
import os

DATA_PATH = "data/raw"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    path = os.path.join(DATA_PATH, file)

    print("\n" + "="*60)
    print(file)

    df = pd.read_csv(path)

    print("Shape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())
    # Fund Master Exploration

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master['fund_house'].unique())

print("\nUnique Categories:")
print(fund_master['category'].unique())

print("\nUnique Sub Categories:")
print(fund_master['sub_category'].unique())

print("\nUnique Risk Grades:")
print(fund_master['risk_category'].unique())
fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "data/raw/02_nav_history.csv"
)

master_codes = set(fund['amfi_code'])

nav_codes = set(nav['amfi_code'])

missing = master_codes - nav_codes

print("Missing codes:",missing)