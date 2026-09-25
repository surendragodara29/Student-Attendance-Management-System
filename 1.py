students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student Already Exist! ")
        return

    name = input("Enter Student name: ")
    branch = input("Enter Student Branch: ")

    students[roll] = {
        "name" : name,
        "branch" : branch
    }
    print("Student Added Sucessfully!")

def view_students():
    if not students:
        print("No Student Found! ")
        return

    print("\n ------Student List------")

    for roll, student in students.items():
        print("Roll Number: ", roll)
        print("name: ", student["name"])
        print("Brench: ", student["branch"])
        print("---------------------------")

def mark_attendence():
    if not students:
        print("No Student Found! ")
        return

    roll = input("Enter Roll Number of Student: ")
    if roll not in students:
        print("No Student Found! ")
        return

    print("1. Present")
    print("2. Absent")

    choise = input("Enter your Choise: ")

    if choise == "1":
        students[roll]["Present"] += 1
        print("Attendence is marked as Present! ")

    elif choise == "2":
        students[roll]["Absent"] += 1
        print("Attendence is marked as Absent! ")

    else:
        print("Invalid Choise! ")

def View_Attendence():
    if not students:
        print("No Student Found! ")
        return

    print("\n--------Attendence-------")
    for roll, student in students.items():
        total = student["Present"] + student["Absent"]

        print("Roll Number: ", roll)
        print("Name: ", student["name"])
        print("Branch: ", student["branch"])
        print("Present: ", student["Present"])
        print("Absent: ", student["Absent"])
        print("Total Days: ", total)
        print("--------------------------------------")

def search_student():
    roll = input("Enter Student Roll Number: ")

    if roll in students:
        student = students[roll]

        print("\n Student Found ! ")
        print("Roll Number: ", roll)
        print("Name: ", student["name"])
        print("Branch: ", student["branch"])
        print("Present: ", student["Present"])
        print("Absent: ", student["Absent"])

    else:
        print("Student Not Found!")

def Attendence_Percentage():
    roll = input("Enter Roll Number of The Student: ")

    if roll not in students:
        print("Student Not Found!")
        return
    student = students[roll]
    total = student["Present"] + student["Absent"]

    if total == 0:
        print("No Attendence Found! ")

    else:
        percentage = (student["Present"]/ total)* 100
        print("Attendance Percentage:", round(percentage, 2), "%")

def delete_student():
    roll = input("Enter Roll Number to delete: ")

    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def Make_Change():
    print("1. add_student")
    print("2. view_students")
    print("3. mark_attendence")
    print("4. View_Attendence")
    print("5. search_student")
    print("6. Attendence_Percentage")

    choise = input("Enter your Choise: ")
    if choise == "1":
        add_student()

    elif choise == "2":
        view_students()

    elif choise == "3":
        mark_attendence()

    elif choise == "4":
        View_Attendence()

    elif choise == "5":
        search_student()

    elif choise == "6":
        Attendence_Percentage()
        

    else:
        print("You Do Not Have Other Authority!")

    Make_Change()

Make_Change()