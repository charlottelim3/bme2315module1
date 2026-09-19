# Sophia Zhou # 
# Computing ID : ezy2hv #

import pandas as pd

df = pd.read_csv("/Users/sophiazhou/Desktop/BME2315/Module 1/bme2315module1/Metadata and Protein Data for Module 1.csv")

for column in df.columns:
    print(column)
