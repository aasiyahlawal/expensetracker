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
connection.close()

try:
    with sqlite3.connect("expenses.db") as conn:
        print("Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
        #pass
except sqlite3.OperationalError as error:
    print("Failed to open a database", error)    