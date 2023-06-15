import psycopg2

conn = psycopg2.connect(host="localhost", port="3307",
                        user="postgres", password="master", database="postgres")

cursor = conn.cursor()

cursor.execute(
    '''INSERT INTO COMPANY VALUES (1, 'Kavi', 18, 'Salem, TN', 100000), (2, 'Master', 24, 'NYC, TN', 120000) RETURNING *''')

# Returning used to return the inserted values.
# Also use RETURNING COL1, COL2

rows = cursor.fetchall()
for i in rows:
    print(i)

conn.commit()
conn.close()
