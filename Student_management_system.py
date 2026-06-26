# ==========================================
# STUDENT MANAGEMENT SYSTEM
# CREATED BY SUMIT GOREGAONKAR
# ==========================================

students = {
    1011: {
        "name": "Sumit Goregaonkar",
        "marks": [95, 98, 94, 96, 97]
    },
    1022: {
        "name": "Aarav Mishra",
        "marks": [75, 78, 80, 72, 77]
    },
    1033: {
        "name": "Riya Sharma",
        "marks": [68, 72, 70, 65, 69]
    },
    1044: {
        "name": "Aditya Singh",
        "marks": [73, 70, 75, 71, 74]
    },
    1055: {
        "name": "Ananya Patel",
        "marks": [62, 66, 64, 68, 65]
    },
    1066: {
        "name": "Karan Verma",
        "marks": [91, 92, 89, 90, 93]
    }
}

# ==========================================
# FUNCTIONS
# ==========================================

def calculate_percentage(marks):
    return sum(marks) / len(marks)

def calculate_grade(percentage):
    if percentage >= 90:
        return "O"
    elif percentage >= 80:
        return "A+"
    elif percentage >= 70:
        return "A"
    elif percentage >= 60:
        return "B+"
    elif percentage >= 40:
        return "B"
    else:
        return "F"

def add_student():
    try:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Student already exists!")
            return

        name = input("Enter Student Name: ")

        marks = []

        for i in range(1, 6):
            mark = float(input(f"Enter Marks for Subject {i}: "))
            marks.append(mark)

        students[roll] = {
            "name": name,
            "marks": marks
        }

        print("Student Added Successfully!")

    except:
        print("Invalid Input!")

def view_students():

    if not students:
        print("No Student Records Found!")
        return

    print("\n")
    print("-" * 80)
    print("ROLL\tNAME\t\t\tPERCENTAGE\tGRADE")
    print("-" * 80)

    for roll, data in students.items():

        percentage = calculate_percentage(data["marks"])
        grade = calculate_grade(percentage)

        print(
            f"{roll}\t{data['name']}\t\t{round(percentage,2)}%\t\t{grade}"
        )

def search_student():

    roll = int(input("Enter Roll Number: "))

    if roll in students:

        data = students[roll]

        percentage = calculate_percentage(data["marks"])
        grade = calculate_grade(percentage)

        print("\nStudent Found")
        print("Roll Number :", roll)
        print("Name :", data["name"])
        print("Marks :", data["marks"])
        print("Percentage :", round(percentage, 2))
        print("Grade :", grade)

    else:
        print("Student Not Found!")

def update_student():

    roll = int(input("Enter Roll Number to Update: "))

    if roll not in students:
        print("Student Not Found!")
        return

    name = input("Enter New Name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter New Marks Subject {i}: "))
        marks.append(mark)

    students[roll]["name"] = name
    students[roll]["marks"] = marks

    print("Record Updated Successfully!")

def delete_student():

    roll = int(input("Enter Roll Number to Delete: "))

    if roll in students:
        del students[roll]
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found!")

def class_report():

    if not students:
        print("No Records Found!")
        return

    percentages = []

    pass_count = 0
    fail_count = 0

    topper_name = ""
    topper_percentage = 0

    for roll, data in students.items():

        percentage = calculate_percentage(data["marks"])

        percentages.append(percentage)

        if percentage >= 40:
            pass_count += 1
        else:
            fail_count += 1

        if percentage > topper_percentage:
            topper_percentage = percentage
            topper_name = data["name"]

    average = sum(percentages) / len(percentages)

    print("\n===== CLASS REPORT =====")
    print("Total Students :", len(students))
    print("Class Average :", round(average, 2))
    print("Pass Count :", pass_count)
    print("Fail Count :", fail_count)
    print("Topper :", topper_name)
    print("Topper Percentage :", round(topper_percentage, 2))

def rank_list():

    ranking = []

    for roll, data in students.items():

        percentage = calculate_percentage(data["marks"])

        ranking.append(
            (percentage, roll, data["name"])
        )

    ranking.sort(reverse=True)

    print("\n===== RANK LIST =====")

    rank = 1

    for percentage, roll, name in ranking:

        print(
            f"Rank {rank} : {name} ({roll}) - {round(percentage,2)}%"
        )

        rank += 1

def show_menu():

    print("\n")
    print("========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Class Report")
    print("7. Rank List")
    print("8. Exit")

# ==========================================
# MAIN PROGRAM
# ==========================================

while True:

    show_menu()

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        class_report()

    elif choice == "7":
        rank_list()

    elif choice == "8":
        print("Thank You!")
        break

    else:
        print("Invalid Choice! Try Again.")