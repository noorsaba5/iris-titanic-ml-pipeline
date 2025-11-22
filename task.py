import sqlite3

def connect_db():
    conn = sqlite3.connect("crud_system.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS entries (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT NOT NULL,
                      age INTEGER NOT NULL)''')
    conn.commit()
    return conn, cursor

def add_entry(cursor, conn):
    name = input("Enter name: ")
    age = input("Enter age: ")
    cursor.execute("INSERT INTO entries (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Entry added successfully!\n")

def view_entries(cursor):
    cursor.execute("SELECT * FROM entries")
    rows = cursor.fetchall()
    if rows:
        print("ID | Name | Age")
        print("-" * 20)
        for row in rows:
            print(f"{row[0]} | {row[1]} | {row[2]}")
    else:
        print("No entries found.")
    print()

def remove_entry(cursor, conn):
    entry_id = input("Enter the ID of the entry to remove: ")
    cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
    conn.commit()
    print("Entry removed successfully!\n")

def menu():
    conn, cursor = connect_db()
    while True:
        print("Menu:")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Remove Entry")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_entry(cursor, conn)
        elif choice == "2":
            view_entries(cursor)
        elif choice == "3":
            remove_entry(cursor, conn)
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.\n")
    conn.close()

if __name__ == "__main__":
    menu()
