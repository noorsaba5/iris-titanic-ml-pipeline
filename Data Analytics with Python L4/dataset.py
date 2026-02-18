import mysql.connector

# Connect to MySQL Server
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password"
)
cursor = conn.cursor()

# Create a new database
cursor.execute("CREATE DATABASE IF NOT EXISTS movie_db")
cursor.execute("USE movie_db")

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    studio VARCHAR(100),
    release_year INT
);
""")

# Commit and close
conn.commit()
conn.close()
print("MySQL Database and table created successfully!")