# validation functions
def get_valid_age():
    age = int(input("Enter Your Age: "))
    while age <= 0:
        print("Age must be greater than 0")
        age = int(input("Enter Your Age: "))
    return age

def get_valid_marks():
    marks = int(input("Enter Your Marks: "))
    while marks < 0 or marks > 100:
        print("Marks should be between 0 and 100")
        marks = int(input("Enter Your Marks: "))
    return marks

# main features
def Add_Student(students):
    student_id = input("Enter Student ID: ").strip().lower()
    if student_id in students:
        print("-"*10,"Student already existed","-"*10)
    else:
        name = input("Enter Your Name: ").title()
        age = get_valid_age()
        marks = get_valid_marks()
        students[student_id] = {
            "name":name,
            "age":age,
            "marks":marks
        }
        print("-"*10, "Student Added Sucessfully!", "-"*10)
    return students

def Delete_Student(students):
    student_id = input("Enter Student ID: ").strip().lower()
    if student_id in students:
        del students[student_id]
        print("-"*10, "Student Deleted Sucessfully", "-"*10)
    else:
        print("-"*10, "Student Not Found", "-"*10)
    return students

def Update_Student(students):
    student_id = input("Enter Student ID to Update: ").strip().lower()
    if student_id in students:
        print("1. Update Name")
        print("2. Update Age")
        print("3. Update Marks")
        updated_choice = int(input("Enter What to Update: "))
        if updated_choice == 1:
            new_name = input("Enter Student Name: ").title()
            students[student_id]["name"] = new_name
            print("-"*10, "Name Updated Sucessfully", "-"*10)
        elif updated_choice == 2:
            new_age = get_valid_age()
            students[student_id]["age"] = new_age
            print("-"*10, "Age Updated Sucessfully", "-"*10)
        elif updated_choice == 3:
            new_marks = get_valid_marks()
            students[student_id]["marks"] = new_marks
            print("-"*10, "Marks Updated Sucessfully", "-"*10)
        else:
            print("-"*10, "Invalid Choice", "-"*10)
    else:
        print("-"*10, "Student Not Found", "-"*10)
    return students

def View_Student():
    if not students:
        print("-"*10, "No Student Found", "-"*10)
    else:
        for k,v in students.items():
            print("ID: ",k)
            print("Name: ",v["name"])
            print("Age: ",v["age"])
            print("Marks: ",v["marks"])
            print("-"*20)

def Find_Topper():
    if not students:
        print("-"*10, "No Students Found", "-"*10)
    else:
        top = float ('-inf')
        top_id = ""
        for k,v in students.items():
            if v['marks'] > top:
                top = v['marks']
                top_id = k
        print("Student Details: ")
        print("Student ID: ",top_id)
        print("Student Name: ",students[top_id]['name'])
        print("Student Marks: ",students[top_id]['marks'])
        print("-"*20)

# menu loop
students = {}  # key = student_id, value = {name, age, marks}

while True:
    print("1. Add Student")
    print("2. Delete Student")
    print("3. Update Student")
    print("4. View Students")
    print("5. Find Topper")
    print("6. Exit")

    choice = input("Enter Your Choice: ")
    if not choice.isdigit():
        print("-"*10, "Enter a number only", "-"*10)
        continue
    choice = int(choice)

    if choice == 1:
        students = Add_Student(students)
    elif choice == 2:
        students = Delete_Student(students)
    elif choice == 3:
        students = Update_Student(students)
    elif choice == 4:
        View_Student()
    elif choice == 5:
        Find_Topper()
    elif choice == 6:
        break
    else:
        print("-"*10, "Invalid Choice", "-"*10)
        


