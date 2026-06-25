import pandas as pd

fund = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

print("\nCOLUMNS:")
print(fund.columns.tolist())

print("\n===== UNIQUE FUND HOUSES =====")
if 'fund_house' in fund.columns:
    print(fund['fund_house'].unique())

print("\n===== UNIQUE CATEGORIES =====")
if 'category' in fund.columns:
    print(fund['category'].unique())

print("\n===== UNIQUE SUB-CATEGORIES =====")
if 'sub_category' in fund.columns:
    print(fund['sub_category'].unique())

print("\n===== UNIQUE RISK GRADES =====")
if 'risk_grade' in fund.columns:
    print(fund['risk_grade'].unique())
else:
    print("risk_grade column not found")
    perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

print(
    perf['risk_grade'].unique()
)