from sqlalchemy import create_engine
import pandas as pd

# SQLAlchemy engine
engine = create_engine("postgresql://myuser:mypass@localhost/mydb")

# Read into DataFrame
try:
    df = pd.read_sql("SELECT * FROM users", con=engine)
    print(df.head())
except Exception as e:
    print("SQLAlchemy Error:", e)
