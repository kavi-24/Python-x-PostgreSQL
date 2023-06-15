import psycopg2

connection = psycopg2.connect(user="postgres",
                              password="master",
                              host="127.0.0.1",
                              port="3307",
                              database="postgres")

cursor = connection.cursor()
insert_query = """ INSERT INTO mobile (ID, MODEL, PRICE) VALUES (1, 'Iphone12', 110000), (2, 'Redmi13', 11000)"""
cursor.execute(insert_query)
connection.commit()
print("1 Record inserted successfully")
cursor.execute("SELECT * from mobile")
record = cursor.fetchall()
print("Result ", record)

update_query = """Update mobile set price = 150000 where id = 1"""
cursor.execute(update_query)
connection.commit()
count = cursor.rowcount
print(count, "Record updated successfully ")
cursor.execute("SELECT * from mobile")
print("Result ", cursor.fetchall())

delete_query = """Delete from mobile where id = 1"""
cursor.execute(delete_query)
connection.commit()
count = cursor.rowcount
print(count, "Record deleted successfully ")
cursor.execute("SELECT * from mobile")
print("Result ", cursor.fetchall())

cursor.close()
connection.close()
print("PostgreSQL connection is closed")
