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
        #print("Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        pass
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

#cursor.execute("""
 #   INSERT INTO Expenses (description, amount, category, date)
  #  VALUES ("Breakfast", 6.30, "Food", "05/09/2026");

# """)

connection.commit()

# Add expenses function
print("Hello welcome to your personal expenses tracker")

def add_expenses():
    description = input("Please enter a brief description of your expense: ")
    amount = float(input(f"Please enter the cost of your {description}: "))
    category = input("Please enter the category of your expense 'e.g Food, Entertainment, Transport etc': ")
    date = input("Please enter the date of your expense in DD/MM/YYYY format: ")

    cursor.execute("""
        INSERT INTO Expenses (description, amount, category, date)
        VALUES (?, ?, ?, ?); 

    """,(description, amount, category, date)) #placeholders used due to sql and python having same variable names

    connection.commit()

def allexpenses():
    cursor.execute("SELECT * FROM Expenses")
    expenses = cursor.fetchall()
    print(expenses)

def view_expenses():
    search_expense = input("Please enter the expense you want to search: ") 
    cursor.execute("SELECT * FROM Expenses WHERE description = ?",(search_expense,))
    expenses = cursor.fetchall()
    print(expenses)

def get_total():
    cursor.execute("SELECT SUM(amount) FROM Expenses")    
    total = cursor.fetchall()
    total_price = total[0][0]
    print(f"Total price of all expenses is {total_price}")
    
#Run
add_expenses()
allexpenses()
view_expenses()
#allexpenses()
get_total()

connection.close()

