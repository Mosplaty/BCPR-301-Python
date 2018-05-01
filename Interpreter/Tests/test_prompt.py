from Interpreter.prompt import Shell
from unittest import TestCase
from unittest.mock import patch, create_autospec
from io import StringIO
import sys


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


class TestPrompt(TestCase):

    def setUp(self):
        self.prompt = Shell()
        self.expected = ""

    def tearDown(self):
        del self.prompt
        del self.expected

    def answer(self):
        result = input('Enter yes or no')  # pragma: no cover
        if result == self.expected:  # pragma: no cover
            return result  # pragma: no cover
        else:
            return result  # pragma: no cover

    def test_cd(self):
        self.expected = ['H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\'
                         'Interpreter']
        with Capturing() as output:
            self.prompt.do_cd('..')
        self.assertEqual(output, self.expected)

    def test_cd_notvalid(self):
        self.expected = ["Not a valid directory"]
        with Capturing() as output:
            self.prompt.do_cd('blah')
        self.assertEqual(output, self.expected)

    def test_cd_nopath(self):
        self.expected = ["No path was specified, please try again"]
        with Capturing() as output:
            self.prompt.do_cd('')
        self.assertEqual(output, self.expected)

    def test_load_db_local(self):
        self.expected = ['No data found']
        user_input = ['local', 'test']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_load("-database")
        self.assertEqual(output, self.expected)

    def test_load_db_local_exists(self):
        self.expected = ['Data has been loaded']
        self.prompt.do_load('filehandler_tests/data.csv')
        user_input = ['test']
        with patch('builtins.input', side_effect=user_input):
            self.prompt.do_save("local")
        user_input = ['local', 'test']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_load("-database")
        self.assertEqual(output, self.expected)

    def test_load_db_remote(self):
        self.expected = ['No data found']
        user_input = ['remote', 'localhost', 'root', '', 'test']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_load("-database")
        self.assertEqual(output, self.expected)

    def test_load_db_remote_exists(self):
        self.expected = ['Data has been loaded']
        self.prompt.do_load('filehandler_tests/data.csv')
        user_input = ['localhost', 'root', '', 'test']
        with patch('builtins.input', side_effect=user_input):
            self.prompt.do_save("remote")
        user_input = ['remote', 'localhost', 'root', '', 'test']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_load("-database")
        self.assertEqual(output, self.expected)

    def test_load_db_invalid(self):
        self.expected = ['invalid database type']
        user_input = ['thingy', 'test']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_load("-database")
        self.assertEqual(output, self.expected)

    def test_load_nopath(self):
        self.expected = ["Path is not a file"]
        with Capturing() as output:
            self.prompt.do_load('blah')
        self.assertEqual(output, self.expected)

    def test_load_noval(self):
        self.expected = ["No path was specified, please try again"]
        with Capturing() as output:
            self.prompt.do_load('')
        self.assertEqual(output, self.expected)

    def test_load_csv(self):
        self.expected = ['.csv', 'Adding Row 0', "{'ID': 'A231', 'Gender': 'M', 'Age': '23', 'Sales': '245', "
                         "'BMI': 'Normal', 'Salary': '20', 'Birthday': '24/06/1994'}",
                         "{0: {'ID': 'A231', 'Gender': 'M', 'Age': '23', 'Sales': '245', 'BMI': 'Normal', "
                         "'Salary': '20', 'Birthday': '24/06/1994'}}"]
        with Capturing() as output:
            self.prompt.do_load('filehandler_tests/data.csv')
        self.assertEqual(output, self.expected)

    def test_load_xlsx(self):
        self.expected = ['.xlsx', 'Adding Row 0', "{'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', "
                         "'BMI': 'Normal', 'Salary': '23', 'Birthday': '24/06/1995'}",
                         "{0: {'ID': 'A233', 'Gender': 'M', 'Age': '22', 'Sales': '245', 'BMI': 'Normal', "
                         "'Salary': '23', 'Birthday': '24/06/1995'}}"]
        with Capturing() as output:
            self.prompt.do_load('filehandler_tests/data.xlsx')
        self.assertEqual(output, self.expected)

    def test_load_txt(self):
        self.expected = ['.txt', 'Adding Row 0', "{'ID': 'A234', 'Gender': 'F', 'Age': '21', 'Sales': '001', "
                         "'BMI': 'Normal', 'Salary': '23', 'Birthday': '01/01/1996'}",
                         "{0: {'ID': 'A234', 'Gender': 'F', 'Age': '21', 'Sales': '001', 'BMI': 'Normal', "
                         "'Salary': '23', 'Birthday': '01/01/1996'}}"]
        with Capturing() as output:
            self.prompt.do_load('filehandler_tests/data.txt')
        self.assertEqual(output, self.expected)

    def test_quit(self):
        self.expected = ['Quitting ......']
        with Capturing() as output:
            result = self.prompt.do_quit("")
        self.assertEqual(output, self.expected)
        self.assertTrue(result)

    def test_pwd(self):
        self.expected = ['H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\'
                         'Interpreter\\Tests']
        with Capturing() as output:
            self.prompt.do_pwd("")
        self.assertEqual(output, self.expected)

    def test_save_nodata(self):
        self.expected = ["Please load data before attempting to save"]
        with Capturing() as output:
            self.prompt.do_save("")
        self.assertEqual(output, self.expected)

    def test_save_invalid(self):
        self.expected = ["invalid database type"]
        self.prompt.do_load('filehandler_tests/data.csv')
        with Capturing() as output:
            self.prompt.do_save("")
        self.assertEqual(output, self.expected)

    def test_save_local(self):
        self.expected = ".\\test"
        self.prompt.do_load('filehandler_tests/data.csv')
        user_input = ['test']
        with patch('builtins.input', side_effect=user_input):
            self.prompt.do_save("local")
        self.assertTrue(self.expected)

    def test_save_remote(self):
        self.expected = []
        self.prompt.do_load('filehandler_tests/data.csv')
        user_input = ['localhost', 'root', '', 'test']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_save("remote")
        self.assertEqual(output, self.expected)

    def test_graph_nodata(self):
        self.expected = ['Please set data before attempting to create a graph']
        with Capturing() as output:
            self.prompt.do_graph("pie, test")
        self.assertEqual(output, self.expected)

    def test_graph_nocriteria(self):
        self.expected = ['You have entered invalid criteria']
        self.prompt.do_load('filehandler_tests/data.csv')
        with Capturing() as output:
            self.prompt.do_graph("pie")
        self.assertEqual(output, self.expected)

    def test_graph_nofilename(self):
        self.expected = ['filename is invalid']
        self.prompt.do_load('filehandler_tests/data.csv')
        with Capturing() as output:
            self.prompt.do_graph("pie, test")
        self.assertEqual(output, self.expected)

    def test_graph(self):
        self.expected = ['pie',
                         'H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\'
                         'Interpreter\\Tests\\test.html']
        self.prompt.do_load('filehandler_tests/data.csv')
        user_input = ['Gender M', 'Salary Sales', 'GraphTitle']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_graph("pie test")
        self.assertEqual(output, self.expected)

    def test_graph_2(self):
        self.expected = ['pie',
                         'H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\'
                         'Interpreter\\Tests\\test.html']
        self.prompt.do_load('filehandler_tests/data.csv')
        user_input = ['Gender', 'Salary', 'Salary Sales GraphTitle']
        with Capturing() as output:
            with patch('builtins.input', side_effect=user_input):
                self.prompt.do_graph("pie test")
        self.assertEqual(output, self.expected)
