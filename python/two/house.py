#!/usr/bin/python
import pandas as pd

def load_house_data():
    path='./datasets/housing/housing.csv'
    return pd.read_csv(path)




housing=load_house_data()
housing.head()
