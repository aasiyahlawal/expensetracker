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

conn = sqlite3.connect(expenses) #not yet created expenses database
conn.close()

try:
    with sqlite3.connect(expenses.db) as conn:
        pass
except sqlite3.OperationalError as error:
    print("Failed to open a database", error)    