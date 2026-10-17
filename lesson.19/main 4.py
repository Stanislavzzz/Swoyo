import psycopg


print(psycopg.__version__)


with psycopg.connect(
    host="localhost",
    port="5432",
    dbname="shop",
    user="postgres",
    password="postgres"
) as connection:

    with connection.cursor() as cursor:

        cursor.execute(
            """
            SELECT u.name AS NAME_USER, o.amount
            FROM users u
            INNER JOIN orders o
            ON u.id = o.user_id
            WHERE o.status = 'paid';
            """
        )

        rows = cursor.fetchall()

        for row in rows:
            print(row[0], row[1])
