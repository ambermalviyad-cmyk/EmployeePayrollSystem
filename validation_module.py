# INPUT OF THE VALIDATION MODULE

def valid_name(name):
    return name != ""


def valid_department(department):
    return department != ""


def valid_salary(salary):
    return salary > 0


def id_exists(employees, emp_id):
    for employee in employees:
        if employee.id == emp_id:
            return True

    return False