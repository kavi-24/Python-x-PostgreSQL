import psycopg2

conn = psycopg2.connect(host="localhost", port="3307",
                        user="postgres", password="master", database="postgres")
cursor = conn.cursor()

sql = """select * from information_schema.tables where table_schema='public';"""
cursor.execute(sql)
rows = cursor.fetchall()
print("table_catalog | table_schema | table_name | table_type | self_referencing_column_name | reference_generation | user_defined_type_catalog | user_defined_type_schema | user_defined_type_name | is_insertable_into | is_typed | commit_action")
for row in rows: print(row)

print("DATABASE | PUBLIC? | TABLE NAME") 
for row in rows:
    print(row[0] + " | " + row[1] + " | " + row[2])

conn.close()
