import pandas as pd

fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/raw/02_nav_history.csv")

fund_codes = set(fund["amfi_code"])
nav_codes = set(nav["amfi_code"])

missing = fund_codes - nav_codes

print("Fund Master Codes:", len(fund_codes))
print("NAV History Codes:", len(nav_codes))
print("Missing Codes:", len(missing))

if len(missing) == 0:
    print("All AMFI codes exist in nav_history.csv")
else:
    print("Missing:", missing)