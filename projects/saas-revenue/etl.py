# ETL for SaaS Revenue and Churn Pipeline

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import os
# import sys
# import logging
# import time
# import requests
# import json
# import psycopg2
# import sqlalchemy
# from sqlalchemy import create_engine

# projects/saas-revenue/etl.py

# Issues with this code:
# 1. It assumes "data/telco_churn.csv" exists in the working directory—this may fail if the path is not correct.
# 2. It assumes .env file is set up and DATABASE_URL is present, does not raise an error or warning if not.
# 3. The code does not handle exceptions for IO (file/database) or for required columns missing in the CSV.
# 4. The transform assumes the "totalcharges" and "churn" columns always exist.
# 5. Using "if_exists='replace'" in to_sql can drop and recreate the whole table, which might not be wanted in prod, and may lose schema information.
# 6. There is no logging or proper error output.
# 7. Doesn't close DB connections or handle engine disposal.
# 8. The resulting customer table may have column types inferred incorrectly by pandas/sqlalchemy if not explicitly specified.
# 9. No parameterization/configuration—hardcoded values everywhere.

# A better version would include: error handling, config, pre-flight checks, comments, and safer handling.

import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import sys

# Load environment
load_dotenv()
db_url = os.getenv("DATABASE_URL")
if not db_url:
    sys.stderr.write("Error: DATABASE_URL not set in environment.\n")
    sys.exit(1)

engine = create_engine(db_url)

# Extract
data_path = "data/telco_churn.csv"
if not os.path.exists(data_path):
    sys.stderr.write(f"Error: CSV data file not found at {data_path}\n")
    sys.exit(1)

try:
    df = pd.read_csv(data_path)
except Exception as e:
    sys.stderr.write(f"Error reading CSV: {e}\n")
    sys.exit(1)

# Transform
required_cols = {"totalcharges", "churn"}
missing = required_cols - set(df.columns.str.lower().str.replace(" ", "_"))
if missing:
    sys.stderr.write(f"Error: Required columns missing from CSV: {missing}\n")
    sys.exit(1)

df.columns = df.columns.str.lower().str.replace(" ", "_")
df["totalcharges"] = pd.to_numeric(df["totalcharges"], errors="coerce")
df = df.dropna(subset=["totalcharges"])
if "churn" not in df.columns:
    sys.stderr.write("Error: 'churn' column missing after renaming.")
    sys.exit(1)
df["churned"] = df["churn"].map({"Yes": 1, "No": 0})

# Load
try:
    df.to_sql("customers", engine, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into table 'customers'")
except Exception as e:
    sys.stderr.write(f"Error loading data to SQL: {e}\n")
    sys.exit(1)
finally:
    engine.dispose()