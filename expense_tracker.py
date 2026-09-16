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

#connection.commit()

# Add expenses function
print("Hello welcome to your personal expenses tracker")

#Main
def main_menu():
    print("Main Menu")
    print("-------------------")
    print("1. Add Expense")
    print("2. Search for an expense")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Show total")

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

def update_expense():
    allexpenses()
    update_expense = input("Please enter the id of the expense you want to update: ")
    updated_description = input("Please enter an updated description of your expense: ")
    updated_amount = float(input(f"Please enter the cost of your {updated_description}: "))
    updated_category = input("Please update the category of your expense: ")
    updated_date = input("Please enter the date of your expense in DD/MM/YYYY format: ")

    cursor.execute("""
            UPDATE Expenses
            SET description = ?, amount = ?, category = ?, date = ?
            WHERE id = ?; 
    
        """,(updated_description, updated_amount, updated_category, updated_date, update_expense))

    connection.commit()
    allexpenses() #So user can see the expenses and the updated expense

def delete_expense():
    pass
    del_expense = input("Please enter the id of the expense you want to delete: ")
    cursor.execute("""
            DELETE FROM Expenses
            WHERE id = ?;
    """, (del_expense))
    connection.commit()
    allexpenses() #Testing

#Run
main_menu()
#add_expenses()
#main_menu()
#allexpenses()
#delete_expense()
#view_expenses()
#update_expense()
#get_total()

connection.close()

