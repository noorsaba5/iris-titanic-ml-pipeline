import sqlite3

def connect_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL,
                      gender TEXT NOT NULL)''')
    conn.commit()
    return conn, cursor

def add_user(cursor, conn):
    name = input("Enter user name: ").strip()
    age = input("Enter user age: ").strip()
    
    # Ensure age is a number
    if not age.isdigit():
        print("Error: Age must be a number.\n")
        return
    
    gender = input("Enter user gender (Male, Female, Gender Fluid, Other): ").strip()
    
    try:
        cursor.execute("INSERT INTO users (name, age, gender) VALUES (?, ?, ?)", (name, int(age), gender))
        conn.commit()
        print(f"User {name} added successfully.\n")
    except sqlite3.IntegrityError:
        print("Error: Entry already exists in the database.\n")

def view_users(cursor):
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    if not rows:
        print("No users found.\n")
        return
    
    print("\nID | Name | Age | Gender")
    print("-" * 30)
    for row in rows:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()

def remove_user(cursor, conn):
    user_id = input("Enter the ID of the user to remove: ").strip()
    
    # Ensure the ID is a number
    if not user_id.isdigit():
        print("Error: User ID must be a number.\n")
        return
    
    cursor.execute("DELETE FROM users WHERE id = ?", (int(user_id),))
    conn.commit()
    
    if cursor.rowcount == 0:
        print("Error: No user found with the given ID.\n")
    else:
        print("User removed successfully!\n")

def menu():
    conn, cursor = connect_db()  # Single connection instance
    while True:
        print("Menu:")
        print("1. Add User")
        print("2. View Users")
        print("3. Remove User")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            add_user(cursor, conn)
        elif choice == "2":
            view_users(cursor)  # Uses the same connection
        elif choice == "3":
            remove_user(cursor, conn)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.\n")
    
    conn.close()  # Close connection only when exiting

if __name__ == "__main__":
    menu()
