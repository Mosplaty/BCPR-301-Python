from unittest import TestSuite, TextTestRunner, makeSuite
from test_validator import TestValidator


def suite():
    testsuite = TestSuite()
    testsuite.addTest(makeSuite(TestValidator))
    return testsuite


if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())
