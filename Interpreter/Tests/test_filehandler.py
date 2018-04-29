from Interpreter.filehandler import FileHandler
from unittest import TestCase
from os import path


class TestFileHandler(TestCase):

    def setUp(self):
        self.filehandler = FileHandler(self)

    def tearDown(self):
        del self.filehandler

    def test_read_csv(self):
        """
        Tests reading a .csv data file
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary": "20",
                    "Birthday": "24/06/1994"}}

        dir = path.realpath(path.curdir)
        data = dir + "\\filehandler_tests\\data.csv"
        self.filehandler = FileHandler(path.normpath(data))
        # filehandler.file_exist()
        self.filehandler.set_file_type()
        result = self.filehandler.read()
        self.assertEqual(expected, result)

    def test_read_txt(self):
        """
        Tests reading a .txt data file
        """
        expected = {0: {"ID": "A234", "Gender": "F", "Age": "21", "Sales": "001", "BMI": "Normal", "Salary": "23",
                    "Birthday": "01/01/1996"}}

        dir = path.realpath(path.curdir)
        data = dir + "\\filehandler_tests\\data.txt"
        self.filehandler = FileHandler(path.normpath(data))
        # filehandler.file_exist()
        self.filehandler.set_file_type()
        result = self.filehandler.read()
        print(result)
        print(expected)
        self.assertEqual(expected, result)

    def test_read_xlsx(self):
        """
        Tests reading a .xlsx data file
        """
        expected = {0: {"ID": "A233", "Gender": "M", "Age": "22", "Sales": "245", "BMI": "Normal", "Salary": "23",
                    "Birthday": "24/06/1995"}}

        dir = path.realpath(path.curdir)
        data = dir + "\\filehandler_tests\\data.xlsx"
        self.filehandler = FileHandler(path.normpath(data))
        # filehandler.file_exist()
        self.filehandler.set_file_type()
        result = self.filehandler.read()
        self.assertEqual(expected, result)

