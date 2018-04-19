from unittest import TestSuite, TextTestRunner, makeSuite
from test_validator import TestValidator
from test_unpickle import TestUnpickler
from test_pickle import TestPickler
from test_database_remote import TestRemote
from test_database_local import TestLocal
from test_database_handler import TestDBHandler
from test_filehandler import TestFileHandler


def suite():
    testsuite = TestSuite()
    testsuite.addTest(makeSuite(TestValidator))
    testsuite.addTest(makeSuite(TestUnpickler))
    testsuite.addTest(makeSuite(TestPickler))
    testsuite.addTest(makeSuite(TestRemote))
    testsuite.addTest(makeSuite(TestLocal))
    testsuite.addTest(makeSuite(TestDBHandler))
    testsuite.addTest(makeSuite(TestFileHandler))
    return testsuite


if __name__ == '__main__':
    runner = TextTestRunner(verbosity=2)
    runner.run(suite())
