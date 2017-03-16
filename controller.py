from ReadingData import Validator
from databaseDemo import DatabaseMaker


class Controller(object):
    def __init__(self):
        self.val = Validator()
        self.db = DatabaseMaker()
        self.filename = None

    def read_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
                line = data.split()
                dic = dict(e.split('=') for e in line)
                print(dic)
            self.filename = dic
        except IOError as err:
            print("The exception is: ", err)

    def validate(self):
        self.val.valid(self.filename)

    def db_drop_table(self):
        self.db.drop_table("employee")

    def db_create_table(self):
        self.db.create_table()

    def db_insert(self):
        try:
            i = self.val.get()
            if i:
                self.db.insert(i["id"], i["gender"], i["age"], i["sales"], i["bmi"], i["salary"], i["birthday"])
                return self.db.get()
            else:
                raise Exception("Cannot add invalid data to the database")
        except Exception as err:
            print("The exception is: ", err)

    def database_close(self):
        self.db.close()
