# Charlotte Lim (wfr2pj)
import csv

class Patient:
    all_patients = []
    def __init__(self, sex: str, ageofD: float,yearsEd: float , genotype: str, ageofSym : str,
                 cogStat: str, abeta42: float, pTAU: float ):
        self.sex = sex
        self.ageofD = ageofD
        self.yearsEd = yearsEd
        self.genotype = genotype
        self.ageofSym = ageofSym
        self.cogStat = cogStat
        self.abeta42 = abeta42
        self.pTAU = pTAU
        Patient.all_patients.append(self)

    def __repr__(self):  # prints object when printed, can define however you want
        return (f"{self.sex} | Age of Death: {self.ageofD} | Years of Education: {self.yearsEd} | APOE Genotype: {self.genotype} | {self.cogStat} | abeta42: {self.abeta42} pg/ug | pTAU: {self.pTAU} pg/ug")

    @classmethod
    def get_patient_genotype(cls, genotype):
        for patient in Patient.all_patients:
            if genotype == patient.genotype:
                return patient

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        # the code below will open the .csv file and create a list of all the rows in your spreadsheet
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
            # the code below will create a dog object for each row, based on the data:
            for row in rows_of_patients:
                Patient(sex=row['Sex'],ageofSym=row['Age of Dementia diagnosis'], ageofD=int(row['Age at Death']),genotype=row['APOE Genotype'],cogStat=row['Cognitive Status'],
                    yearsEd=int(row['Years of education']),abeta42=float(row['ABeta42 pg/ug']), pTAU=float(row['pTAU pg/ug']))

# sex,ageofSym, ageofD,genotype,cogStat, yearsEd,abeta42, pTAU
    @classmethod # filter by attribute
    def filter(cls, list, sex: str = "any", ageofSym: int = "any", ageofD: int = "any", genotype: str = "any",
               cogStat: str = "any", yearsEd: int = "any", abeta42: str = "any", pTAU: str = "any"):
        all_patients = list
        remove_list = []
        attr_list = (
            sex,
            ageofSym,
            ageofD,
            genotype,
            cogStat,
            yearsEd,
            abeta42,
            pTAU
        )
        attr_name = (
            "sex",
            "ageofSym",
            "ageofD",
            "genotype",
            "cogStat",
            "yearsEd",
            "abeta42",
            "pTAU"
)
        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)
                all_patients = [patient for patient in all_patients if patient not in remove_list]
                remove_list.clear()

        return all_patients

