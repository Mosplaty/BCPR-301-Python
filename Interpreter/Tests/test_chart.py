from Interpreter.chart import Graph
from unittest import TestCase


class TestChart(TestCase):

    def setUp(self):
        self.graph = Graph()
        self.testArray = {0: {"ID": "A233", "Gender": "M", "Age": "22", "Sales": "245", "BMI": "Normal",
                              "Salary": "20", "Birthday": "24/06/1995"},
                          1: {"ID": "A244", "Gender": "F", "Age": "30", "Sales": "666", "BMI": "Underweight",
                              "Salary": "301", "Birthday": "05/05/1988"},
                          2: {"ID": "A525", "Gender": "M", "Age": "35", "Sales": "456", "BMI": "Obesity",
                              "Salary": "84", "Birthday": "01/08/1983"},
                          3: {"ID": "A266", "Gender": "M", "Age": "24", "Sales": "999", "BMI": "Normal",
                              "Salary": "999", "Birthday": "24/05/1993"}}

    def tearDown(self):
        self.graph = None

    # Ughhhhhhhhhhhh
    def test_chart_bar(self):
        self.graph.set_data(self.testArray, "pie", "expected_test")
        self.graph.set_criteria("Gender", "Male")
        self.graph.set_keys("Salary", "Sales")
        result = self.graph.draw("Salary", "Sales", "Title")
