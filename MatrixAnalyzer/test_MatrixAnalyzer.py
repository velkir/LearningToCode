import unittest
import tempfile
from MatrixAnalyzer import MatrixAnalyzer
import csv
import os
import random
import string
import numpy as np


class TestLoadCSV(unittest.TestCase):
    def setUp(self):
        self.matrixAnalyzer = MatrixAnalyzer()
        self.temp_file_numeric = self._create_numeric_csv_file()
        self.temp_file_non_numeric = self._create_non_numeric_csv_file()
    def _create_numeric_csv_file(self):
        numeric_data = [["col1", "col2", "col3"],
                        [1, 2, 3],
                        [4, 5, 6],
                        [4, 5, 6],
                        [4, 5, 8]]
        temp = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv')
        writer = csv.writer(temp)
        writer.writerows(numeric_data)
        temp.close()
        if temp:
            return temp
        else:
            raise ValueError

    def _create_non_numeric_csv_file(self):
        non_numeric_data = [["col1", "col2", "col3"],
                            [1, 2, 3],
                            [1, 2, 3],
                            [4, "qeq", 6],
                            [4, 5, "asd"]
                            ]
        temp = tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix='.csv')
        writer = csv.writer(temp)
        writer.writerows(non_numeric_data)
        temp.close()
        if temp:
            return temp
        else:
            raise ValueError

    def _generate_random_csv_path(self, length=15):
        characters = string.ascii_lowercase + string.digits
        name = ''.join(random.choices(characters, k=length))
        return f"{name}.csv"

    def test_incorrect_path(self):
        incorrect_path = "asdasgadsfqfascxvasdqfacascnqodsqa.csv"
        with self.assertRaises(FileNotFoundError):
            self.matrixAnalyzer.load_csv(incorrect_path)

    def test_numeric_data_loading(self):
        self.assertEqual(self.matrixAnalyzer.load_csv(self.temp_file_numeric.name, skip_header=1), 1)

    def test_non_numeric_data_not_loading(self):
        with self.assertRaises(ValueError):
            self.matrixAnalyzer.load_csv(self.temp_file_non_numeric.name, skip_header=1)

    def tearDown(self):
        os.unlink(self.temp_file_numeric.name)
        os.unlink(self.temp_file_non_numeric.name)


class TestComputing(unittest.TestCase):
    def setUp(self):
        self.matrixAnalyzer = MatrixAnalyzer()
        self.temp_file_computing = self._create_computing_csv_file()
        self.matrixAnalyzer.load_csv(self.temp_file_computing.name, skip_header=1)

    def _create_computing_csv_file(self):
        comp_file = tempfile.NamedTemporaryFile(mode="w+",
                                                delete=False,
                                                suffix=".csv")
        comp_data = [
            ["col1", "col2", "col3"],
            [49, 71, 99, 40, 5],
            [45, 34, 5, 56, 23],
            [77, 68, 11, 14, 72],
            [25, 31, 51, 12, 95],
            [79, 63, 10, 20, 49]
        ]
        writer = csv.writer(comp_file)
        writer.writerows(comp_data)
        comp_file.close()
        if comp_file:
            return comp_file
        else:
            raise ValueError

    def test_compute_eigenvalues(self):
        self.assertEqual(self.matrixAnalyzer.compute_eigenvalues()[0][0],
                         np.linalg.eig(self.matrixAnalyzer.data)[0][0])

    def test_range_of_values(self):
        self.assertEqual(self.matrixAnalyzer.compute_range_of_values(), 94.0)

    def test_compute_median(self):
        self.assertEqual(self.matrixAnalyzer.compute_median(), 45.0)

    def test_compute_std(self):
        self.assertEqual(self.matrixAnalyzer.compute_std(), 27.93375019577572)

    def test_compute_variance(self):
        self.assertEqual(self.matrixAnalyzer.compute_variance(), 780.2944)


if __name__ == '__main__':
    unittest.main()