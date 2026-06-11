from Employee import Employee

from Manager import Manager

from database_service import Database

def create_emp():

    first_name = user_input("First name: ")

    last_name = user_input("Last name: ")

    age = user_input("Age: ",type_to_cast=int)

    department = user_input("Department: ")

    salary = user_input("Salary: ",type_to_cast=float)

    managed_dept = user_input("Managed Department (leave blank if not a manager): ",allow_blank=True)

    if managed_dept == "":
        emp = Employee(None,first_name,last_name,age,department,salary)
    else:
        emp = Manager(None,first_name,last_name,age,department,salary,managed_dept)
    emp.save(Database.connection)

def transfere_emp():
    emp_id = user_input("Employee ID: ",type_to_cast=int)
    new_dept = user_input("New Department: ")
    emp = Employee.find(emp_id,Database.connection)
    if emp:
        if emp[6] == None:
            emp = Employee(emp[0],emp[1],emp[2],emp[3],emp[4],emp[5])
        else:
            emp = Manager(emp[0],emp[1],emp[2],emp[3],emp[4],emp[5],emp[6])
        emp.transfere(new_dept)
        emp.update(Database.connection)
    else:
        print("Employee not found")


def user_input(prompt,allow_blank = False,type_to_cast=str):
    value = ""
    while True:
        try:

            value = type_to_cast(input(prompt))

            if value == "" and not allow_blank:

                print(f"Value can't be empty!")
                continue

            return value

        except:

            print(f"Wrong expected type expected {type_to_cast.__name__} found {type(value).__name__}")

def print_all():
    employees = Employee.findAll(Database.connection)
    for emp in employees:
        print(emp)


def find_emp():
    emp_id = user_input("Employee ID: ",type_to_cast=int)
    emp = Employee.find(emp_id,Database.connection)
    if emp:
        print(emp)
    else:
        print("Employee not found")

options = {"c":["Create Employee",create_emp],"t":["Transfere Employee",transfere_emp],"a":['Print all',print_all],"f":["Find Employee",find_emp],"q":["Exit",exit]}

if __name__ == "__main__":

    db = Database.connect()

    if db == None:

        exit()

    while True:

        for opt in options.keys():

            print(f"{opt} => {options[opt][0]}")

        choice = input("Enter your choice: ")

        if choice in options:

            options[choice][1]()
        else:

            print("Invalid choice")

    db.close()