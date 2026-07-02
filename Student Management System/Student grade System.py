# Initialising dictionary
student_grades = {}

# add a new student
def add_student(name,grade):
    student_grades[name] = grade
    #[Diksha] = 100
    print(f"Added {name} with a {grade}")
    #  added Diksha with a 100

# Update a student
def update_student(name,grade):
    if name in student_grades:
        student_grades[name] = grade
        # diksha = 200
        print(f"{name} with marks are updated {grade}")

    else:
        print(f"{name} is not found!")

# Delete a student
def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has ben sucessfully deleted")
    else:
        print(f"{name} is not found!")
    

# view all student
def display_all_student():
    if student_grades:
        for name,grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No Students found/added")

def main():
    while True:
        print('\n Student Grades Management System')
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View Student")
        print("5. Exit")

        choice = int(input("Enter your choice = "))
        if choice == 1:
            name = input("Enter Student name =")
            grade = int(input("Enter student grade = "))
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter Student name =")
            grade = int(input("Enter Student grade = "))
            update_student(name,grade)

        elif choice == 3:
            name = input("Enter Student name =")
            delete_student(name) 

        elif choice == 4:
            display_all_student()

        elif choice == 5:
            print("closing the program...")
            break
        else:
            print("Invalid choice")
main()


