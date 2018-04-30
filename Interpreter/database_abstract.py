from abc import ABCMeta, abstractmethod


class DatabaseAbstract(metaclass=ABCMeta):
    def __init__(self):
        self.connection = None
        self.cursor = None

    @abstractmethod
    def connect(self):
        pass  # pragma: no cover

    @abstractmethod
    def create_table(self):
        pass  # pragma: no cover

    def drop_table(self):
        """Used for testing, will drop table to clear data"""
        self.cursor.execute("Drop table if exists employee")

    def insert_dictionary(self, dictionary):
        """Write a dictionary with key and pickled values
            into the database"""
        for key, value in dictionary.items():
            self.insert_record(value)

    def get_db(self):
        """Return the database"""
        self.cursor.execute("select empNo, personal from employee")
        return self.cursor.fetchall()

    def commit(self):
        """Changes to the database need to be committed to the database"""
        self.connection.commit()

    def close(self):
        """Close the connection after each crud operation with database"""
        self.connection.close()

    def query(self, sql):
        """Test query"""
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    @abstractmethod
    def insert_record(self, value):
        pass  # pragma: no cover

    @abstractmethod
    def delete_record(self, key):
        pass  # pragma: no cover

    @abstractmethod
    def update_record(self, key, value):
        pass  # pragma: no cover

