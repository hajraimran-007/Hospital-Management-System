import sqlite3


def create_doctor_table():

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    query.execute("""
        CREATE TABLE IF NOT EXISTS doctors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            specialization TEXT,
            available_times TEXT
        )
    """)

    query.execute("PRAGMA table_info(doctors)")
    columns = query.fetchall()
    column_names = []

    for column in columns:
        column_names.append(column[1])

    if "available_times" not in column_names:
        query.execute("""
            ALTER TABLE doctors
            ADD COLUMN available_times TEXT
        """)

    connect.commit()
    connect.close()


def save_doctor(doctor):

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    available_times = ",".join(
        doctor.available_times
    )

    query.execute("""
        INSERT INTO doctors
        (
            name,
            specialization,
            available_times
        )
        VALUES (?, ?, ?)
    """, (
        doctor.name,
        doctor.specialization,
        available_times
    ))

    connect.commit()

    doctor_id = query.lastrowid

    connect.close()

    return doctor_id


def get_doctor_available_times(doctor_id):

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    query.execute("""
        SELECT available_times
        FROM doctors
        WHERE id = ?
    """, (doctor_id,))

    result = query.fetchone()

    connect.close()

    if result is None:
        return None

    available_times = result[0]

    if not available_times:
        return []

    available_times = available_times.split(",")

    return available_times


def get_all_doctors():

    connect = sqlite3.connect("database/PIMS.db")
    query = connect.cursor()

    query.execute("""
        SELECT
            id,
            name,
            specialization,
            available_times
        FROM doctors
        ORDER BY id
    """)

    doctors = query.fetchall()

    connect.close()

    return doctors