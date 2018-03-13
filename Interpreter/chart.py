from plotly import offline
from plotly.graph_objs import Scatter, Layout, Pie, Bar
from abc import ABCMeta, abstractmethod
import doctest
# Create switch for file or image


# Sam
class GraphType(metaclass=ABCMeta):
    # Wesley
    def __init__(self, data, filename):
        self.filename = filename
        self.data = data

    # Sam
    @abstractmethod
    def draw_graph(self, x_key, y_key, title):
        pass

    # Wesley
    def set_criteria(self, key, statistic):
        """
        This will search through the given dictionary and return each employee that matches the criteria
        e.g. return a dictionary with all people where their gender is male
        :param dictionary: the data that will be used
        :param key: the key value in the dictionary you would like to search
        :param statistic: the set value you would like to search
        :return:
        >>> g.file_type.data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}, 1: {"IhD": "A2f3", "Gender": "Female", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}}
        >>> g.file_type.set_criteria("Gender", "Male")
        {0: {'1ID': 'A23', 'Gender': 'Male', 'Age': 22, 'Sales': 245, 'BMI': 'normal', 'salary': 20, 'Birthday': '24/06/1995'}}
        """
        self.data = {record[0]: record[1] for record in self.data.items() if record[1][key] == statistic}
        return self.data

    # Wesley
    def set_data_keys(self, key_a, key_b):
        """
        :param dictionary:
        :param key_a:
        :param key_b:
        :return:
        >>> g.file_type.data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}, 1: {"IhD": "A2f3", "Gender": "Female", "Age": 22, "Sales": 245, "BMI": "normal", "salary": 20, "Birthday": "24/06/1995"}}
        >>> g.file_type.set_data_keys("Gender", "Sales")
        {'Gender': ['Male', 'Female'], 'Sales': [245, 245]}
        """
        # dictionary = {key1: [value[1] in x for value in record[1].items() if value[0] == key1] for record in dictionary.items()}
        keys_a = list()
        keys_b = list()
        for (key, value) in self.data.items():
            for (key1, value1) in value.items():
                if key1 == key_a:
                    keys_a.append(value1)
                if key1 == key_b:
                    keys_b.append(value1)
        self.data = {key_a: keys_a, key_b: keys_b}
        return self.data


# Sam
class ScatterGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Scatter(x=self.data[x_key], y=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Sam
class PieGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Pie(labels=self.data[x_key], values=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Sam
class BarGraph(GraphType):
    def draw_graph(self, x_key, y_key, graph_title):
        offline.plot({
            "data": [Bar(x=self.data[x_key], y=self.data[y_key])],
            "layout": Layout(title=graph_title)
        }, filename=self.filename)


# Wesley
class Graph:
    # Wesley
    def __init__(self):
        self.file_type = None

    # Wesley
    def set_data(self, dictionary, a_type, filename):
        """
        Set the data to be used
        :param dictionary: Will contain the data that will be used

        :param a_type: set the type of graph to generate
        :param filename: sets the save location and file name
        :return: void
        """
        print("graph")
        print(dictionary)
        types = {
            'pie': PieGraph(dictionary, filename),
            'scatter': ScatterGraph(dictionary, filename),
            'bar': BarGraph(dictionary, filename)
        }
        self.file_type = types[a_type]

    def set_criteria(self, criteria_1, criteria_2):
        self.file_type.set_criteria(criteria_1, criteria_2)

    def set_keys(self, key_1, key_2):
        self.file_type.set_data_keys(key_1, key_2)

    def draw(self, x_key, y_key, title):
        self.file_type.draw_graph(x_key, y_key, title)


#######################################################################################################################
# This section is just to test everything to check that it works, must be commented before running from shell
# This is also used for the doctests!!!
# if __name__ == "__main__":
#     g = Graph()
#     # sample1 = {"x axis": [1, 2, 3, 4, 5, 6, 7, 8, 9], "y axis": [9, 8, 7, 5.5, 5, 4, 3, 2, 1]}
#     data = {0: {"1ID": "A23", "Gender": "Male", "Age": 22, "Sales": 2445, "BMI": "normal", "salary": 20,
#                 "Birthday": "24/06/1995"},
#             1: {"IhD": "A2f3", "Gender": "Male", "Age": 23, "Sales": 2565, "BMI": "normal", "salary": 20,
#                 "Birthday": "24/06/1995"},
#             2: {"IjD": "Aa23", "Gender": "Female", "Age": 25, "Sales": 25, "BMI": "normal", "salary": 20,
#                 "Birthday": "24/06/1995"},
#             3: {"IgD": "A23", "Gender": "Female", "Age": 26, "Sales": 225, "BMI": "normal", "salary": 20,
#                 "Birthday": "24/06/1995"}}
#     g.set_data(data, "bar", "C:\\temp\\random.html")
#     g.file_type.set_criteria("Gender", "Male")
#     g.file_type.set_data_keys("Age", "Sales")
#     g.draw("Age", "Sales", "Age sales for males ")
#     doctest.testmod()
