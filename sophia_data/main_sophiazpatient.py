# Sophia Zhou (ID: ezy2hv)#

from patient_Sophia import *
import matplotlib.pyplot as plt
import numpy as np
import statistics


# 1. class defined (check)


# 2. Constructor (__init__) objects (check)
# Constructor id in patient_Sophia.py


# 3. created representor (__repr__) (check)
# Representor is in patient_Sophia.py


# 4. patient objects created from the csv file (check)

Patient.instantiate_from_csv(
    "/Users/sophiazhou/Desktop/BME2315/Module_1/Module1_Patient practice data /Metadata and Protein Data for Module 1.csv"
)

print("\nNumber of patients = ")
print(len(Patient.all_patients))


# 5. sort by attribute
# sort by years of education 

print("\nPatients sorted by years of education:")

Patient.all_patients.sort(
    key=lambda x: x.years_of_education if x.years_of_education is not None else 0,
    reverse=False
)

for patient in Patient.all_patients:
    print(patient)


# 6. from patient_Sophia import *
import matplotlib.pyplot as plt
import numpy as np
import statistics


# 1. class defined (check)
# Patient class is defined in patient_Sophia.py


# 2. Constructor (__init__) objects (check)
# Constructor is defined in patient_Sophia.py


# 3. created representor (__repr__) (check)
# Representor is defined in patient_Sophia.py


# 4. patient objects created from the csv file (check)

Patient.instantiate_from_csv(
    "/Users/sophiazhou/Desktop/BME2315/Module_1/Module1_Patient practice data /Metadata and Protein Data for Module 1.csv"
)

print("\nNumber of patients = ")
print(len(Patient.all_patients))


# 5. sort by attribute
# sort by years of education and print all listed patients

print("\nPatients sorted by years of education:")

Patient.all_patients.sort(
    key=lambda x: x.years_of_education if x.years_of_education is not None else 0,
    reverse=False
)

for patient in Patient.all_patients:
    print(patient)


# 6. filter and print subset using 2 attributes

print("\nFemale patients with dementia:")

filtered_patients = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)

for patient in filtered_patients:
    print(patient)


# 7. making my bar graph for the mean of
# Amyloid-Beta42 between female and male patients with dementia

abeta42_Female = []
abeta42_Male = []


for patient in Patient.filter(
    Patient.all_patients,
    cognitive_status="Dementia"
):

    if patient.sex == "Female" and patient.abeta42 is not None:
        abeta42_Female.append(patient.abeta42)


for patient in Patient.filter(
    Patient.all_patients,
    cognitive_status="Dementia"
):

    if patient.sex == "Male" and patient.abeta42 is not None:
        abeta42_Male.append(patient.abeta42)


# define the bars for bar graph

x_Female_bar = statistics.mean(abeta42_Female)
x_Male_bar = statistics.mean(abeta42_Male)

abeta42_Female_stdev = statistics.stdev(abeta42_Female)
abeta42_Male_stdev = statistics.stdev(abeta42_Male)


# define standard deviations

print(
    f'x_Female_bar = {x_Female_bar}, '
    f'abeta42_Female_stdev = {abeta42_Female_stdev}'
)

print(
    f'x_Male_bar = {x_Male_bar}, '
    f'abeta42_Male_stdev = {abeta42_Male_stdev}'
)


# bar graph

Patient_sex_cols = ['Female', 'Male']

mean_sex = [
    x_Female_bar,
    x_Male_bar
]

stdev_sex = [
    abeta42_Female_stdev,
    abeta42_Male_stdev
]

yerr = [
    np.zeros(len(mean_sex)),
    stdev_sex
]


# plot and show the bar graph

plt.bar(
    Patient_sex_cols,
    mean_sex,
    yerr=yerr,
    capsize=10
)

plt.title("Average Amyloid-Beta42 Levels in Dementia Patients")
plt.xlabel("Sex")
plt.ylabel("Average Amyloid-Beta42 (pg/ug)")
plt.show()


# 8. make scatter plot
# comparing patient attributes

patient_age = []
patient_abeta42 = []


for patient in Patient.all_patients:

    if patient.age is not None and patient.abeta42 is not None:

        patient_age.append(patient.age)
        patient_abeta42.append(patient.abeta42)


# define independent variable

X = patient_age
y = patient_abeta42


# how to visualize the data

# plt.scatter(X, y)

# plt.xlabel('Age at Death')
# plt.ylabel('Amyloid-Beta42 (pg/ug)')
# plt.title('Scatter Plot of Age at Death vs Amyloid-Beta42')
# plt.show()

print("\nFemale patients with dementia:")

filtered_patients = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)

for patient in filtered_patients:
    print(patient)


# 7. making my bar graph for the mean of
# Amyloid-Beta42 between female and male patients with dementia

abeta42_Female = []
abeta42_Male = []


for patient in Patient.filter(
    Patient.all_patients,
    cognitive_status="Dementia"
):

    if patient.sex == "Female" and patient.abeta42 is not None:
        abeta42_Female.append(patient.abeta42)


for patient in Patient.filter(
    Patient.all_patients,
    cognitive_status="Dementia"
):

    if patient.sex == "Male" and patient.abeta42 is not None:
        abeta42_Male.append(patient.abeta42)


# define the bars for bar graph

x_Female_bar = statistics.mean(abeta42_Female)
x_Male_bar = statistics.mean(abeta42_Male)

abeta42_Female_stdev = statistics.stdev(abeta42_Female)
abeta42_Male_stdev = statistics.stdev(abeta42_Male)


# define standard deviations

print(
    f'x_Female_bar = {x_Female_bar}, '
    f'abeta42_Female_stdev = {abeta42_Female_stdev}'
)

print(
    f'x_Male_bar = {x_Male_bar}, '
    f'abeta42_Male_stdev = {abeta42_Male_stdev}'
)


# bar graph

Patient_sex_cols = ['Female', 'Male']

mean_sex = [
    x_Female_bar,
    x_Male_bar
]

stdev_sex = [
    abeta42_Female_stdev,
    abeta42_Male_stdev
]

yerr = [
    np.zeros(len(mean_sex)),
    stdev_sex
]


# plot and show the bar graph

plt.bar(
    Patient_sex_cols,
    mean_sex,
    yerr=yerr,
    capsize=10
)

plt.title("Average Amyloid-Beta42 Levels in Dementia Patients")
plt.xlabel("Sex")
plt.ylabel("Average Amyloid-Beta42 (pg/ug)")
plt.show()


# 8. make scatter plot
# comparing patient attributes

patient_age = []
patient_abeta42 = []


for patient in Patient.all_patients:

    if patient.age is not None and patient.abeta42 is not None:

        patient_age.append(patient.age)
        patient_abeta42.append(patient.abeta42)


# define independent variable

X = patient_age
y = patient_abeta42


# how to visualize the data

plt.scatter(X, y)

plt.xlabel('Age at Death')
plt.ylabel('Amyloid-Beta42 (pg/ug)')
plt.title('Scatter Plot of Age at Death vs Amyloid-Beta42')
plt.show()