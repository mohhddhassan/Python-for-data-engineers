import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="mydb",
        user="myuser",
        password="mypass"
    )

    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()

except Exception as e:
    print("Error connecting to DB:", e)
