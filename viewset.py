import psycopg2

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="movie_db",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

# Fetch data from the movies table
cursor.execute("SELECT * FROM movies")
rows = cursor.fetchall()

# Print the data
for row in rows:
    print(row)

# Close the connection
conn.close()