import psycopg2

conn = psycopg2.connect(host="localhost", port="3307", database="postgres", user="postgres", password="master")
cursor = conn.cursor()

cursor.execute("select version()")
data = cursor.fetchone()
print("Connection Established:", data)

conn.close()