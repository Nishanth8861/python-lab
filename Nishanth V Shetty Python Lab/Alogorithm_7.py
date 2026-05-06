def add_student(records):
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    records[name] = marks
    print("Student added!\n")

def display_students(records):
    if not records:
        print("No records found\n")
        return
    for name, marks in records.items():
        print(f"{name} -> {marks}")
    print()

def find_topper(records):
    if records:
        topper = max(records, key=records.get)
        print(f"Topper: {topper} with {records[topper]} marks\n")

records = {}

while True:
    print("1.Add  2.Display  3.Topper  4.Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        add_student(records)
    elif choice == '2':
        display_students(records)
    elif choice == '3':
        find_topper(records)
    elif choice == '4':
        break
    else:
        print("Invalid choice\n")
