import mariadb
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'port': 3306,
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': 'broadwaydb'
}


def get_connection():
    try:
        conn = mariadb.connect(**db_config)
        return conn
    except Exception as e:
        print(f"Unable to connect to Database. {e}")
