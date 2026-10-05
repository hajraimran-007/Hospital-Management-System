import sqlite3


def create_patient_table():

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    query.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            disease TEXT
        )
    """)

    connect.commit()
    connect.close()


def save_patient(patient):

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    query.execute("""
        INSERT INTO patients
        (name, age, gender, disease)
        VALUES (?, ?, ?, ?)
    """, (
        patient.name,
        patient.age,
        patient.gender,
        patient.disease
    ))

    connect.commit()

    patient_id = query.lastrowid

    connect.close()

    return patient_id


def get_all_patients():

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    query.execute("""
        SELECT
            id,
            name,
            age,
            gender,
            disease
        FROM patients
        ORDER BY id
    """)

    patients = query.fetchall()

    connect.close()

    return patients