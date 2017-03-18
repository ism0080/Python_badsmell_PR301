import re
from datetime import date
# file = open("table.txt", "r")
# for line in file:
#     print(line)

with open('table.txt', 'r') as file:
    # data = file.readlines()
    data2 = file.read()
    # print(data)

    line = data2.split()
    dic = dict(e.split('=') for e in line)
    # print(dic)
    # print(data.split('='))


class Validator(object):

    def __init__(self):
        self.regDic = {"id": r'[A-Z][1-9]{3}',
                       "gender": r'M|F',
                       "age": r'[0-9]{2}',
                       "sales": r'[0-9]{3}',
                       "bmi": r'(Normal|Overweight|Obesity|Underweight)',
                       "salary": r'[0-9]{2,3}',
                       "birthday": r'[0-3][0-9]-[0-9]{1,2}-[0-9]{4}'}
        self.dictionary = {}
        self.list_of_dictionaries = []

    def valid(self, filename):
        un_clean = []
        try:
            for key, value in filename.items():
                match = re.search(self.regDic.get(key), value)
                if match is not None:
                    self.dictionary[key] = value
                else:
                    un_clean.extend(["{} = False".format(key.upper())])
            if len(self.dictionary) < 7:
                raise Exception("Data is invalid")
            if self.valid_date(self.dictionary["birthday"]):
                if int(self.valid_age(self.dictionary["birthday"])) == int(self.dictionary["age"]):
                    pass
                else:
                    raise Exception("Age does not match birthdate")
        except Exception as err:
            print("The exception is:", err)
            self.dictionary = {}
        finally:
            if self.dictionary:
                print(self.dictionary)
                print("\nVALIDATION SUCCESSFUL")
            else:
                print(un_clean)
                print("\nVALIDATION FAILED")

    def valid_date(self, mydate):
        minyear = 1900
        maxyear = date.today().year

        mydate = mydate
        dateparts = mydate.split('-')
        try:
            if int(dateparts[2]) > maxyear or int(dateparts[2]) < minyear:
                raise ValueError("Year out of range")
            dateobj = date(int(dateparts[2]), int(dateparts[1]), int(dateparts[0]))
            return True
        except ValueError as err:
            self.dictionary = {}
            print(err)

    def valid_age(self, mydate):
        today = date.today()
        dateparts = mydate.split('-')
        born = date(int(dateparts[2]), int(dateparts[1]), int(dateparts[0]))
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def get(self):
        return self.dictionary

    def __str__(self):
        s = ""
        for key, value in self.dictionary.items():
            s += key + " = " + value + "\n"
        return s

    # def valid(self, input):
    #     clean = []
    #     i = 0
    #     for key, value in input.items():
    #         match = re.search(self.regLi[i], value)
    #         if match is not None:
    #             clean.extend(["{} = True Validation".format(key.upper())])
    #         else:
    #             clean.extend(["{} = False Validation".format(key.upper())])
    #         i += 1
    #     return clean


e = Validator()
print(e.valid(dic))
