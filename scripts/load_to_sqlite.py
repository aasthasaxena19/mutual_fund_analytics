from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "sqlite:///bluestock_mf.db"
)

df = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

df.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)
