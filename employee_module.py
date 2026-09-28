# EMPLOYEE CLASS MODULE

from salary_module import calculate_salary, salary_grade


class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
        self.calculate()

    def calculate(self):
        self.allowance, self.pf, self.gross, self.tax, self.net = calculate_salary(self.salary)
        self.grade = salary_grade(self.salary)

    def display(self):
        print("\n----------------------------")
        print("Employee ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Basic Salary:", self.salary)
        print("Allowance:", self.allowance)
        print("Gross Salary:", self.gross)
        print("PF:", self.pf)
        print("Tax:", self.tax)
        print("Net Salary:", self.net)
        print("Salary Grade:", self.grade)
        print("----------------------------")

    def salary_slip(self):
        print("\n================================")
        print("          SALARY SLIP")
        print("================================")
        print("Employee ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("--------------------------------")
        print("Basic Salary:", self.salary)
        print("Allowance:", self.allowance)
        print("Gross Salary:", self.gross)
        print("PF:", self.pf)
        print("Tax:", self.tax)
        print("--------------------------------")
        print("Net Salary:", self.net)
        print("Salary Grade:", self.grade)
        print("================================")