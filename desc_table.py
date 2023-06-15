import psycopg2
conn = psycopg2.connect(host="localhost", port=3307, user="postgres", password="master", dbname="postgres")


cur = conn.cursor()
cur.execute("Select * from information_schema.columns where table_name='company';")
rows = cur.fetchall()

print("table_catalog | table_schema | table_name | column_name | ordinal_position | column_default | is_nullable | data_type | character_maximum_length | character_octet_length | numeric_precision | numeric_precision_radix | numeric_scale | datetime_precision | interval_type | interval_precision | character_set_catalog | character_set_schema | character_set_name | collation_catalog | collation_schema | collation_name | domain_catalog | domain_schema | domain_name | udt_catalog | udt_schema | udt_name | scope_catalog | scope_schema | scope_name | maximum_cardinality | dtd_identifier | is_self_referencing | is_identity | identity_generation | identity_start | identity_increment | identity_maximum | identity_minimum | identity_cycle | is_generated | generation_expression | is_updatable")
print(rows)

for row in rows:
    print(row[3], row[7], row[8])

conn.close()
