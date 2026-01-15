import mariadb

db_config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'test1',
    'password': 'pass1',
    'database': 'broadwaydb'
}

def get_connection():
    try:
        conn = mariadb.connect(**db_config)
        return conn
    except Exception as e:
        print(f"Unable to connect to Database. {e}")