from coverage import Coverage
from Tests.test_validator import TestValidator

cov = Coverage()
cov.start()

# code here

v = TestValidator()

cov.stop()
cov.html_report(directory='coverage_report')
