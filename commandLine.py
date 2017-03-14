"""
Problem Domain CMD
"""
import sys
from cmd import Cmd

from ReadingData import Validator
validator = Validator()


class DomainCmd(Cmd):
    def __init__(self):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.my_name = "unknown"
        self.intro = "Welcome to the Problem Domain"

    def do_validate(self, filename):
        with open(filename, 'r') as file:
            data = file.read()

        e = validator
        print(e.empid(data))
        print(e.gender(data))
        # print(e.age(data))
        # print(e.sales(data))
        # print(e.bmi(data))
        # print(e.salary(data))
        # print(e.birthday(data))

    def do_table(self, line):
        t = validator
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
