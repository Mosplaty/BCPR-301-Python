from Interpreter.database_local import DBLocal
from unittest import TestCase


class TestLocal(TestCase):
    def setUp(self):
        self.db = DBLocal()
        self.db.connect("testing")
        self.db.create_table()

    def tearDown(self):
        self.db.drop_table()
        self.db.close()
        self.db = None

    def test_db_insert_values(self):
        """
        Create a table, insert data and check the return data is what was inserted
        """
        expected = [(1, 'dskjhflkasdjlfkj23543'), (2, 'dskjhflkasdjlasdfdsafkj23543')]
        self.db.insert_record('dskjhflkasdjlfkj23543')
        self.db.insert_record('dskjhflkasdjlasdfdsafkj23543')
        self.db.commit()
        result = self.db.get_db()
        self.assertEqual(expected, result)

    def test_db_get(self):
        """
        Getting an empty database
        """
        expected = list()
        result = self.db.get_db()
        self.assertEqual(expected, result)

    def test_db_insert_dict(self):
        """
        Insert a dictionary into the database
        """
        expected = [(1, 'dskjhflkasdjlfkj23543'), (2, 'dskjhflkasdjlasdfdsafkj23543')]
        data = {1: 'dskjhflkasdjlfkj23543', 2: 'dskjhflkasdjlasdfdsafkj23543'}
        self.db.insert_dictionary(data)
        result = self.db.get_db()
        self.assertEqual(expected, result)

    def test_db_update(self):
        """
        Update an existing database entry
        """
        expected = [(1, 'dskjhflkasdjlfkj2354'), (2, 'dskjhflkasdjlasdfdsafkj23543')]
        data = {1: 'dskjhflkasdjlfkj23543', 2: 'dskjhflkasdjlasdfdsafkj23543'}
        self.db.insert_dictionary(data)
        self.db.update_record('1', 'dskjhflkasdjlfkj2354')
        result = self.db.get_db()
        self.assertEqual(result, expected)

    def test_db_delete(self):
        """
        Delete an existing database entry
        """
        expected = [(1, 'dskjhflkasdjlfkj23543')]
        data = {1: 'dskjhflkasdjlfkj23543', 2: 'dskjhflkasdjlasdfdsafkj23543'}
        self.db.insert_dictionary(data)
        self.db.delete_record('2')
        result = self.db.get_db()
        self.assertEqual(expected, result)

    def test_abstract_query(self):
        expected = []
        data = "Select * from employee"
        result = self.db.query(data)
        self.assertEqual(result, expected)
