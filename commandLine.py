"""
Problem Domain CMD
"""
import sys
from cmd import Cmd

from ReadingData import Validator
val = Validator()


class DomainCmd(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.filename = None
        self.my_name = "unknown"
        self.intro = "Welcome to the Problem Domain"

    def do_read(self, filename):
        try:
            with open(filename, 'r') as file:
                data = file.read()
            print(data)
        except IOError as err:
            print("The exception is: ", err)

    def do_validate(self, line):
        data = self.filename
        print(val.empid(data))
        print(val.gender(data))
        print(val.age(data))
        print(val.sales(data))
        print(val.bmi(data))
        print(val.salary(data))
        print(val.birthday(data))

    def do_table(self, line):
        t = val
        print(t)

    # Quit the cmd
    def do_quit(self, line):
        print("Closing cmd..")
        return True

    # shortcut
    do_q = do_quit

if __name__ == '__main__':
    domain = DomainCmd()
    domain.cmdloop()
