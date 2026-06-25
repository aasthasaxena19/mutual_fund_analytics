import sqlite3

conn = sqlite3.connect(
    "bluestock_mf.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM dim_fund"
)

print(cursor.fetchone())