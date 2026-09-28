# PAYROLL SUMMARY

def payroll_summary(employees):
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    basic = 0
    allowance = 0
    pf = 0
    tax = 0
    net = 0

    for employee in employees:
        basic += employee.salary
        allowance += employee.allowance
        pf += employee.pf
        tax += employee.tax
        net += employee.net

    
    print("        PAYROLL SUMMARY")
    print("===============================")
    print("Total Employees:", len(employees))
    print("Total Basic Salary:", basic)
    print("Total Allowance:", allowance)
    print("Total PF:", pf)
    print("Total Tax:", tax)
    print("Total Net Salary:", net)
    print("=======================")


def highest_salary(employees):
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    highest = employees[0]

    for employee in employees:
        if employee.salary > highest.salary:
            highest = employee

    print("\nHIGHEST SALARY EMPLOYEE")
    highest.display()


def average_salary(employees):
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    total = 0

    for employee in employees:
        total += employee.salary

    average = total / len(employees)

    print("\nAverage Basic Salary:", average)


def employee_count(employees):
    print("\nTotal Employees:", len(employees))


def sort_by_salary(employees):
    if len(employees) == 0:
        print("\nNo employees found.")
        return

    sorted_employees = employees.copy()

    for i in range(len(sorted_employees)):
        for j in range(0, len(sorted_employees) - i - 1):
            if sorted_employees[j].salary > sorted_employees[j + 1].salary:
                temp = sorted_employees[j]
                sorted_employees[j] = sorted_employees[j + 1]
                sorted_employees[j + 1] = temp

    print("\nEMPLOYEES SORTED BY SALARY")

    for employee in sorted_employees:
        print(employee.id, "-", employee.name, "-", employee.salary)