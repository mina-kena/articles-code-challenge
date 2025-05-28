cursor.executescript()

cursor.executescript(schema_sql)
conn.commit()
conn.close()

print("Database initialized successfully!")