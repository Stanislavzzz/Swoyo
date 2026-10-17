import psycopg


print(psycopg.__version__)


connection = psycopg.connect(
    host="localhost",
    port="5432",
    dbname="shop",
    user="postgres",
    password="postgres"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM users")

#
rows = cursor.fetchall()
print(rows)
print(type(rows))

print(rows[1])
print(rows[3])

# row = cursor.fetchone()
# print(row)
# print(type(row))

cursor.close()

connection.close()
