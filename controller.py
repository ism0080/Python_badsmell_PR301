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

    def database(self):
        # db.drop_table("employee")
        self.db.create_table()
        i = self.val.get()
        self.db.insert(i["id"], i["gender"], i["age"], i["sales"], i["bmi"], i["salary"], i["birthday"])
        return self.db.get()

    def database_close(self):
        self.db.close()
