import unittest
import reader
import database
import command_line
import validator
import display
import controller
import mock
import sys


class MoreTests(unittest.TestCase):
    def setUp(self):
        self.read = reader.FileReader()
        self.valid = validator.Validator()
        self.db = database.DatabaseMaker()
        self.con = controller.Controller()
        self.cmd = command_line.DomainCmd(self.con)
        self.chart = display.PyGal()

    def tearDown(self):
        print("down")

    def test_reader_exception_thrown(self):
        self.assertRaises(Exception, self.read.read("invalid.txt"))

    def test_database_duplicate_data_exception_thrown(self):
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        self.assertRaises(Exception,  self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996'))

    def test_database_noSuchTableData_exceptionThrown(self):
        self.assertRaises(Exception, self.db.get("Dog"))

    def test_database_bar_get(self):
        self.db.drop_table("employee")
        self.db.create_table()
        self.db.insert('A123', 'M', '20', '123', 'Normal', '109', '24-10-1996')
        self.assertEqual(["M"], self.db.bar_get("gender"), 'Not Equal')

    def test_database_bar_get_exception_thrown(self):
        self.assertRaises(Exception, self.db.bar_get("Dog"))

    def test_con_validator(self):
        testFile = self.con.read_file("testData.txt")
        test = self.con.validate()

    def test_con_validator_throw_exception(self):
        self.assertRaises(Exception, self.con.validate())

    def test_validator_get(self):
        self.assertEqual([], self.valid.get())

    def test_con_valid(self):
        self.con.valid('')
        with mock.patch('controller.input') as mp:
            mp.return_value = "table.txt"
            self.con.valid('-f')
        self.con.valid('-v')

    def test_con_reader_throwException(self):
        self.con.read_file("lol")

    def test_con_database(self):
        self.con.db_table('')
        self.con.db_table('-d')
        self.con.db_table('-c')
        self.con.db_table('-dc')
        self.con.db_table('-i')
        with mock.patch('controller.input') as mp:
            mp.return_value = "age"
            self.con.db_table('-v')
        with mock.patch('controller.input') as mp:
            mp.return_value = "table.txt"
            self.con.db_table('-if')
        self.con.database_close()

    def test_con_database_throwException(self):
       self.assertRaises(Exception, self.con.db_table('q'))

    def test_con_pygal(self):
        with mock.patch('controller.input') as mp:
            mp.return_value = "sales"
            self.con.pygal(1)
        with mock.patch('controller.input') as mp:
            mp.return_value = "sales"
            self.con.pygal(2)

    def test_con_pygal_throwException(self):
        self.assertRaises(Exception, self.con.py_view(123))

    def test_con_pickled(self):
        with mock.patch('controller.input') as mp:
            mp.return_value = "data"
            self.con.pickled('')
        with mock.patch('controller.input') as mp:
            mp.return_value = ""
            self.con.pickled('')
        with mock.patch('controller.input') as mp:
            mp.return_value = "data"
            self.con.pickled('-r')
        with mock.patch('controller.input') as mp:
            mp.return_value = ""
            self.con.pickled('-r')
        self.assertRaises(Exception, self.con.pickled('p'))

    def test_cmd_arg_chart(self):
        sys.argv = ['', 'chart', '']
        with mock.patch('controller.input') as mp:
            mp.return_value = "sales"
            self.cmd.arg()

    def test_cmd_arg_read(self):
        sys.argv = ['', 'read', '']
        with mock.patch('controller.input') as mp:
            mp.return_value = "table.txt"
            self.cmd.arg()

    def test_cmd_arg_validate(self):
        sys.argv = ['', 'validate', '']
        self.cmd.arg()

    def test_cmd_arg_db(self):
        sys.argv = ['', 'db', '']
        self.cmd.arg()

    def test_cmd_arg_throwException(self):
        sys.argv = "cart"
        self.assertRaises(Exception, self.cmd.arg())

    def test_cmd(self):
        self.cmd.do_read("table.txt")
        self.cmd.do_read("")
        self.cmd.do_validate('')
        self.cmd.do_db('')
        with mock.patch('controller.input') as mp:
            mp.return_value = "age"
            self.cmd.do_chart('')
        with mock.patch('controller.input') as mp:
            mp.return_value = "data"
            self.cmd.do_serial('')
        self.cmd.do_quit("line")

    if __name__ == "__main__":  # pragma: no cover
        unittest.main(verbosity=True)  # with more detail
        # unittest.main()
        # unittest.main(exit=False) # with more detail