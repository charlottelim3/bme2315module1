# Charlotte Lim (wfr2pj)

# %% view types of data in dataset
import pandas as pd

df = pd.read_csv("/Users/charlottelim/Library/CloudStorage/OneDrive-UniversityofVirginia/fall ‘26/bme 2315/module 1/bme2315module1/Metadata and Protein Data for Module 1.csv")
for header in df.columns:
    print(header)

# %%