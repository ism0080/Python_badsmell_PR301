from validator import Validator
from database import DatabaseMaker
from reader import FileReader
from display import PyGal


class Controller(object):
    def __init__(self):
        self.val = Validator()
        self.db = DatabaseMaker()
        self.reader = FileReader()
        self.py = PyGal()
        self.converted_file = None
        self.file_count = 1

    def read_file(self, filename):
        try:
            self.converted_file = self.reader.read(filename)
            for dict in self.converted_file:
                print("FILE_DATA:", self.file_count, "\n", dict)
                self.file_count += 1
        except Exception as err:
            print("The exception is: ", err)

    def valid(self, flag):
        if flag == '':
            self.validate()
        if flag == '-f':
            file = input("Validate which file?:")
            self.read_file(file)
            self.validate()
        if flag == '-v':
            self.view_valid()
        if flag == '-fv':
            file = input("Validate which file?:")
            self.read_file(file)
            self.validate()

    def validate(self):
        try:
            for dict in self.converted_file:
                self.val.valid(dict)
            return self.view_valid()
        except Exception as err:
            print("The exception is: No file specified")

    def view_valid(self):
        print("\n VALID DATA:")
        for dict in self.val.get():
            print(dict)

    def db_table(self, flag):
        if flag == "-d":
            self.db_drop_table()
        elif flag == '-c':
            self.db_create_table()
        elif flag == '-dc':
            self.db_drop_table()
            self.db_create_table()
        elif flag == '-i':
            for i in self.db_insert():
                print(i)
        elif flag == '-v':
            value = input("What column do you want to\
                            see from the employee table?")
            self.db_view(value)
        elif flag == '-if':
            file = input("Input which file?:")
            self.read_file(file)
            self.validate()
            self.db_insert()
        elif flag == '':
            self.db_view("*")

    def db_drop_table(self):
        self.db.drop_table("employee")

    def db_create_table(self):
        self.db.create_table()

    def db_insert(self):
        try:
            list_of_dictionaries = self.val.get()
            if list_of_dictionaries:
                for dict in list_of_dictionaries:
                    self.db.insert(dict["id"],
                                   dict["gender"],
                                   dict["age"],
                                   dict["sales"],
                                   dict["bmi"],
                                   dict["salary"],
                                   dict["birthday"])
                return self.db.get("*")
            else:
                raise Exception("Cannot add invalid data to the database")
        except Exception as err:
            print("The exception is: ", err)

    def db_view(self, value):
        for v in self.db.get(value):
            print(v)

    def database_close(self):
        self.db.close()

    def pygal(self, flag):
        if flag == '':
            value = input("Which data do you want to see a bar graph of?")
            self.py_view(value)
        if flag == '-d':
            value = input("Input first bar graph comparison:")
            value2 = input("Input second bar graph comparison:")
            self.py_view(value, value2)

    def py_view(self, value, value2=None):
        try:
            data = self.db.bar_get(value)
            if value2 is not None:
                data2 = self.db.bar_get(value2)
                self.py.bar_char(value, data, value2, data2)
            else:
                self.py.bar_char(value, data)
        except Exception as err:
            print("The exception is: ", err)

    def pickled(self, flag):
        if flag == '':
            self.pickled_write()
        elif flag == '-r':
            self.pickled_read()

    def pickled_write(self):
        import pickle
        with open('data.pickle', 'wb') as f:
            pickle.dump(self.converted_file, f)

    def pickled_read(self):
        import pickle
        with open('data.pickle', 'rb') as f:
            data = pickle.load(f)
        print(data)
        # print(data == self.db_view("*"))
