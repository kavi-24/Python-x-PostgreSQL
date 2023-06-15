import datetime

import psycopg2

conn = psycopg2.connect(user="postgres",
                              password="master",
                              host="127.0.0.1",
                              port="3307",
                              database="postgres")

cursor = conn.cursor()
create_table = '''CREATE TABLE item ( 
	item_id serial NOT NULL PRIMARY KEY, 
	item_name VARCHAR (100) NOT NULL, 
	purchase_time timestamp NOT NULL,
	price INTEGER NOT NULL
);'''
cursor.execute(create_table)

item_purchase_time = datetime.datetime.now()

item_tuple = (12, "Keyboard", item_purchase_time, 150)
insert_query = """INSERT INTO item (item_Id, item_name, purchase_time, price) VALUES (%s, %s, %s, %s)"""
cursor.execute(insert_query, item_tuple)

conn.commit()
print("1 item inserted successfully")

cursor.execute("SELECT purchase_time from item where item_id = 12")
purchase_datetime = cursor.fetchone()

print("Item Purchase date is  ", purchase_datetime[0].date())
print("Item Purchase time is  ", purchase_datetime[0].time())

cursor.close()
conn.close()
print("PostgreSQL connection is closed")
