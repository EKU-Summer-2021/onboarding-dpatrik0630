"""System module"""
import pandas as pd


def read_csv(source):
    """CSV file reading function"""
    print(pd.read_csv(source))
    return pd.read_csv(source)
