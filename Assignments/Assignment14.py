df = spark.table('skit.raw')

table_defs = {}

for row in df.collect():
    table_name = row['Name']
    column_def = f"{row['Column']} {row['Datatype']}"

    if table_name in table_defs:
        table_defs[table_name].append(column_def)
    else:
        table_defs[table_name] = [column_def]
    display(table_defs)

for table_name, columns in table_defs.items():
    column_list = ", ".join(columns)
    create_sql = f"CREATE TABLE {table_name} ({column_list})"

    spark.sql(f"DROP TABLE IF EXISTS {table_name}")
    spark.sql(create_sql)

    print(f"Table created: {table_name}")
spark.sql("SHOW TABLES").show()
