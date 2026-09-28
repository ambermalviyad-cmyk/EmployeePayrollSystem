# module for searching

def search_employee(employees, emp_id):
    for employee in employees:
        if employee.id == emp_id:
            return employee

    return None


def search_by_name(employees, name):
    for employee in employees:
        if employee.name.lower() == name.lower():
            return employee

    return None


def department_employees(employees, department):
    found = []

    for employee in employees:
        if employee.department.lower() == department.lower():
            found.append(employee)

    return found