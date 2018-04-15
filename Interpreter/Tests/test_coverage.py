from coverage import Coverage
from Tests.test_validator import TestValidator

cov = Coverage()
cov.start()

# code here

v = TestValidator()
v.test_valid_data()
v.test_invalid_value_ID()
v.test_invalid_value_gen()
v.test_invalid_value_age()
v.test_invalid_value_sales()
v.test_invalid_value_bmi()
v.test_invalid_value_salary()
v.test_invalid_value_birthday()
v.test_invalid_key_ID()
v.test_invalid_key_gen()
v.test_invalid_key_age()
v.test_invalid_key_sales()
v.test_invalid_key_bmi()
v.test_invalid_key_salary()
v.test_invalid_key_birthday()

cov.stop()
cov.html_report(directory='coverage_report')
