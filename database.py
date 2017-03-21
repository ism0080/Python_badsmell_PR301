import sqlite3


class DatabaseMaker(object):
    def __init__(self):
        try:
            self.connection = sqlite3.connect("problem_domain.db")
            self.cursor = self.connection.cursor()
        except Exception as e:
            print(e)
        else:
            print("Opened database successfully")
        finally:
            print("Finishing connecting to database")

    def drop_table(self, table):
        format_str = """DROP TABLE {table};"""
        sql_command = format_str.format(table=table)
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
            format_str = """INSERT INTO employee (staff_number,
                                                  id,
                                                  gender,
                                                  age,
                                                  sales,
                                                  bmi,
                                                  salary,
                                                  birthday)
                            VALUES (NULL, "{id}",
                                          "{gender}",
                                          "{age}",
                                          "{sales}",
                                          "{bmi}",
                                          "{salary}",
                                          "{birthday}");"""

            sql_command = format_str.format(id=p[0],
                                            gender=p[1],
                                            age=p[2],
                                            sales=p[3],
                                            bmi=p[4],
                                            salary=p[5],
                                            birthday=p[6])
            self.cursor.execute(sql_command)
        self.connection.commit()

    def get(self, value):
        try:
            format_str = "SELECT {value} FROM employee"
            sql_command = format_str.format(value=value)
            self.cursor.execute(sql_command)
            print("fetchall:")
            result = self.cursor.fetchall()
            list = []
            for r in result:
                list.extend([r])
            return list
        except Exception as err:
            print(err)

    def bar_get(self, value):
        try:
            format_str = "SELECT {value} FROM employee"
            sql_command = format_str.format(value=value)
            self.cursor.execute(sql_command)
            result = self.cursor.fetchall()
            list = []
            for r in result:
                list.extend(r)
            return list
        except Exception as err:
            print(err)

    def close(self):
        self.connection.close()
