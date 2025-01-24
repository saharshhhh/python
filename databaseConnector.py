import mysql.connector as c
mydb = c.connect(
    host="localhost",  # database from the same system
    user="root",
    password="root",
    database="cvr"
)
mycursor = mydb.cursor()



entries = [
    (1230, 'Ananya'),
    (1231, 'Mohan'),
    (1222, 'Priya'),
    (1223, 'Vikram'),
    (1234, 'Neha'),
    (1225, 'Mani')
]

for entry in entries:
    mycursor.execute("INSERT INTO faculty (id, name) VALUES (%s, %s)", entry)
mydb.commit()
def insert_faculty():
    name = input("Enter your name: ")
    id = input("Enter your id: ")
    mycursor.execute("INSERT INTO faculty (id, name) VALUES (%s, %s)", (id, name))
    mydb.commit()
    print("Record inserted successfully.")
def update_faculty():
    id = input("Enter the id of the faculty member you want to update: ")
    new_name = input("Enter the new name: ")
    mycursor.execute("UPDATE faculty SET name = %s WHERE id = %s", (new_name, id))
    mydb.commit()
    print("Record updated successfully.")
def delete_faculty():
    id = input("Enter the id of the faculty member you want to delete: ")
    mycursor.execute("DELETE FROM faculty WHERE id = %s", (id,))
    mydb.commit()
    print("Record deleted successfully.")
def display_records():
    mycursor.execute("SELECT * FROM faculty order by name")
    records = mycursor.fetchall()
    for record in records:
        print(record)
def selectedRecords():
    mycursor.execute("Select * from faculty as f Where f.id between 1220 and 1230")
    records= mycursor.fetchall()
    for record in records:
        print(record)
def startsWithM():
    mycursor.execute("SELECT * from faculty as f where f.name like 'm%'")
    records = mycursor.fetchall()
    for record in records:
        print(record)
while True:
    print("\nOptions:")
    print("1. Insert Faculty")
    print("2. Update Faculty")
    print("3. Delete Faculty")
    print("4. Display All Faculty based on asc order of names")
    print("5. Display All faculty whose id is between 1220 and 1230")
    print("6. Display All faculty whose name starts with m")
    print("7. Exit")

    choice = input("Choose an option : ")

    if choice == '1':
        insert_faculty()
    elif choice == '2':
        update_faculty()
    elif choice == '3':
        delete_faculty()
    elif choice == '4':
        display_records()
    elif choice == '5':
        selectedRecords()
    elif choice == '6':
        startsWithM()
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")