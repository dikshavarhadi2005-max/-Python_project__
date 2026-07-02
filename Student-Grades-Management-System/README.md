# 🎓 Student Grades Management System

A simple **Python Console-Based Student Grades Management System** that allows users to manage student records using a dictionary. The application provides a menu-driven interface to perform basic CRUD (Create, Read, Update, Delete) operations on student grades.

---

## 📌 Features

- ➕ Add a new student with grade
- ✏️ Update an existing student's grade
- ❌ Delete a student record
- 📋 View all student records
- 🚪 Exit the application

---

## 🛠️ Technologies Used

- Python 3
- Dictionary Data Structure
- Functions
- Loops
- Conditional Statements

---

## 📂 Project Structure

```
Student-Grades-Management-System/
│
├── student_grades.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed on your computer

### Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/Student-Grades-Management-System.git
```

2. Navigate to the project folder

```bash
cd Student-Grades-Management-System
```

3. Run the program

```bash
python student_grades.py
```

---

## 📖 Menu

```
Student Grades Management System

1. Add Student
2. Update Student
3. Delete Student
4. View Student
5. Exit
```

---

## 💻 Example Output

### Add Student

```
Enter your choice = 1
Enter Student name = Diksha
Enter student grade = 100

Added Diksha with a 100
```

### View Students

```
Diksha : 100
```

### Update Student

```
Enter Student name = Diksha
Enter Student grade = 95

Diksha with marks are updated 95
```

### Delete Student

```
Enter Student name = Diksha

Diksha has been successfully deleted
```

---

## 🧠 Functions Used

### `add_student(name, grade)`

Adds a new student and stores their grade in the dictionary.

### `update_student(name, grade)`

Updates the grade of an existing student.

### `delete_student(name)`

Deletes a student's record from the dictionary.

### `display_all_student()`

Displays all students along with their grades.

### `main()`

Controls the menu-driven application and handles user interaction.

---

## 📊 Data Structure Used

The project uses a **Python Dictionary**.

Example:

```python
student_grades = {
    "Diksha": 100,
    "Rahul": 95,
    "Priya": 88
}
```

- **Key** → Student Name
- **Value** → Student Grade

---

## ✨ Future Enhancements

- 🔍 Search student by name
- 💾 Save records in a file or database
- 📈 Calculate average grade
- 🏆 Display highest and lowest grades
- ✅ Add input validation

---

## 📚 Learning Outcomes

This project helps in understanding:

- Python Dictionaries
- Functions
- Loops
- Conditional Statements
- User Input Handling
- CRUD Operations
- Menu-Driven Programming

---

## 👩‍💻 Author

**Diksha Varhadi**

Python Mini Project

---

