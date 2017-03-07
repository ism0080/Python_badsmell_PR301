import re

ID = "A123"
GENDER = "M"
AGE = 12
SALES = 123
BMI = "NORMAL"
SALARY = 10.999
BIRTHDAY = "24-10-1996"


class Validator(object):

    def empid(self, empid):
        match = re.match(r'[A-Z][1-9]{3}', empid)
        if match is not None:
            clean = match.group(0)
        else:
            clean = "Not a Valid ID"
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
        return "EMPID={id}, GENDER={gender}, AGE={age}, SALES={sales}, BMI={bmi}, SALARY={salary}, BIRTHDAY={birthday}".format(id=self.id, gender=self.gender, age=self.age, sales=self.sales, bmi=self.bmi, salary=self.salary, birthday=self.birthday )

e = Validator()
print(e.empid(ID))
j = Table(e.empid(ID), GENDER, AGE, SALES, BMI, SALARY, BIRTHDAY)
print(j.say("mes"))

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
