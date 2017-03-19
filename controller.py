import re
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

    def validate(self):
        try:
            for dict in self.converted_file:
                self.val.valid(dict)
        except Exception as err:
            print("The exception is: No file specified")

    def view_valid(self):
        print("\n VALID DATA:")
        for dict in self.val.get():
            print(dict)

    def db_drop_table(self):
        self.db.drop_table("employee")

    def db_create_table(self):
        self.db.create_table()

    def db_insert(self):
        try:
            list_of_dictionaries = self.val.get()
            if list_of_dictionaries:
                for dict in list_of_dictionaries:
                    self.db.insert(dict["id"], dict["gender"], dict["age"], dict["sales"], dict["bmi"], dict["salary"], dict["birthday"])
                return self.db.get()
            else:
                raise Exception("Cannot add invalid data to the database")
        except Exception as err:
            print("The exception is: ", err)

    def db_view(self):
        self.db.get()

    def database_close(self):
        self.db.close()

    def py_view(self, value):
        try:
            for words in ['age', 'sales', 'salary']:
                if re.search(r'\b' + words + r'\b', value):
                    data = self.db.bar_get(value)
                    self.py.bar_char(value, data)
            else:
                raise Exception("Can't create bar chart from that data")
        except Exception as err:
            print("The exception is: ", err)
