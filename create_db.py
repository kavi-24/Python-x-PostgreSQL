import psycopg2

conn = psycopg2.connect(host="localhost", port="3307", user="postgres", password="master")
cursor = conn.cursor()

cursor.execute(r"\c")

conn.close()
