# Charlotte Lim (wfr2pj)

# %% patient class
from patient import *

Patient.instantiate_from_csv("/Users/charlottelim/Library/CloudStorage/OneDrive-UniversityofVirginia/fall ‘26/bme 2315/module 1/bme2315module1/Metadata and Protein Data for Module 1.csv")

# %% patient plots
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics
from sklearn.linear_model import LinearRegression

# %% stats for bar plot (anova)
# Highest level of education vs. age of symptoms onset
high_school_ageSym = []
trade_school_ageSym = []
bachelors_ageSym = []
grad_school_ageSym = []
Patient.all_patients_symptomatic = [ p for p in Patient.all_patients if p.ageofSym is not None ] # removing null age of symptoms patients

for p in Patient.filter(Patient.all_patients_symptomatic, highestEd = "High School"): #create patient lists
    high_school_ageSym.append(p.ageofSym)
for p in Patient.filter(Patient.all_patients_symptomatic, highestEd = "Trade School/ Tech School"): #create patient lists
    trade_school_ageSym.append(p.ageofSym)
for p in Patient.filter(Patient.all_patients_symptomatic, highestEd = "Bachelors"): #create patient lists
    bachelors_ageSym.append(p.ageofSym)
for p in Patient.filter(Patient.all_patients_symptomatic, highestEd = "Graduate (PhD/Masters)"): #create patient lists
    grad_school_ageSym.append(p.ageofSym)
for p in Patient.filter(Patient.all_patients_symptomatic, highestEd = "Professional"): #create patient lists
    grad_school_ageSym.append(p.ageofSym)

print("High School:", len(high_school_ageSym), high_school_ageSym)
print("Trade School:", len(trade_school_ageSym), trade_school_ageSym)
print("Bachelors:", len(bachelors_ageSym), bachelors_ageSym)
print("Graduate:", len(grad_school_ageSym), grad_school_ageSym)
# check for normality
for name, group in zip(
    ["High School", "Trade School", "Bachelors", "Graduate School"],
    [high_school_ageSym, trade_school_ageSym, bachelors_ageSym, grad_school_ageSym]
):
    stat, p = stats.shapiro(group)
    print(f"{name}: p = {p:.4f}") #
    # High School: p = 0.0455 -> not normally distributed
    # Trade School: p = 0.0677 -> is normally distributed
    # Bachelors: p = 0.0101 -> not normally distributed
    # Graduate School: p = 0.1089 -> is normally distributed

# check for equal variance
stat, p = stats.levene(high_school_ageSym, trade_school_ageSym, bachelors_ageSym, grad_school_ageSym)

print(f"Levene's test: p = {p:.4f}") #omg variances aren't different Levene's test: p = 0.9568

# kruskal-wallis test (non parametric since data is not normally distributed)
stat, p = stats.kruskal(high_school_ageSym, trade_school_ageSym, bachelors_ageSym, grad_school_ageSym)
print(f"Kruskal-Wallis: H = {stat:.3f}, p = {p:.4f}")
# results: Kruskal-Wallis: H = 3.115, p = 0.3743
# groups are NOT different  at the 90% significance level

# %% BAR PLOT (highestEd v age of symptoms)

x_hs_bar = (statistics.mean(high_school_ageSym)) # means
x_trades_bar = (statistics.mean(trade_school_ageSym)) # means
x_bs_bar = (statistics.mean(bachelors_ageSym)) # means
x_grads_bar = (statistics.mean(grad_school_ageSym)) # means


hs_stdev = (statistics.stdev(high_school_ageSym)) #standard devs
trades_stdev = (statistics.stdev(trade_school_ageSym)) #standard devs
bs_stdev = (statistics.stdev(bachelors_ageSym)) #standard devs
grads_stdev = (statistics.stdev(grad_school_ageSym)) #standard devs


genotype_cols = ['High School', 'Trade School', 'Bachelors','Graduate School'] # make graphs
mean_genotype = [x_hs_bar, x_trades_bar, x_bs_bar, x_grads_bar]
stdev_genotype = [hs_stdev, trades_stdev, bs_stdev, grads_stdev]
yerr = stdev_genotype

plt.bar(genotype_cols, mean_genotype, yerr=yerr, capsize=10, color=["blue", "orange", "purple", "red"]) # plot graphs
plt.title("Age of Cognitive Symptoms Onset for Highest Level of Education Groups")
plt.xlabel("Highest Level of Education")
plt.ylabel("Age of Cognitive Symptoms Onset")
plt.text( # stats
    0.5, 0.95,
    f"Kruskal-Wallis: H = {stat:.3f}, p = {p:.4f}",
    transform=plt.gca().transAxes,
    ha="center")
plt.show()
#
#
# %% SCATTER PLOT (yearsEd x abeta42)
patient_yearsEd = [] # lists
patient_abeta42 = []

# removing outliers
remove_list = []
for p in Patient.all_patients:
        if p.abeta42 < 0.031835158285 or p.abeta42 > 945.6276521849929:
            remove_list.append(p)
for p in remove_list:
        Patient.all_patients.remove(p)

# add patients (non-outliers) to lists
for p in Patient.all_patients:
    patient_yearsEd.append(p.yearsEd)
    patient_abeta42.append(p.abeta42)

X = np.array(patient_yearsEd).reshape(-1, 1) # independent var
y = np.array(patient_abeta42)  # dependent variable

model = LinearRegression() # linear regression
model.fit(X,y)
slope = model.coef_[0]
intercept = model.intercept_
r2 = model.score(X, y)
equation = f"y = {slope:.2f}x + {intercept:.2f}\nR^2 = {r2:.2f}"
y_pred = model.predict(X)
plt.text(0.5, 0.98, equation, transform=plt.gca().transAxes, color="red", fontsize=12, horizontalalignment='center', verticalalignment='top')

plt.scatter(X, y, color='blue') # plots plot
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

# for directly bottom 0.5% and top 99.5%:
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