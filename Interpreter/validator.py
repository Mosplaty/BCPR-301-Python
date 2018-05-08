import re
from copy import deepcopy
from abc import ABCMeta, abstractmethod
from datetime import datetime, date


class Validator:
    def __init__(self):
        self.temp_dict = dict()
        self.valid_dict = dict()
        self.empid = "^[A-Z][\d]{3}$"
        self.gender = "^(M|F)$"
        self.age = "^[\d]{2}$"
        self.sales = "^[\d]{3}$"
        self.BMI = "^(Normal|Overweight|Obesity|Underweight)$"
        self.salary = "^([\d]{2}|[\d]{3})$"
        self.birthday = "^(0[1-9]|[1-2][0-9]|3(0|1))(-|/)(0[1-9]|1[0-2])(-|/)(19|20)[0-9]{2}$"

    def check_empid(self, new_empid):
        """
        Checks the empid matches validation rules
        :param new_empid:
        :return:
        >>> v = Validator()
        >>> v.check_empid("A123")
        'A123'
        """
        match = re.match(self.empid, new_empid)
        if match:
            return new_empid
        else:
            new_empid = False
            return new_empid

    def check_gender(self, new_gender):
        """
        Checks the gender matches validation rules
        :param new_gender:
        :return:
        >>> v = Validator()
        >>> v.check_gender("M")
        'M'
        """
        match = re.match(self.gender, new_gender)
        if match:
            return new_gender
        else:
            match = re.match("^((m|M)ale)$", new_gender)
            if match:
                new_gender = "M"
                return new_gender
            fmatch = re.match("^((f|F)emale)$", new_gender)
            if fmatch:
                new_gender = "F"
                return new_gender
            new_gender = False
            return new_gender

    def check_age(self, new_age):
        """
        Checks the age matches validation rules
        :param new_age:
        :return:
        >>> v = Validator()
        >>> v.check_age("24")
        '24'
        """
        new_age = str(new_age)
        match = re.match(self.age, new_age)
        if match:
            return new_age
        else:
            new_age = False
            return new_age

    def check_sales(self, new_sales):
        """
        Checks the sales matches validation rules
        :param new_sales:
        :return:
        >>> v = Validator()
        >>> v.check_sales('20')
        False
        """
        new_sales = str(new_sales)
        match = re.match(self.sales, new_sales)
        if match:
            return new_sales
        else:
            new_sales = False
            return new_sales

    def check_BMI(self, new_BMI):
        """
        Checks the BMI matches validation rules
        :param new_BMI:
        :return:
        >>> v = Validator()
        >>> v.check_BMI("normal")
        'Normal'
        """
        match = re.match(self.BMI, new_BMI)
        if match:
            return new_BMI
        else:
            match = re.match("^(normal|overweight|obesity|underweight)$", new_BMI)
            if match:
                new_BMI = new_BMI.capitalize()
                return new_BMI
            new_BMI = False
            return new_BMI

    def check_salary(self, new_salary):
        new_salary = str(new_salary)
        match = re.match(self.salary, new_salary)
        if match:
            return new_salary
        else:
            new_salary = False
            return new_salary

    @staticmethod
    def xlsx_date(a_date):
        return a_date.date().strftime("%d/%m/%Y")

    def check_birthday(self, new_birthday):
        invalid_delims = "^(|\\.:;,_)$"
        for i in invalid_delims:
            new_birthday = new_birthday.replace(i, '/')
        match = re.match(self.birthday, new_birthday)
        if match:
            return new_birthday
        else:
            new_birthday = False
            return new_birthday

    @staticmethod
    def checker(row):
        result = True
        for key, value in row.items():
            value = str(value)
            checker_keys = {'ID': a.check_empid(value),
                            'Gender': a.check_gender(value),
                            'Age': a.check_age(value),
                            'Sales': a.check_sales(value),
                            'BMI': a.check_BMI(value),
                            'Salary': a.check_salary(value),
                            'Birthday': a.check_birthday(value)
                            }
            if key == "ID":
                if a.check_empid(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_empid(value))
            elif key == "Gender":
                if a.check_gender(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_gender(value))
            elif key == "Age":
                if a.check_age(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_age(value))
            elif key == "Sales":
                if a.check_sales(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_sales(value))
            elif key == "BMI":
                if a.check_BMI(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_BMI(value))
            elif key == "Salary":
                if a.check_salary(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_salary(value))
            elif key == "Birthday":
                if a.check_birthday(value) is False:
                    result = False
                    return result
                else:
                    a.push_value(key, a.check_birthday(value))
            else:
                result = False
                return result

    @staticmethod
    def save_dict(loaded_dict):
        for empno, row in loaded_dict.items():
            b = a.checker(row)
            if b is False:
                print("Error at entry: " + str(empno))
            else:
                a.push_row(empno)
        return a.return_dict()

    def push_value(self, key, val):
        self.temp_dict[key] = val

    def push_row(self, empno):
        print("Adding Row " + str(empno))
        temp = deepcopy(self.temp_dict)
        self.valid_dict[empno] = temp
        print(self.valid_dict[empno])

    def return_dict(self):
        return self.valid_dict


a = Validator()
