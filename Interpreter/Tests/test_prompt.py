from Interpreter.prompt import Shell
from unittest import TestCase
from unittest.mock import patch


def answer():
    result = input('Enter yes or no')
    if result == 'yes':
        return 'yes'
    if result == 'no':
        return 'no'
    else:
        return result


class TestPrompt(TestCase):

    def setUp(self):
        self.prompt = Shell()

    def tearDown(self):
        del self.prompt

    def test_tester(self):
        user_input = ['yes']
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(answer(), 'yes')

    def test_cd(self):
        expected = "H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\Interpreter"
        self.prompt.do_cd('..')
        result = self.prompt.directory
        user_input = [result]
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(answer(), expected)

    def test_load_csv(self):
        expected = "H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\Interpreter" \
                   "\\Tests\\filehandler_tests\\data.csv"
        self.prompt.do_load('filehandler_tests/data.csv')
        result = self.prompt.file
        user_input = [result]
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(answer(), expected)

    def test_load_xlsx(self):
        expected = "H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\Interpreter" \
                   "\\Tests\\filehandler_tests\\data.xlsx"
        self.prompt.do_load('filehandler_tests/data.xlsx')
        result = self.prompt.file
        user_input = [result]
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(answer(), expected)

    def test_load_txt(self):
        expected = "H:\\Documents\\Classes\\BCPR301 - Adv. Programming\\Assignment 2\\BCPR301_Assignment\\Interpreter" \
                   "\\Tests\\filehandler_tests\\data.txt"
        self.prompt.do_load('filehandler_tests/data.txt')
        result = self.prompt.file
        user_input = [result]
        with patch('builtins.input', side_effect=user_input):
            self.assertEqual(answer(), expected)
