
import streamlit as st
import pandas as pd

from datetime import date

from patient.patient import Patient
from doctor.doctor import Doctor
from appointment.appointment import Appointment

from database.patient_table import (
    create_patient_table,
    save_patient,
    get_all_patients
)

from database.doctor_table import (
    create_doctor_table,
    save_doctor,
    get_all_doctors,
    get_doctor_available_times
)

from database.appointment_table import (
    create_appointment_table,
    save_appointment,
    get_all_appointments
)


# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------

st.set_page_config(
    page_title="Hospital Management System",
    page_icon="🏥",
    layout="wide"
)


# -----------------------------------
# DATABASE INITIALIZATION
# -----------------------------------

create_patient_table()
create_doctor_table()
create_appointment_table()


# -----------------------------------
# PAGE HEADER
# -----------------------------------

st.title("🏥 Hospital Management System")

st.caption(
    "Patient Management | Doctor Management | Appointments"
)

st.divider()


# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------

st.sidebar.title("🏥 HMS Navigation")

page = st.sidebar.radio(
    "Select a Section",
    [
        "Dashboard",
        "Register Patient",
        "View Patients",
        "Register Doctor",
        "View Doctors",
        "Book Appointment",
        "Check Appointments"
    ]
)


# -----------------------------------
# DASHBOARD
# -----------------------------------

if page == "Dashboard":

    st.header("📊 Dashboard")

    patients = get_all_patients()
    doctors = get_all_doctors()
    appointments = get_all_appointments()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Patients",
        len(patients)
    )

    col2.metric(
        "Total Doctors",
        len(doctors)
    )

    col3.metric(
        "Total Appointments",
        len(appointments)
    )

    st.divider()

    st.subheader("Welcome!")

    st.write(
        "Use the navigation menu on the left "
        "to manage patients, doctors and appointments."
    )


# -----------------------------------
# REGISTER PATIENT
# -----------------------------------

elif page == "Register Patient":

    st.header("👤 Patient Registration")

    with st.form("patient_registration_form"):

        name = st.text_input("Patient Name")

        age = st.number_input(
            "Patient Age",
            min_value=1,
            max_value=120,
            value=18,
            step=1
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        disease = st.selectbox(
            "Disease",
            [
                "Heart",
                "Skin",
                "Eye",
                "Bone",
                "Stomach",
                "Child",
                "General"
            ]
        )

        submitted = st.form_submit_button(
            "Register Patient"
        )

    if submitted:

        if not name.strip():
            st.error("Please enter the patient name.")

        else:

            patient = Patient(
                name.strip(),
                int(age),
                gender,
                disease
            )

            patient_id = save_patient(patient)

            st.success(
                f"Patient registered successfully! "
                f"Patient ID: {patient_id}"
            )


# -----------------------------------
# VIEW PATIENTS
# -----------------------------------

elif page == "View Patients":

    st.header("👥 All Patients")

    patients = get_all_patients()

    if not patients:

        st.info("No patients found.")

    else:

        patient_df = pd.DataFrame(
            patients,
            columns=[
                "Patient ID",
                "Patient Name",
                "Age",
                "Gender",
                "Disease"
            ]
        )

        st.dataframe(
            patient_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total registered patients: {len(patients)}"
        )


# -----------------------------------
# REGISTER DOCTOR
# -----------------------------------

elif page == "Register Doctor":

    st.header("🩺 Doctor Registration")

    with st.form("doctor_registration_form"):

        name = st.text_input("Doctor Name")

        specialization = st.selectbox(
            "Specialization",
            [
                "Cardiologist",
                "Dermatologist",
                "Ophthalmologist",
                "Orthopedic",
                "Gastroenterologist",
                "Pediatrician",
                "General Physician"
            ]
        )

        available_times = st.multiselect(
            "Available Appointment Times",
            [
                "09:00",
                "10:00",
                "11:00",
                "12:00",
                "13:00",
                "14:00",
                "15:00",
                "16:00"
            ]
        )

        submitted = st.form_submit_button(
            "Register Doctor"
        )

    if submitted:

        if not name.strip():

            st.error("Please enter the doctor name.")

        elif not available_times:

            st.error(
                "Please select at least one available time."
            )

        else:

            doctor = Doctor(
                name.strip(),
                specialization,
                available_times
            )

            doctor_id = save_doctor(doctor)

            st.success(
                f"Doctor registered successfully! "
                f"Doctor ID: {doctor_id}"
            )


# -----------------------------------
# VIEW DOCTORS
# -----------------------------------

elif page == "View Doctors":

    st.header("👨‍⚕️ All Doctors")

    doctors = get_all_doctors()

    if not doctors:

        st.info("No doctors found.")

    else:

        doctor_rows = []

        for doctor in doctors:

            times = doctor[3]

            if times:
                times = ", ".join(times.split(","))
            else:
                times = "No available times"

            doctor_rows.append({
                "Doctor ID": doctor[0],
                "Doctor Name": doctor[1],
                "Specialization": doctor[2],
                "Available Times": times
            })

        doctor_df = pd.DataFrame(doctor_rows)

        st.dataframe(
            doctor_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total registered doctors: {len(doctors)}"
        )


# -----------------------------------
# BOOK APPOINTMENT
# -----------------------------------

elif page == "Book Appointment":

    st.header("📅 Book Appointment")

    patients = get_all_patients()
    doctors = get_all_doctors()

    if not patients:

        st.warning(
            "No patients registered. "
            "Please register a patient first."
        )

    elif not doctors:

        st.warning(
            "No doctors registered. "
            "Please register a doctor first."
        )

    else:

        patient_options = {
            f"{p[1]} (ID: {p[0]})": p[0]
            for p in patients
        }

        doctor_options = {
            f"{d[1]} - {d[2]} (ID: {d[0]})": d[0]
            for d in doctors
        }

        with st.form("appointment_form"):

            selected_patient = st.selectbox(
                "Select Patient",
                list(patient_options.keys())
            )

            selected_doctor = st.selectbox(
                "Select Doctor",
                list(doctor_options.keys())
            )

            appointment_date = st.date_input(
                "Appointment Date",
                min_value=date.today()
            )

            book_submitted = st.form_submit_button(
                "Book Appointment"
            )

        if book_submitted:

            patient_id = patient_options[selected_patient]
            doctor_id = doctor_options[selected_doctor]

            available_times = get_doctor_available_times(
                doctor_id
            )

            if not available_times:

                st.error(
                    "This doctor has no available times."
                )

            else:

                st.session_state["appointment_context"] = {
                    "patient_id": patient_id,
                    "doctor_id": doctor_id,
                    "appointment_date": appointment_date.isoformat(),
                    "available_times": available_times
                }

        context = st.session_state.get(
            "appointment_context"
        )

        if context:

            # Verify that the saved selection still
            # corresponds to the currently selected date
            # and doctor before booking.

            if (
                context["doctor_id"] != doctor_options[selected_doctor]
                or context["patient_id"] != patient_options[selected_patient]
                or context["appointment_date"] != appointment_date.isoformat()
            ):

                st.info(
                    "Your selection has changed. "
                    "Click 'Book Appointment' again to load "
                    "the available times."
                )

            else:

                st.subheader("Available Appointment Times")

                selected_time = st.selectbox(
                    "Select Time",
                    context["available_times"],
                    key="appointment_time"
                )

                if st.button(
                    "Confirm Appointment",
                    type="primary"
                ):

                    appointment = Appointment(
                        context["patient_id"],
                        context["doctor_id"],
                        context["appointment_date"],
                        selected_time
                    )

                    appointment_id = save_appointment(
                        appointment
                    )

                    if appointment_id is None:

                        st.error(
                            "This appointment time is already booked. "
                            "Please choose another time."
                        )

                    else:

                        st.success(
                            "Appointment booked successfully!"
                        )

                        st.write(
                            "Appointment ID:",
                            appointment_id
                        )

                        st.write(
                            "Patient ID:",
                            context["patient_id"]
                        )

                        st.write(
                            "Doctor ID:",
                            context["doctor_id"]
                        )

                        st.write(
                            "Date:",
                            context["appointment_date"]
                        )

                        st.write(
                            "Time:",
                            selected_time
                        )

                        del st.session_state[
                            "appointment_context"
                        ]


# -----------------------------------
# CHECK APPOINTMENTS
# -----------------------------------

elif page == "Check Appointments":

    st.header("📋 All Appointments")

    appointments = get_all_appointments()

    if not appointments:

        st.info("No appointments found.")

    else:

        appointment_df = pd.DataFrame(
            appointments,
            columns=[
                "Appointment ID",
                "Patient Name",
                "Doctor Name",
                "Specialization",
                "Appointment Date",
                "Appointment Time"
            ]
        )

        st.dataframe(
            appointment_df,
            use_container_width=True,
            hide_index=True
        )

        st.caption(
            f"Total appointments: {len(appointments)}"
        )


# -----------------------------------
# FOOTER
# -----------------------------------

st.divider()

st.caption(
    "Hospital Management System | Python + Streamlit + SQLite"
)