import re

# ID = "A123"
# GENDER = "M"
# AGE = 12
# SALES = 123
# BMI = "NORMAL"
# SALARY = 10.999
# BIRTHDAY = "24-10-1996"

# file = open("table.txt", "r")
# for line in file:
#     print(line)

with open('table.txt', 'r') as file:
    data = file.read()
    print(data)


class Validator(object):
    def empid(self, empid):
        match = re.search(r'id=[A-Z][1-9]{3}', empid)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

    def gender(self, gender):
        match = re.search(r'gender=M|F', gender)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

    def age(self, age):
        match = re.search(r'age=[0-9]{2}', age)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

    def sales(self, sales):
        match = re.search(r'sales=[0-9]{3}', sales)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

    def bmi(self, bmi):
        match = re.search(r'bmi=(Normal|Overweight|Obesity|Underweight)', bmi)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

    def salary(self, salary):
        match = re.search(r'salary=[0-9]{2,3}', salary)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

    def birthday(self, birthday):
        match = re.search(r'birthday=[0-3][1-9]-[0-9]{1,2}-[1-9]{4}', birthday)
        if match is not None:
            clean = match.group(0)
        else:
            clean = ""
        return clean

class Table(object):
    def __init__(self, new_id, new_gender, new_age, new_sales, new_bmi, new_salary, new_birthday):
        self.id = new_id
        self.gender = new_gender
        self.age = new_age
        self.sales = new_sales
        self.bmi = new_bmi
        self.salary = new_salary
        self.birthday = new_birthday

    def say(self, msg):
        return "EMPID={id}, GENDER={gender}, AGE={age}, SALES={sales}, BMI={bmi}, SALARY={salary}, BIRTHDAY={birthday}".format(
            id=self.id, gender=self.gender, age=self.age, sales=self.sales, bmi=self.bmi, salary=self.salary,
            birthday=self.birthday)


e = Validator()
print(e.empid(data))
print(e.gender(data))
print(e.age(data))
print(e.sales(data))
print(e.bmi(data))
print(e.salary(data))
print(e.birthday(data))
# j = Table(e.empid(ID), GENDER, AGE, SALES, BMI, SALARY, BIRTHDAY)
# print(j.say("mes"))

# try:
#     matchObj = re.match(r'[A-Z][1-9]{3}', ID)
#     if matchObj:
#         var_id = ID
#         print(var_id)
# except re.error:
#     print("Enter a valid ID")
#

# ID = "A123"
# re.match(r'[A-Z][1-9]{3}', ID)
