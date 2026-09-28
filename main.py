from array import array

from login_module import login
from employee_module import Employee

from search_module import search_employee
from search_module import search_by_name
from search_module import department_employees

from payroll_module import payroll_summary
from payroll_module import highest_salary
from payroll_module import average_salary
from payroll_module import employee_count
from payroll_module import sort_by_salary

from validation_module import valid_name
from validation_module import valid_department
from validation_module import valid_salary
from validation_module import id_exists


# Login
print("================================")
print("      EMPLOYEE PAYROLL SYSTEM")
print("================================")

if login() == False:
    print("Access denied.")
    exit()


employees = []
salaries = array('f')


while True:

    print("\n================================")
    print("        PAYROLL MENU")
    print("================================")
    print("1. Add Employee")
    print("2. Display All Employees")
    print("3. Search by Employee ID")
    print("4. Search by Employee Name")
    print("5. Update Employee")
    print("6. Delete Employee")
    print("7. Generate Salary Slip")
    print("8. Department-wise Employees")
    print("9. Payroll Summary")
    print("10. Highest Salary Employee")
    print("11. Average Salary")
    print("12. Employee Count")
    print("13. Salary Grade")
    print("14. Sort Employees by Salary")
    print("15. Exit")
    print("================================")

    choice = input("Enter your choice: ").strip()

    # 1. ADD EMPLOYEE
    if choice == "1":

        while True:

            emp_id = input("Enter Employee ID: ").strip()

            if emp_id == "":
                print("Employee ID cannot be empty.")
                continue

            if id_exists(employees, emp_id):
                print("Employee ID already exists.")
                continue

            name = input("Enter Name: ").strip()
            department = input("Enter Department: ").strip()

            if not valid_name(name):
                print("Name cannot be empty.")
                continue

            if not valid_department(department):
                print("Department cannot be empty.")
                continue

            try:
                salary = float(input("Enter Basic Salary: "))
            except ValueError:
                print("Enter a valid salary.")
                continue

            if not valid_salary(salary):
                print("Salary must be greater than zero.")
                continue

            employee = Employee(emp_id, name, department, salary)

            employees.append(employee)
            salaries.append(salary)

            print("\nEmployee added successfully.")

            again = input(
                "Do you want to add another employee? (y/n): "
            ).lower().strip()

            if again != "y":
                break

    # 2. DISPLAY ALL EMPLOYEES
    elif choice == "2":

        if len(employees) == 0:
            print("\nNo employees found.")
        else:
            print("\n========== ALL EMPLOYEES ==========")

            for employee in employees:
                employee.display()

    # 3. SEARCH BY EMPLOYEE ID
    elif choice == "3":

        emp_id = input("Enter Employee ID: ").strip()

        employee = search_employee(employees, emp_id)

        if employee is None:
            print("\nEmployee not found.")
        else:
            employee.display()

    # 4. SEARCH BY EMPLOYEE NAME
    elif choice == "4":

        name = input("Enter Employee Name: ").strip()

        employee = search_by_name(employees, name)

        if employee is None:
            print("\nEmployee not found.")
        else:
            employee.display()

    # 5. UPDATE EMPLOYEE
    elif choice == "5":

        emp_id = input("Enter Employee ID to update: ").strip()

        employee = search_employee(employees, emp_id)

        if employee is None:
            print("\nEmployee not found.")
            continue

        name = input("Enter New Name: ").strip()
        department = input("Enter New Department: ").strip()

        if not valid_name(name):
            print("Name cannot be empty.")
            continue

        if not valid_department(department):
            print("Department cannot be empty.")
            continue

        try:
            salary = float(input("Enter New Basic Salary: "))
        except ValueError:
            print("Enter a valid salary.")
            continue

        if not valid_salary(salary):
            print("Salary must be greater than zero.")
            continue

        employee.name = name
        employee.department = department
        employee.salary = salary

        employee.calculate()

        index = employees.index(employee)
        salaries[index] = salary

        print("\nEmployee updated successfully.")

    # 6. DELETE EMPLOYEE
    elif choice == "6":

        emp_id = input("Enter Employee ID to delete: ").strip()

        employee = search_employee(employees, emp_id)

        if employee is None:
            print("\nEmployee not found.")
        else:
            index = employees.index(employee)

            employees.pop(index)
            salaries.pop(index)

            print("\nEmployee deleted successfully.")

    # 7. GENERATE SALARY SLIP
    elif choice == "7":

        emp_id = input("Enter Employee ID: ").strip()

        employee = search_employee(employees, emp_id)

        if employee is None:
            print("\nEmployee not found.")
        else:
            employee.salary_slip()

    # 8. DEPARTMENT-WISE EMPLOYEES
    elif choice == "8":

        department = input("Enter Department: ").strip()

        found = department_employees(employees, department)

        if len(found) == 0:
            print("\nNo employees found in this department.")
        else:
            print("\nEmployees in", department)

            for employee in found:
                print(
                    employee.id,
                    "-",
                    employee.name,
                    "-",
                    employee.salary
                )

    # 9. PAYROLL SUMMARY
    elif choice == "9":

        payroll_summary(employees)

    # 10. HIGHEST SALARY
    elif choice == "10":

        highest_salary(employees)

    # 11. AVERAGE SALARY
    elif choice == "11":

        average_salary(employees)

    # 12. EMPLOYEE COUNT
    elif choice == "12":

        employee_count(employees)

    # 13. SALARY GRADE
    elif choice == "13":

        emp_id = input("Enter Employee ID: ").strip()

        employee = search_employee(employees, emp_id)

        if employee is None:
            print("\nEmployee not found.")
        else:
            print("\nEmployee:", employee.name)
            print("Basic Salary:", employee.salary)
            print("Salary Grade:", employee.grade)

    # 14. SORT BY SALARY
    elif choice == "14":

        sort_by_salary(employees)

    # 15. EXIT
    elif choice == "15":

        print("\nThank you for using the Employee Payroll System.")
        break

    # INVALID CHOICE
    else:

        print("\nInvalid choice.")