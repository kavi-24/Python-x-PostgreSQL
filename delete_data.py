import psycopg2

conn = psycopg2.connect(host="localhost", port="3307", user="postgres", password="master", database="postgres")

cursor = conn.cursor()

cursor.execute("DELETE FROM COMPANY;") # Delete the data inside
cursor.execute('''DROP TABLE COMPANY;''') # Deletet the whole table

conn.commit()
conn.close()
