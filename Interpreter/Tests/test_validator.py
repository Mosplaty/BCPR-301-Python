from ..validator import Validator
from unittest import TestCase


class TestValidator(TestCase):

    def setUp(self):
        self.validator = Validator()
        self.maxDiff = None

    def tearDown(self):
        self.validator = None

    def test_valid_data(self):
        """
        Tests validating data
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary": "20 000",
                        "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                        "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                    "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertEqual(expected, result)

    def test_invalid_value_ID(self):
        """
        Tests validating data containing an invalid row value ID
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A2232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_value_gen(self):
        """
        Tests validating data containing an invalid row value Gender
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal",
                    "Salary": "20 000", "Birthday": "24/06/1992"}}
        data = {
            0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
            1: {"ID": "A232", "Gender": "Msakjnb", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_value_age(self):
        """
        Tests validating data containing an invalid row value Age
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal",
                    "Salary": "20 000", "Birthday": "24/06/1992"}}
        data = {
            0: {"1D": "A231", "Gender": "Male", "Age": "sadad", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
            1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_value_sales(self):
        """
        Tests validating data containing an invalid row value Sales
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal",
                    "Salary": "20 000", "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "dsajbdk", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_value_bmi(self):
        """
        Tests validating data containing an invalid row value BMI
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal",
                    "Salary": "20 000", "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "insane", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_value_salary(self):
        """
        Tests validating data containing an invalid row value Salary
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal",
                    "Salary": "20 000", "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "dajhsbjfa",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_value_birthday(self):
        """
        Tests validating data containing an invalid row value Birthday
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal",
                    "Salary": "20 000", "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "abcdefg"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_ID(self):
        """
        Tests validating data containing an invalid key for ID
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"IyD": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_gen(self):
        """
        Tests validating data containing an invalid key for Gender
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Genderrrr": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_age(self):
        """
        Tests validating data containing an invalid key for Age
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Ageeee": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_sales(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Saylesz": "270", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_bmi(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMIs": "normal", "Salary": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_salary(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salaryyyyy": "20 000",
                "Birthday": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)

    def test_invalid_key_birthday(self):
        """
        Tests validating data containing an invalid key for Sales
        """
        expected = {0: {"1D": "A231", "Gender": "M", "Age": "23", "Sales": "245", "BMI": "Normal", "Salary":
                    "20 000", "Birthday": "24/06/1994"},
                    1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "Normal", "Salary": "20 000",
                    "Birthday": "24/06/1992"}}
        data = {0: {"1D": "A231", "Gender": "Male", "Age": "23", "Sales": "245", "BMI": "normal", "Salary": "20 000",
                "Birthday": "24/06/1994"},
                1: {"ID": "A232", "Gender": "M", "Age": "25", "Sales": "270", "BMI": "normal", "Salary": "20 000",
                "Birthdayyyyyyyy": "24/06/1992"}}
        result = Validator.save_dict(data)
        self.assertNotEqual(expected, result)
