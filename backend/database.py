import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="diagnosai",
    user="postgres",
    password="123456"
)

print("Connected to PostgreSQL!")