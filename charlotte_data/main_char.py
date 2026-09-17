# Charlotte Lim (wfr2pj)

# # %% view types of data in dataset
# import pandas as pd
#
# df = pd.read_csv("/Users/charlottelim/Library/CloudStorage/OneDrive-UniversityofVirginia/fall ‘26/bme 2315/module 1/bme2315module1/Metadata and Protein Data for Module 1.csv")
# for header in df.columns:
#     print(header)

# %% patient class
from patient import *

Patient.instantiate_from_csv("/Users/charlottelim/Library/CloudStorage/OneDrive-UniversityofVirginia/fall ‘26/bme 2315/module 1/bme2315module1/Metadata and Protein Data for Module 1.csv")
# sort by years of Education and abeta42, & print all patients
# Patient.all_patients.sort(key=lambda patient: (patient.yearsEd, patient.abeta42), reverse=False)
# for patient in Patient.all_patients:
#     print(patient)
# # filter for dementia and APOE 4/4
# dementia_patients = Patient.filter(Patient.all_patients, cogStat = "Dementia", genotype = "4_4")
# print(f'Number of Patients with Dementia and APOE 4/4: {len(dementia_patients)}') # print num
# for patient in dementia_patients: # print patients
#     print(patient)

# %% patient plots
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics

# %% stats for bar plot (anova)
abeta42_APOE_Genotype_2_3 = []
abeta42_APOE_Genotype_3_3 = []
abeta42_APOE_Genotype_3_4 = []
abeta42_APOE_Genotype_4_4 = []

for p in Patient.filter(Patient.all_patients, genotype = "2_3"): #create patient lists
    abeta42_APOE_Genotype_2_3.append(p.abeta42)
for p in Patient.filter(Patient.all_patients, genotype = "3_3"): #create patient lists
    abeta42_APOE_Genotype_3_3.append(p.abeta42)
for p in Patient.filter(Patient.all_patients, genotype = "3_4"): #create patient lists
    abeta42_APOE_Genotype_3_4.append(p.abeta42)
for p in Patient.filter(Patient.all_patients, genotype = "4_4"): #create patient lists
    abeta42_APOE_Genotype_4_4.append(p.abeta42)
    
# check for normality
for name, group in zip(
    ["2/3", "3/3", "3/4", "4/4"],
    [abeta42_APOE_Genotype_2_3, abeta42_APOE_Genotype_3_3, abeta42_APOE_Genotype_3_4, abeta42_APOE_Genotype_4_4]
):
    stat, p = stats.shapiro(group)
    print(f"{name}: p = {p:.4f}") # not normal at all LOL
    # 2/3: p = 0.0005 3/3: p = 0.0000 3/4: p = 0.0000 4/4: p = 0.0076

# check for equal variance
stat, p = stats.levene(abeta42_APOE_Genotype_2_3, abeta42_APOE_Genotype_3_3, abeta42_APOE_Genotype_3_4, abeta42_APOE_Genotype_4_4)

print(f"Levene's test: p = {p:.4f}") #omg variances aren't different Levene's test: p = 0.2491

# kruskal-wallis test
stat, p = stats.kruskal(abeta42_APOE_Genotype_2_3, abeta42_APOE_Genotype_3_3, abeta42_APOE_Genotype_3_4, abeta42_APOE_Genotype_4_4)

print(f"Kruskal-Wallis: H = {stat:.3f}, p = {p:.4f}")
# results: Kruskal-Wallis: H = 15.127, p = 0.0017 groups are statistically significant at the 95% significance level!

# %% BAR PLOT (apoe genotype x abeta42)

x_2_3_bar = (statistics.mean(abeta42_APOE_Genotype_2_3)) # means
x_3_3_bar = (statistics.mean(abeta42_APOE_Genotype_3_3)) # means
x_3_4_bar = (statistics.mean(abeta42_APOE_Genotype_3_4)) # means
x_4_4_bar = (statistics.mean(abeta42_APOE_Genotype_4_4)) # means


abeta42_2_3_stdev = (statistics.stdev(abeta42_APOE_Genotype_2_3)) #standard devs
abeta42_3_3_stdev = (statistics.stdev(abeta42_APOE_Genotype_3_3)) #standard devs
abeta42_3_4_stdev = (statistics.stdev(abeta42_APOE_Genotype_3_4)) #standard devs
abeta42_4_4_stdev = (statistics.stdev(abeta42_APOE_Genotype_4_4)) #standard devs


genotype_cols = ['2/3', '3/3', '3/4','4/4'] # make graphs
mean_genotype = [x_2_3_bar, x_3_3_bar, x_3_4_bar, x_4_4_bar]
stdev_genotype = [abeta42_2_3_stdev, abeta42_3_3_stdev, abeta42_3_4_stdev, abeta42_4_4_stdev]
yerr = [np.zeros(len(mean_genotype)), stdev_genotype]

plt.bar(genotype_cols, mean_genotype, yerr=yerr, capsize=10, color=["blue", "orange", "purple", "red"]) # plot graphs
plt.title("Average Amyloid-Beta 42 of APOE Genotypes")
plt.xlabel("APOE Genotype")
plt.ylabel("Average Amyloid-Beta 42 (pg/ug)")
plt.text( # stats
    0.5, 0.95,
    f"Kruskal-Wallis: H = {stat:.3f}, p = {p:.4f}",
    transform=plt.gca().transAxes,
    ha="center")
plt.show()


#%% SCATTER PLOT (yearsEd x abeta42)
# patient_yearsEd = [] # lists
# patient_abeta42 = []
# for p in Patient.all_patients: # add dogs to list
#     patient_yearsEd.append(p.yearsEd)
# for p in Patient.all_patients:
#     patient_abeta42.append(p.abeta42)
# X = [patient_yearsEd]  # Independent variable
# y = [patient_abeta42]   # Dependent variable
# plt.scatter(X, y, color='purple') # plots plot
# plt.xlabel('Years of Education')
# plt.ylabel('Amyloid-Beta 42 (pg/ug)')
# plt.title('Years of Education vs Amyloid-Beta 42')
# plt.show() # one outlier-- get rid of for project?