import re
# file = open("table.txt", "r")
# for line in file:
#     print(line)

# with open('table2.txt', 'r') as file:
#     # data = file.readlines()
#     data2 = file.read()
#     # print(data)

    # line = data2.split()
    # dic = dict(e.split('=') for e in line)
    # print(dic)
    # # print(data.split('='))


class Validator(object):

    def __init__(self):
        self.regDic = {"id": r'[A-Z][1-9]{3}',
                       "gender": r'M|F',
                       "age": r'[0-9]{2}',
                       "sales": r'[0-9]{3}',
                       "bmi": r'(Normal|Overweight|Obesity|Underweight)',
                       "salary": r'[0-9]{2,3}',
                       "birthday": r'[0-3][1-9]-[0-9]{1,2}-[1-9]{4}'}
        self.dictionary = {}
        # # for i, j in reg:
        # self.regLi = [r'[A-Z][1-9]{3}',
        #               r'M|F',
        #               r'[0-9]{2}',
        #               r'[0-9]{3}',
        #               r'(Normal|Overweight|Obesity|Underweight)',
        #               r'[0-9]{2,3}',
        #               r'[0-3][1-9]-[0-9]{1,2}-[1-9]{4}']

    def valid(self, filename):
        # clean = []
        un_clean = []
        try:
            for key, value in filename.items():
                match = re.search(self.regDic.get(key), value)
                if match is not None:
                    # clean.extend(["{} = True".format(key.upper())])
                    self.dictionary[key] = value
                else:
                    un_clean.extend(["{} = False".format(key.upper())])
                    # raise Exception("Data is invalid")
                    # clean.extend(["{} = False".format(key.upper())])
            if len(self.dictionary) < 7:
                raise Exception("Data is invalid")
        except Exception as err:
            print("The exception is:", err)
            # clean = []
            self.dictionary = {}
            # if match is None:
            #     un_clean.extend(["{} = False".format(key.upper())])
        finally:
            if self.dictionary:
                print(self.dictionary)
                print("\nVALIDATION SUCCESSFUL")
            else:
                print(un_clean)

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


# e = Validator()
# print(e.valid(dic))
