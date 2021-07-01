"""System module"""
import unittest
import pandas as pd

from src.read_csv_data import read_csv


class TestForReadCsv(unittest.TestCase):
    """the test class for reading csv files"""
    def test_for_csv(self):
        """test function for reading csv files"""
        self.assertIsInstance(read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/'
                                       'intelligent_system_data''/main/'
                                       'Intelligent%20System%20Data/CSP/'
                                       'CSP_360.csv'), pd.DataFrame)
