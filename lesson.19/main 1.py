import psycopg


print(psycopg.__version__)


connection = psycopg.connect(
    host="localhost",
    port="5432",
    dbname="shop",
    user="postgres",
    password="postgres"
)

print(connection)

connection.close()
