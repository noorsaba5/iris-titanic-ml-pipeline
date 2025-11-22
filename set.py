import psycopg2
from tabulate import tabulate

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

# Get column names
col_names = [desc[0] for desc in cursor.description]

# Print the table
print(tabulate(rows, headers=col_names, tablefmt="psql"))

# Close the connection
conn.close()