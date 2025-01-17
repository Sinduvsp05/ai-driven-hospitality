import MySQLdb

# Connect to the database
db = MySQLdb.connect(
    host='localhost',
    user='root',        # MySQL username
    password='root',        # MySQL password (default is empty for XAMPP)
    database='mydemo'   # Name of the database
)

# Create a cursor object to interact with the database
cursor = db.cursor()

# Input from the user (Normally this would be provided via input prompts)
id = input("Enter the ID: ")
name = input("Enter Name: ")
pref = input("Enter the Preference: ")

# Check if the ID exists in the database
cursor.execute("SELECT * FROM student2 WHERE std_id = %s", (id,))
is_exists = cursor.fetchone()

# If the student exists, update the preference, else insert a new record
if is_exists:
    cursor.execute("SELECT Preferance FROM student2 WHERE std_id = %s", (id,))
    current_prefs = cursor.fetchone()[0]
    updated_prefs = current_prefs + ', ' + pref
    cursor.execute("UPDATE student2 SET Preferance = %s WHERE std_id = %s", (updated_prefs, id))
    db.commit()
    print("Preferences updated.")
else:
    cursor.execute("INSERT INTO student2 (std_id, name, Preferance) VALUES (%s, %s, %s)", (id, name, pref))
    db.commit()
    print("New student added.")

# Close the database connection
cursor.close()
db.close()
