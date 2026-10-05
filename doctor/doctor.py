class Doctor:

    def __init__(self, name, specialization, available_times):

        self.name = name
        self.specialization = specialization
        self.available_times = available_times

    def display_doctor(self):

        print("\n===== Doctor Information =====")

        print("Doctor Name:", self.name)
        print("Specialization:", self.specialization)
        print("Available Times:")

        for time in self.available_times:
            print("-", time)