import sqlite3
 
def view_database():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("\nDatabase Contents:")
        for row in rows:
            print(row)
    else:
        print("Database is empty.")
 
if __name__ == "__main__":
    view_database()