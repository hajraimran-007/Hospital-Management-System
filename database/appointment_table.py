import sqlite3


def create_appointment_table():

    # Database se connection
    connect = sqlite3.connect("database/PIMS.db")

    # Foreign Keys enable karna
    connect.execute("PRAGMA foreign_keys = ON")

    # Cursor create karna
    query = connect.cursor()

    # Appointment table create karna
    query.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            doctor_id INTEGER,
            appointment_date TEXT,
            appointment_time TEXT,
            FOREIGN KEY (patient_id) REFERENCES patients(id),
            FOREIGN KEY (doctor_id) REFERENCES doctors(id)
        )
    """)

    # Changes save karna
    connect.commit()

    # Database connection close
    connect.close()


def is_time_booked(
    doctor_id,
    appointment_date,
    appointment_time
):

    # Database se connection
    connect = sqlite3.connect("database/PIMS.db")

    # Cursor create karna
    query = connect.cursor()

    # Same doctor, same date aur same time check karna
    query.execute("""
        SELECT id
        FROM appointments
        WHERE doctor_id = ?
        AND appointment_date = ?
        AND appointment_time = ?
    """, (
        doctor_id,
        appointment_date,
        appointment_time
    ))

    result = query.fetchone()

    # Database connection close
    connect.close()

    if result is not None:
        return True

    return False


def save_appointment(appointment):

    # Database se connection
    connect = sqlite3.connect("database/PIMS.db")

    # Foreign Keys enable karna
    connect.execute("PRAGMA foreign_keys = ON")

    # Cursor create karna
    query = connect.cursor()

    # Double booking check karna
    if is_time_booked(
        appointment.doctor_id,
        appointment.appointment_date,
        appointment.appointment_time
    ):

        connect.close()

        return None

    # Appointment database mein insert karna
    query.execute("""
        INSERT INTO appointments
        (
            patient_id,
            doctor_id,
            appointment_date,
            appointment_time
        )
        VALUES (?, ?, ?, ?)
    """, (
        appointment.patient_id,
        appointment.doctor_id,
        appointment.appointment_date,
        appointment.appointment_time
    ))

    # Changes save karna
    connect.commit()

    # Appointment ID lena
    appointment_id = query.lastrowid

    # Connection close
    connect.close()

    return appointment_id


def get_all_appointments():

    # Database se connection
    connect = sqlite3.connect("database/PIMS.db")

    # Cursor create karna
    query = connect.cursor()

    # Patient aur doctor ke names ke saath
    # appointments retrieve karna
    query.execute("""
        SELECT
            appointments.id,
            patients.name,
            doctors.name,
            doctors.specialization,
            appointments.appointment_date,
            appointments.appointment_time
        FROM appointments
        JOIN patients
            ON appointments.patient_id = patients.id
        JOIN doctors
            ON appointments.doctor_id = doctors.id
        ORDER BY
            appointments.appointment_date,
            appointments.appointment_time
    """)

    appointments = query.fetchall()

    # Database connection close
    connect.close()

    return appointments