import unittest
import pandas as pd

from src.read_csv_data import read_csv

class readTest(unittest.TestCase):
    def test_for_csv(self):
        self.assertIsInstance(read_csv('https://raw.githubusercontent.com/EKU-Summer-2021/intelligent_system_data'
                                       '/main/Intelligent%20System%20Data/CSP/CSP_360.csv'), pd.DataFrame)



