import psycopg2

conn = psycopg2.connect(host="localhost", port="3307", user="postgres", password="master", database="postgres")

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS COMPANY(
    ID INT PRIMARY KEY NOT NULL,
    NAME CHAR(25) NOT NULL,
    AGE INT NOT NULL,
    ADDRESS TEXT,
    SALARY REAL
)''')
print("Table Created")
conn.commit()
conn.close()