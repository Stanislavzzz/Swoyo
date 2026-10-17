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

cursor.execute(
    """
    SELECT u.name AS NAME_USER, o.amount
    FROM users u
    INNER JOIN orders o
    ON u.id = o.user_id
    WHERE o.status = 'paid';
    """
)

#
rows = cursor.fetchall()
print(rows)
print(type(rows))


for row in rows:
    print(row[0], row[1])

cursor.close()

connection.close()
