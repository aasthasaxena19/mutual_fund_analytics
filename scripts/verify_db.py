import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

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

print("\n===== DATABASE ROW COUNTS =====\n")

for table in tables:

    try:

        query = f"""
        SELECT COUNT(*) as rows
        FROM {table}
        """

        count = pd.read_sql(
            query,
            conn
        )

        print(
            f"{table}: {count['rows'][0]} rows"
        )

    except Exception as e:

        print(
            f"{table}: NOT FOUND"
        )

conn.close()