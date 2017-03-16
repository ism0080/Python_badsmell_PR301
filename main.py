from commandLine import DomainCmd
from controller import Controller

if __name__ == '__main__':
    con = Controller()
    cmdView = DomainCmd(con)
    # cmdView.set_controller(con)
    cmdView.cmdloop()
