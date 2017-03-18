"""
Problem Domain CMD
"""
import sys
from cmd import Cmd

class DomainCmd(Cmd):
    def __init__(self, con):
        Cmd.__init__(self)
        self.prompt = "-> "
        self.intro = "Welcome to the Problem Domain"
        self.con = con

    # def set_controller(self, con):
    #     self.con = con
    def arg(self):
        try:
            if sys.argv[1] == "barchart":
                self.do_table(None)
            if sys.argv[1] == "read":
                self.do_read(sys.argv[2])
            if sys.argv[1] == "validate":
                self.do_validate(sys.argv[2])
            if sys.argv[1] == "insert":
                self.do_insert(sys.argv[2])
        except Exception as err:
            pass

    def do_read(self, filename):
        self.con.read_file(filename)

    def do_validate(self, filename=None):
        if filename:
            self.con.read_file(filename)
            self.con.validate()
        else:
            self.con.validate()

    def do_check(self, line):
        self.con.view_valid()

    def do_droptable(self, line):
        self.con.db_drop_table()

    def do_createtable(self, line):
        self.con.db_create_table()

    def do_insert(self, filename=None):
        if filename:
            self.con.read_file(filename)
            self.con.validate()
            self.con.db_insert()
        else:
            self.con.db_insert()

    def do_view(self, line):
        self.con.db_view()

    # Quit the cmd
    def do_quit(self, line):
        self.con.database_close()
        print("Closing cmd..")
        return True

    def do_table(self, line):
        self.con.py_view()

    # shortcut
    do_q = do_quit

# if __name__ == '__main__':
#     arg = arg()
#     print(arg)
    # domain = DomainCmd()
    # domain.cmdloop()
