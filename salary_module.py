# SALARY CALCULATION MODULE

def calculate_salary(salary):
    allowance = salary * 10 / 100
    pf = salary * 12 / 100
    gross = salary + allowance

    if gross <= 30000:
        tax = 0
    elif gross <= 50000:
        tax = gross * 5 / 100
    else:
        tax = gross * 10 / 100

    net = gross - pf - tax

    return allowance, pf, gross, tax, net


def salary_grade(salary):
    if salary < 30000:
        return "Grade C"
    elif salary <= 60000:
        return "Grade B"
    else:
        return "Grade A"