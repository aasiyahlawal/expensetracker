import sqlite3

#Structure
#Program starts
#Connect to database
#Make sure database/table exists
#Display menu
#User chooses an option
#Perform the chosen action
#Return to menu
#Exit

connection = sqlite3.connect("expenses.db") #not yet created expenses database
cursor = connection.cursor()
#connection.close()

try:
    with sqlite3.connect("expenses.db") as conn:
        print("Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        #pass
except sqlite3.OperationalError as error:
    print("Failed to open a database", error)    


cursor.execute("""
 CREATE TABLE IF NOT EXISTS Expenses (
    id INTEGER PRIMARY KEY,
    description TEXT,
    amount REAL,
    category TEXT NOT NULL,
    date TEXT
    )
""")

connection.commit()

cursor.execute("""
    INSERT INTO Expenses (description, amount, category, date)
    VALUES ("Breakfast", 6.30, "Food", "05/09/2026");

 """)

connection.commit()

cursor.execute("SELECT * FROM Expenses")

expenses = cursor.fetchall()

print(expenses)

connection.close()

