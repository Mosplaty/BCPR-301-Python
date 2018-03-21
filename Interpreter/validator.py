import re
from copy import deepcopy
from datetime import datetime, date


class Validator:
    def __init__(self):
        self.temp_dict = dict()
        self.valid_dict = dict()
        self.id = "^[A-Z][\d]{3}$"
        self.gender = "^(M|F)$"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.bmi = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(-|/)(0[1-9]|1[0-2])(-|/)(19|20)[0-9]{2}$"
        self.checks = ["id", "gender", "age", "sales", "bmi", "salary", "birthday"]
        self.invalid = {"gender": {"^((m|M)ale)$": "M", "^((f|F)emale)$": "F"}, "birthday": {"^(/|\\|.|:|;|,|_)$", '-'}}

    # Sales, ID, age, salary
    def check(self, attr, new_value):
        attr = attr.lower()
        an_attr = getattr(self, attr)
        a_value = str(new_value).title()
        match = re.match(an_attr, a_value)
        if match:
            result = a_value
        else:
            result = self.invalid_check(attr, a_value)
        return result

    # gender, birthday
    def invalid_check(self, attr, a_value):
        result = False
        for (key, value) in self.invalid.items():
            if key == attr:
                for (criteria, needed) in value.items():
                    match = re.match(criteria, a_value)
                    if attr == "birthday":
                        a_value.replace(criteria, needed)
                        result = a_value
                    elif match:
                            result = needed
        return result

    def checker(self, row):
        for (key, value) in row.items():
            for item in self.checks:
                if key.lower() == item:
                    valid = self.check(item, value)
                    if valid is not False:
                        self.temp_dict[item] = valid
                    else:
                        return False
        return True

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d-%m-%Y")

    @staticmethod
    def save_dict(loaded_dict):
        for empno, row in loaded_dict.items():
            b = a.checker(row)
            if b is False:
                print("Error at entry: " + str(empno))
            else:
                a.push_row(empno)
        return a.return_dict()

    def push_row(self, empno):
        print("Adding Row " + str(empno))
        temp = deepcopy(self.temp_dict)
        self.valid_dict[empno] = temp
        print(self.valid_dict[empno])

    def return_dict(self):
        return self.valid_dict


a = Validator()
