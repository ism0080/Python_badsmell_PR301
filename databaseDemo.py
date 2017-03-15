import sqlite3

# conn = sqlite3.connect('problem_domain.db')
# c = conn.cursor()
#
# # create table
# c.execute('''CREATE TABLE IF NOT EXISTS employer
#              (id char(4) PRIMARY KEY NOT NULL, gender char(1), age INT(2), sales INT, bmi VARCHAR(11), salary INT, birthday DATE )''')
#
# #insert data
# c.execute("INSERT INTO employer VALUES ('A123','M','32',100,'Normal', 104, '1996-10-24')")
#
# for row in c.execute('SELECT * FROM employer'):
#         print(row)


class DatabaseMaker(object):
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.c = self.conn.cursor()

    # def connection(self):
    #     conn = sqlite3.connect('problem_domain.db')
    #     c = conn.cursor()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS employer
                      (id char(4) PRIMARY KEY NOT NULL, gender char(1), age INT(2), sales INT, bmi VARCHAR(11), salary INT, birthday DATE )''')

    def insert(self, id, gender, age, sales, bmi, salary, birthday):
        self.c.execute("INSERT INTO employer VALUES (id, gender, age, sales, bmi, salary, birthday)")

    def __str__(self):
        for row in self.c.execute('SELECT * FROM employer'):
            return row