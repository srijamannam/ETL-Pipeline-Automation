import configparser
import psycopg2
import csv

config = configparser.ConfigParser()
config.read('config.ini')

db_par = {
    'host': config['database']['hostname'],
    'database': config['database']['database'],
    'user': config['database']['username'],
    'password':config['database']['pwd']
}

csv_file = 'shoes_db.csv'
table_name = 'shoes_db'

# Create a connection
conn = psycopg2.connect(**db_par)
cur = conn.cursor()

try:
    with open(csv_file, 'r') as f:
        header = next(csv.reader(f))
        create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(f'{column} text' for column in header)})"
        cur.execute(create_table_sql)
        conn.commit()

    with open(csv_file, 'r') as f:
        copy_sql = f"COPY {table_name} FROM stdin WITH CSV HEADER"
        cur.copy_expert(sql=copy_sql, file=f)
        conn.commit()

except Exception as e:
    print(f"Error: {str(e)}")


finally:
    # Close the cursor and the database connection, even in case of an error
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()