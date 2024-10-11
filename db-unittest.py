#Script created by Jasleen Kaur

import unittest
import mysql.connector

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = mysql.connector.connect(
            user='krushith7',
            password='reddy@2000',
            host='localhost',
            database='firstdb'
        )
        self.cursor = self.conn.cursor()

    def tearDown(self):
        self.conn.close()

    def test_insert_employee(self):
        self.cursor.execute(
            "INSERT INTO Student (StudentId, Name, department) VALUES (3, 'Jasleen Kaur', 'ComputerScience')"
        )
        self.conn.commit()

        self.cursor.execute("SELECT * FROM Student WHERE StudentID = 2")
        result = self.cursor.fetchone()
        self.assertEqual(result[1], 'Jasleen Kaur')  # Check if the name matches

if __name__ == '__main__':
    unittest.main()
