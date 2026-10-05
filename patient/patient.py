class Patient:

    def __init__(self, name, age, gender, disease):

        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def display_patient(self):

        print("\n===== Patient Information =====")

        print("Patient Name:", self.name)
        print("Patient Age:", self.age)
        print("Patient Gender:", self.gender)
        print("Patient Disease:", self.disease)