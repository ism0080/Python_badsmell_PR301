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
    def __init__(self):
        # self.db = db
        # self.conn = sqlite3.connect(self.db)
        # self.c = self.conn.cursor()
        try:
            self.connection = sqlite3.connect("problem_domain.db")
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connecting to database")

    # def connection(self):
    #     conn = sqlite3.connect('problem_domain.db')
    #     c = conn.cursor()
    def drop_table(self, table):
        format_str = """DROP TABLE {table};"""
        sql_command = format_str.format(table = table)
        self.cursor.execute(sql_command)

    def create_table(self):
        sql_command = """
        CREATE TABLE IF NOT EXISTS employee (
        staff_number INTEGER PRIMARY KEY,
        id CHAR(4),
        gender CHAR(1),
        age INT(2),
        sales INT,
        bmi VARCHAR(11),
        salary INT,
        birthday DATE);"""
        self.cursor.execute(sql_command)

    def insert(self, id, gender, age, sales, bmi, salary, birthday):
        staff_data = [(id, gender, age, sales, bmi, salary, birthday)]
        for p in staff_data:
            format_str = """INSERT INTO employee (staff_number, id, gender, age, sales, bmi, salary, birthday)
            VALUES (NULL, "{id}", "{gender}", "{age}", "{sales}", "{bmi}", "{salary}", "{birthday}");"""

            sql_command = format_str.format(id=p[0], gender=p[1], age=p[2], sales=p[3], bmi=p[4], salary=p[5], birthday=p[6])
            self.cursor.execute(sql_command)
        self.connection.commit()

    def get(self):
        try:
            self.cursor.execute("SELECT * FROM employee")
            print("fetchall:")
            result = self.cursor.fetchall()
            for r in result:
                print(r)
        except Exception as err:
            print(err)

    def bar_get(self):
        try:
            self.cursor.execute("SELECT age FROM employee")
            # print("fetchall:")
            result = self.cursor.fetchall()
            list = []
            for r in result:
                list.extend(r)
            return list
        except Exception as err:
            print(err)

    def close(self):
        self.connection.close()