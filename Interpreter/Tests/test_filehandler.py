from Interpreter.filehandler import FileHandler
from Interpreter.validator import a
from unittest import TestCase
from os import path


class TestFileHandler(TestCase):

    def setUp(self):
        self.filehandler = FileHandler(self)
        ######
        self.validator = a

    def tearDown(self):
        self.filehandler = None
        ######
        self.validator.a = None

    def test_read_csv(self):
        """
        Tests reading a .csv data file
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary": "20",
                        "Birthday": "24/06/1994"}}

        dir = path.realpath(path.curdir)
        data = dir + "\\filehandler_tests\\data.csv"
        filehandler = FileHandler(path.normpath(data))
        # filehandler.file_exist()
        filehandler.set_file_type()
        result = filehandler.read()
        self.assertEqual(expected, result)

    def test_read_xlsx(self):
        """
        Tests reading a .xlsx data file
        """
        expected = {0: {"ID": "A233", "Gender": "M", "Age": "22", "Sales": "245", "BMI": "Normal", "Salary": "23",
                        "Birthday": "24/06/1995"}}

        dir = path.realpath(path.curdir)
        data = dir + "\\filehandler_tests\\data.xlsx"
        filehandler = FileHandler(path.normpath(data))
        # filehandler.file_exist()
        filehandler.set_file_type()
        result = filehandler.read()
        print(result)
        self.assertEqual(expected, result)
