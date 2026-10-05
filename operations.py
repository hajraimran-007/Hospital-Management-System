from patient.patient_service import create_patient
from database.patient_table import (
    create_patient_table,
    save_patient,
    get_all_patients
)

from doctor.doctor_service import create_doctor
from database.doctor_table import (
    create_doctor_table,
    save_doctor,
    get_all_doctors
)

from appointment.appointment_service import create_appointment
from database.appointment_table import (
    create_appointment_table,
    save_appointment,
    get_all_appointments
)


def register_patient():

    print("\n===== Patient Registration =====")

    patient = create_patient()

    patient_id = save_patient(patient)

    print("\n===== Patient Information =====")

    print("Patient ID:", patient_id)
    print("Patient Name:", patient.name)
    print("Patient Age:", patient.age)
    print("Patient Gender:", patient.gender)
    print("Patient Disease:", patient.disease)

    print("\nPatient data saved successfully.")


def view_patients():

    print("\n===== All Patients =====")

    patients = get_all_patients()

    if len(patients) == 0:
        print("\nNo patients found.")
        return

    for patient in patients:

        print("\n------------------------------")

        print("Patient ID:", patient[0])
        print("Patient Name:", patient[1])
        print("Patient Age:", patient[2])
        print("Patient Gender:", patient[3])
        print("Patient Disease:", patient[4])

    print("\n------------------------------")


def register_doctor():

    print("\n===== Doctor Registration =====")

    doctor = create_doctor()

    doctor_id = save_doctor(doctor)

    print("\n===== Doctor Information =====")

    print("Doctor ID:", doctor_id)
    print("Doctor Name:", doctor.name)
    print("Specialization:", doctor.specialization)

    print("Available Times:")

    for time in doctor.available_times:
        print("-", time)

    print("\nDoctor data saved successfully.")


def view_doctors():

    print("\n===== All Doctors =====")

    doctors = get_all_doctors()

    if len(doctors) == 0:
        print("\nNo doctors found.")
        return

    for doctor in doctors:

        print("\n------------------------------")

        print("Doctor ID:", doctor[0])
        print("Doctor Name:", doctor[1])
        print("Specialization:", doctor[2])

        print("Available Times:")

        if doctor[3]:

            available_times = doctor[3].split(",")

            for time in available_times:
                print("-", time)

        else:
            print("- No available times")

    print("\n------------------------------")


def book_appointment():

    print("\n===== Appointment Booking =====")

    appointment = create_appointment()

    if appointment is None:
        print("\nAppointment could not be created.")
        return

    appointment_id = save_appointment(
        appointment
    )

    if appointment_id is None:
        print(
            "\nThis appointment time is already booked."
        )
        return

    print("\n===== Appointment Information =====")

    print("Appointment ID:", appointment_id)
    print("Patient ID:", appointment.patient_id)
    print("Doctor ID:", appointment.doctor_id)

    print(
        "Appointment Date:",
        appointment.appointment_date
    )

    print(
        "Appointment Time:",
        appointment.appointment_time
    )

    print("\nAppointment booked successfully.")


def check_appointments():

    print("\n===== All Appointments =====")

    appointments = get_all_appointments()

    if len(appointments) == 0:
        print("\nNo appointments found.")
        return

    for appointment in appointments:

        print("\n------------------------------")

        print(
            "Appointment ID:",
            appointment[0]
        )

        print(
            "Patient Name:",
            appointment[1]
        )

        print(
            "Doctor Name:",
            appointment[2]
        )

        print(
            "Doctor Specialization:",
            appointment[3]
        )

        print(
            "Appointment Date:",
            appointment[4]
        )

        print(
            "Appointment Time:",
            appointment[5]
        )

    print("\n------------------------------")


def initialize_database():

    create_patient_table()
    create_doctor_table()
    create_appointment_table()