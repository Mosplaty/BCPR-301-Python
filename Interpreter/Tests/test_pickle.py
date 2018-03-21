from ..pickler import Pickler
from unittest import TestCase


# Wesley
class TestPicklerSetUp(TestCase):
    # Wesley
    def setUp(self):
        self.pickler = Pickler()

    # Wesley
    def tearDown(self):
        # self.pickler.dispose()
        self.pickler = None

    # Wesley
    # def test_pickle_record_byte_stream(self):
    #     """Check if values are a byte stream when using pickle_record_values function"""
    #     key = "test"
    #     expected = bytes
    #     value = {"ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday":
    #              "24/06/1995"}
    #     data = self.pickler.pickle_record_values(key, value)
    #     result = type(data["test"])
    #     self.assertEqual(result, expected)

    # Wesley
    # def test_pickle_record_return_dict(self):
    #     """Function returns a dictionary"""
    #     key = "test"
    #     expected = dict
    #     value = {"ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday":
    #              "24/06/1995"}
    #     result = self.pickler.pickle_dictionary_values(key, value)
    #     self.assertIsInstance(result, expected)

    # Wesley
    def test_pickle_dictionary_type_byte(self):
        """True if all values in dictionary are of type 'byte'"""
        expected = bytes
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = self.pickler.pickle_dictionary_values(data)
        result = (type(value) == expected for value in data.values())
        self.assertTrue(all(result))

    # Wesley
    def test_pickle_dictionary_type_string(self):
        """False if any values in dictionary are of type 'string'"""
        the_type = bytes
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = self.pickler.pickle_dictionary_values(data)
        data[2] = "This is a string"
        result = (type(value) == the_type for value in data.values())
        self.assertFalse(all(result))

    # Wesley
    def test_pickle_dictionary_type_string_true(self):
        """True if a value in dictionary are of type 'string'"""
        the_type = str
        data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                1: {"IhD": "A2f3", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                2: {"IjD": "Aa23", "Genkder": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"},
                3: {"IgD": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20,
                    "Birthday": "24/06/1995"}}
        data = self.pickler.pickle_dictionary_values(data)
        data[2] = "This is a string"
        result = (type(value) == the_type for value in data.values())
        self.assertTrue(any(result))

