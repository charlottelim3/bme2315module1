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
import pandas as pd
from sklearn.linear_model import LinearRegression

# # %% stats for bar plot (anova)
# abeta42_APOE_Genotype_2_3 = []
# abeta42_APOE_Genotype_3_3 = []
# abeta42_APOE_Genotype_3_4 = []
# abeta42_APOE_Genotype_4_4 = []
#
# for p in Patient.filter(Patient.all_patients, genotype = "2_3"): #create patient lists
#     abeta42_APOE_Genotype_2_3.append(p.abeta42)
# for p in Patient.filter(Patient.all_patients, genotype = "3_3"): #create patient lists
#     abeta42_APOE_Genotype_3_3.append(p.abeta42)
# for p in Patient.filter(Patient.all_patients, genotype = "3_4"): #create patient lists
#     abeta42_APOE_Genotype_3_4.append(p.abeta42)
# for p in Patient.filter(Patient.all_patients, genotype = "4_4"): #create patient lists
#     abeta42_APOE_Genotype_4_4.append(p.abeta42)
#
# # check for normality
# for name, group in zip(
#     ["2/3", "3/3", "3/4", "4/4"],
#     [abeta42_APOE_Genotype_2_3, abeta42_APOE_Genotype_3_3, abeta42_APOE_Genotype_3_4, abeta42_APOE_Genotype_4_4]
# ):
#     stat, p = stats.shapiro(group)
#     print(f"{name}: p = {p:.4f}") # not normal at all LOL
#     # 2/3: p = 0.0005 3/3: p = 0.0000 3/4: p = 0.0000 4/4: p = 0.0076
#
# # check for equal variance
# stat, p = stats.levene(abeta42_APOE_Genotype_2_3, abeta42_APOE_Genotype_3_3, abeta42_APOE_Genotype_3_4, abeta42_APOE_Genotype_4_4)
#
# print(f"Levene's test: p = {p:.4f}") #omg variances aren't different Levene's test: p = 0.2491
#
# # kruskal-wallis test
# stat, p = stats.kruskal(abeta42_APOE_Genotype_2_3, abeta42_APOE_Genotype_3_3, abeta42_APOE_Genotype_3_4, abeta42_APOE_Genotype_4_4)
#
# print(f"Kruskal-Wallis: H = {stat:.3f}, p = {p:.4f}")
# # results: Kruskal-Wallis: H = 15.127, p = 0.0017 groups are different with statistically significance at the 99% significance level!
#
# # %% BAR PLOT (apoe genotype x abeta42)
#
# x_2_3_bar = (statistics.mean(abeta42_APOE_Genotype_2_3)) # means
# x_3_3_bar = (statistics.mean(abeta42_APOE_Genotype_3_3)) # means
# x_3_4_bar = (statistics.mean(abeta42_APOE_Genotype_3_4)) # means
# x_4_4_bar = (statistics.mean(abeta42_APOE_Genotype_4_4)) # means
#
#
# abeta42_2_3_stdev = (statistics.stdev(abeta42_APOE_Genotype_2_3)) #standard devs
# abeta42_3_3_stdev = (statistics.stdev(abeta42_APOE_Genotype_3_3)) #standard devs
# abeta42_3_4_stdev = (statistics.stdev(abeta42_APOE_Genotype_3_4)) #standard devs
# abeta42_4_4_stdev = (statistics.stdev(abeta42_APOE_Genotype_4_4)) #standard devs
#
#
# genotype_cols = ['2/3', '3/3', '3/4','4/4'] # make graphs
# mean_genotype = [x_2_3_bar, x_3_3_bar, x_3_4_bar, x_4_4_bar]
# stdev_genotype = [abeta42_2_3_stdev, abeta42_3_3_stdev, abeta42_3_4_stdev, abeta42_4_4_stdev]
# yerr = [np.zeros(len(mean_genotype)), stdev_genotype]
#
# plt.bar(genotype_cols, mean_genotype, yerr=yerr, capsize=10, color=["blue", "orange", "purple", "red"]) # plot graphs
# plt.title("Average Amyloid-Beta 42 of APOE Genotypes")
# plt.xlabel("APOE Genotype")
# plt.ylabel("Average Amyloid-Beta 42 (pg/ug)")
# plt.text( # stats
#     0.5, 0.95,
#     f"Kruskal-Wallis: H = {stat:.3f}, p = {p:.4f}",
#     transform=plt.gca().transAxes,
#     ha="center")
# plt.show()


# %% SCATTER PLOT (yearsEd x abeta42)
patient_yearsEd = [] # lists
patient_abeta42 = []
# for p in Patient.all_patients: # add dogs to list
#     patient_yearsEd.append(p.yearsEd)
# for p in Patient.all_patients:
#     patient_abeta42.append(p.abeta42)

# remove outliers?
remove_list = []
for p in Patient.all_patients:
        if p.abeta42 < 0.031835158285 or p.abeta42 > 945.6276521849929:
            remove_list.append(p)
for p in remove_list:
        Patient.all_patients.remove(p)

for p in Patient.all_patients:
    patient_yearsEd.append(p.yearsEd)
    patient_abeta42.append(p.abeta42)

X = np.array(patient_yearsEd).reshape(-1, 1) # independent var
y = np.array(patient_abeta42)  # Dependent variable

model = LinearRegression() # linear regression
model.fit(X,y)
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR^2 = {r2:.2f}"
y_pred = model.predict(X)
plt.text(np.max(X), np.max(y), equation, color="red", fontsize=12, horizontalalignment='center', verticalalignment='top')

plt.scatter(X, y, color='purple') # plots plot
plt.plot(X, y_pred, color="red")
plt.xlabel('Years of Education')
plt.ylabel('Amyloid-Beta 42 (pg/ug)')
plt.title('Years of Education vs Amyloid-Beta 42')
plt.show() # one outlier-- get rid of for project?

# %% testing for outliers
# # using interquartile regions (basic from stats)
# Q1 = np.percentile(patient_abeta42, 25)
# Q3 = np.percentile(patient_abeta42, 75)
#
# IQR = Q3 - Q1

# lower_bound = Q1 - 2.7 * IQR # flags for 1% extreme outliers
# upper_bound = Q3 + 2.7 * IQR

# for directly top 0.5% and 99.5%:
lower_bound = np.percentile(patient_abeta42, 0.5)
upper_bound = np.percentile(patient_abeta42, 99.5)

outliers = [
    x for x in patient_abeta42
    if x < lower_bound or x > upper_bound
]
# for aB42 levels
print("Lower bound:", lower_bound) # -95.739736845625
print("Upper bound:", upper_bound) # 177.491842111375
print("Outliers:", outliers)
# results:
# Lower bound: 0.031835158285
# Upper bound: 945.6276521849929
# Outliers: [1412.566961, 0.019621053]