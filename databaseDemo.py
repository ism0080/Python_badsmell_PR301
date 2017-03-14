import sqlite3

conn = sqlite3.connect('problem_domain.db')
c = conn.cursor()

# create table
c.execute('''CREATE TABLE IF NOT EXISTS employer
             (id char(4) PRIMARY KEY NOT NULL, gender char(1), age INT(2), sales INT, bmi VARCHAR(11), salary DECIMAL(2,3), birthday DATE )''')

#insert data
c.execute("INSERT INTO employer VALUES ('A123','M','32',100,'Normal', 10.222, '1996-10-24')")

for row in c.execute('SELECT * FROM employer'):
        print(row)
