# step 0 - import sqlite3
import sqlite3

# step 1 - connect to the database
# Triple check spelling of database filename
connection = sqlite3.connect("rpg_db.sqlite3")

# step 2 - Make the "cursor"
cursor = connection.cursor()

# step 3 - write a query
query = "SELECT character_id, name FROM charactercreator_character;"

# step 4 - execute the query on the cursor and fetch the results
#  "pulling the results" from the cursor
results = cursor.execute(query).fetchall()

if __name__ == "__main__":
    print(results[:5])
