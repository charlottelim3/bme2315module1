import csv


class Patient:
    all_patients = []

    def __init__(
        self,
        patient_id: str,
        age: int,
        sex: str,
        years_of_education: int,
        apoe_genotype: str,
        cognitive_status: str,
        age_onset: float,
        casi: float,
        mmse: float,
        moca: float,
        abeta40: float,
        abeta42: float,
        ttau: float,
        ptau: float
    ):

        self.patient_id = patient_id
        self.age = age
        self.sex = sex
        self.years_of_education = years_of_education
        self.apoe_genotype = apoe_genotype
        self.cognitive_status = cognitive_status
        self.age_onset = age_onset
        self.casi = casi
        self.mmse = mmse
        self.moca = moca
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self)


    def __repr__(self):
        return f"{self.patient_id}: ({self.age} | {self.sex} | {self.years_of_education} | {self.cognitive_status} | {self.age_onset})"


    def get_education(self):
        return self.years_of_education


    @classmethod
    def get_genotype(cls, genotype):
        for patient in Patient.all_patients:
            if genotype == patient.apoe_genotype:
                return patient


    @classmethod
    def instantiate_from_csv(cls, filename: str):

        with open(filename, newline="") as f:
            reader = csv.DictReader(f)

            for row in reader:

                # Convert blank values into None
                age = int(row['Age at Death']) if row['Age at Death'] else None

                years_of_education = int(row['Years of education']) if row['Years of education'] else None

                age_onset = float(row['Age of onset cognitive symptoms']) if row['Age of onset cognitive symptoms'] else None

                casi = float(row['Last CASI Score']) if row['Last CASI Score'] else None

                mmse = float(row['Last MMSE Score']) if row['Last MMSE Score'] else None

                moca = float(row['Last MOCA Score']) if row['Last MOCA Score'] else None

                abeta40 = float(row['ABeta40 pg/ug']) if row['ABeta40 pg/ug'] else None

                abeta42 = float(row['ABeta42 pg/ug']) if row['ABeta42 pg/ug'] else None

                ttau = float(row['tTAU pg/ug']) if row['tTAU pg/ug'] else None

                ptau = float(row['pTAU pg/ug']) if row['pTAU pg/ug'] else None


                Patient(
                    patient_id=row['Donor ID'],
                    age=age,
                    sex=row['Sex'],
                    years_of_education=years_of_education,
                    apoe_genotype=row['APOE Genotype'],
                    cognitive_status=row['Cognitive Status'],
                    age_onset=age_onset,
                    casi=casi,
                    mmse=mmse,
                    moca=moca,
                    abeta40=abeta40,
                    abeta42=abeta42,
                    ttau=ttau,
                    ptau=ptau
                )


    @classmethod
    def filter(
        cls,
        list,
        age="any",
        sex="any",
        years_of_education="any",
        cognitive_status="any",
        age_onset="any"
    ):

        all_patients = list
        remove_list = []

        attr_list = (
            age,
            sex,
            years_of_education,
            cognitive_status,
            age_onset
        )

        attr_name = (
            "age",
            "sex",
            "years_of_education",
            "cognitive_status",
            "age_onset"
        )

        for attr in range(len(attr_list)):

            if attr_list[attr] != "any":

                for patient in all_patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)

                all_patients = [
                    patient for patient in all_patients
                    if patient not in remove_list
                ]

                remove_list.clear()

        return all_patients