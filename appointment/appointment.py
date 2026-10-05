class Appointment:

    def __init__(
        self,
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time
    ):

        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.appointment_date = appointment_date
        self.appointment_time = appointment_time

    def display_appointment(self):

        print("\n===== Appointment Information =====")

        print("Patient ID:", self.patient_id)
        print("Doctor ID:", self.doctor_id)
        print("Appointment Date:", self.appointment_date)
        print("Appointment Time:", self.appointment_time)