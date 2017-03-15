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
                line = data.split()
                dic = dict(e.split('=') for e in line)
                print(dic)
                self.filename = dic
        except IOError as err:
            print("The exception is: ", err)

    def do_validate(self, line):
        data = self.filename
        print(val.valid(data))

    def do_table(self, line):
        print(val)

    # Quit the cmd
    def do_quit(self, line):
        print("Closing cmd..")
        return True

    # shortcut
    do_q = do_quit

if __name__ == '__main__':
    domain = DomainCmd()
    domain.cmdloop()
