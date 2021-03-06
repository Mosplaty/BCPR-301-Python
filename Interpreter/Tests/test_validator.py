from Interpreter.validator import Validator
from unittest import TestCase
from datetime import datetime


class TestValidator(TestCase):

    def setUp(self):
        self.validator = Validator()

    def tearDown(self):
        del self.validator

    def test_valid_data(self):
        """
        Tests validating data
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary": "20",
                        "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "290", "BMI": "Normal", "Salary": "200",
                        "Birthday": "24/06/1992"},
                    2: {"ID": "A233", "Gender": "F", "Age": "30", "Sales": "222", "BMI": "Overweight", "Salary": "200",
                        "Birthday": "24/06/1987"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                    "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "290", "BMI": "Normal", "Salary": "200",
                    "Birthday": "24/06/1992"},
                2: {"ID": "A233", "Gender": "Female", "Age": "30", "Sales": "222", "BMI": "overweight", "Salary": "200",
                    "Birthday": "24/06/1987"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_ID(self):
        """
        Tests validating data containing an invalid row value for ID
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A2232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_gen(self):
        """
        Tests validating data containing an invalid row value for Gender
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "Msakjnb", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_age(self):
        """
        Tests validating data containing an invalid row value for Age
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {
            0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
            1: {"ID": "A232", "Gender": "M", "Age": "jhfbkjsa", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_sales(self):
        """
        Tests validating data containing an invalid row value for Sales
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "dsajbdk", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_bmi(self):
        """
        Tests validating data containing an invalid row value for BMI
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "insane", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_salary(self):
        """
        Tests validating data containing an invalid row value for Salary
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "dajhsbjfa",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_birthday(self):
        """
        Tests validating data containing an invalid row value for Birthday
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "abcdefg"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_ID(self):
        """
        Tests validating data containing an invalid key for ID
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"IyD": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_gen(self):
        """
        Tests validating data containing an invalid key for Gender
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Genderrrr": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_age(self):
        """
        Tests validating data containing an invalid key for Age
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Ageeee": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_sales(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Saylesz": "270", "BMI": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_bmi(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMIs": "normal", "Salary": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_salary(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salaryyyyy": "200",
                "Birthday": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_key_birthday(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "200",
                "Birthdayyyyyyyy": "24/06/1992"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_birthday_replace(self):
        """
        Tests validating data containing an invalid delimiter value for Birthday
        """
        expected = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24/06/1994"}}
        data = {0: {"ID": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20", "Birthday": "24_06_1994"}}
        result = self.validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_xlsx_date(self):
        """
        Tests validating data containing a date in xlsx format
        """
        expected = "24/05/1993"
        data = datetime(1993, 5, 24)
        result = self.validator.xlsx_date(data)
        self.assertEqual(expected, result)
