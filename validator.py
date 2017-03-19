import re
from datetime import date
# file = open("table.txt", "r")
# for line in file:
#     print(line)

# with open('table.txt', 'r') as file:
#     # data = file.readlines()
#     data2 = file.read()
#     # print(data)
#
#     line = data2.split()
#     dic = dict(e.split('=') for e in line)
#     # print(dic)
#     # print(data.split('='))

# with open("table5.txt", 'r') as file:
#     file_data = file.read()
#     # splits on newline
#     group = file_data.split('\n')
#     line = []
#     list_of_dictionaries = []
#     i = 0
#     for x in group:
#         line.extend([group[i].split(', ')])
#         list_of_dictionaries.extend([i])
#         i += 1
#     for empty in list_of_dictionaries:
#         list_of_dictionaries[empty] = dict(e.split('=') for e in line[empty])
#     # for dictionary in list_of_dictionaries:
#     #     print(dictionary)



class Validator(object):

    def __init__(self):
        self.regDic = {"id": r'[A-Z][0-9]{3}',
                       "gender": r'M|F',
                       "age": r'[0-9]{2}',
                       "sales": r'[0-9]{3}',
                       "bmi": r'(Normal|Overweight|Obesity|Underweight)',
                       "salary": r'^[0-9]{2,3}$',
                       "birthday": r'[0-31]\w-[0-12]\w-[0-9]{4}'}
        self.dictionary = {}
        self.list_of_dictionaries = []
        self.file_count = 1

    def valid(self, filename):
        invalid = []
        self.dictionary = {}
        try:
            print("\nFILE_DATA:", self.file_count)
            for key, value in filename.items():
                match = re.search(self.regDic.get(key), value)
                if match is not None:
                    if self.valid_date(filename["birthday"]):
                        if int(self.valid_age(filename["birthday"])) == int(filename["age"]):
                            self.dictionary[key] = value
                        else:
                            raise Exception("Age does not match birthdate")
                    else:
                        break
                else:
                    invalid.extend(["{} = False".format(key.upper())])
            if len(self.dictionary) < 7:
                raise Exception("Data is invalid")
        except Exception as err:
            print("The exception is:", err)
            self.dictionary = {}
        finally:
            self.file_count += 1
            if self.dictionary:
                print(self.dictionary, "\nVALIDATION SUCCESSFUL")
                self.list_of_dictionaries.extend([self.dictionary])
            else:
                print(filename, "\n", invalid, "\nVALIDATION FAILED")

    # def valid(self, filename):
    #     invalid = []
    #     try:
    #         print("\nFILE", self.file_count)
    #         for key, value in filename.items():
    #             match = re.search(self.regDic.get(key), value)
    #             if match is not None:
    #                 self.dictionary[key] = value
    #             else:
    #                 invalid.extend(["{} = False".format(key.upper())])
    #         if len(self.dictionary) < 7:
    #             raise Exception("Data is invalid")
    #         if self.valid_date(self.dictionary["birthday"]):
    #             if int(self.valid_age(self.dictionary["birthday"])) == int(self.dictionary["age"]):
    #                 pass
    #             else:
    #                 raise Exception("Age does not match birthdate")
    #     except Exception as err:
    #         print("The exception is:", err)
    #         self.dictionary = {}
    #     finally:
    #         self.file_count += 1
    #         if self.dictionary:
    #             print(self.dictionary, "\nVALIDATION SUCCESSFUL")
    #             self.list_of_dictionaries.extend([self.dictionary])
    #         else:
    #             print(filename, "\n", invalid, "\nVALIDATION FAILED")

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
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        return age

    def get(self):
        # for dict in self.list_of_dictionaries:
        #     print(dict)
        return self.list_of_dictionaries

    # def __str__(self):
    #     s = ""
    #     for key, value in self.dictionary.items():
    #         s += key + " = " + value + "\n"
    #     return s

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


# e = Validator()
# for dictionary in list_of_dictionaries:
#     print(e.valid(dictionary))
#
# for i in e.get():
#     print(i)

