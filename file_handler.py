PATIENT_FILE = "patients.txt"
DOCTOR_FILE = "doctors.txt"
APPOINTMENT_FILE = "appointments.txt"


def save_patient(patient):
    with open(PATIENT_FILE, "a") as file:
        file.write(
            f"{patient.patient_id}|"
            f"{patient.name}|"
            f"{patient.age}|"
            f"{patient.gender}|"
            f"{patient.disease}\n"
        )


def load_patients():
    patients = []

    try:
        with open(PATIENT_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                if len(data) == 5:
                    patients.append(data)

    except FileNotFoundError:
        return []

    return patients


def save_doctor(doctor):
    with open(DOCTOR_FILE, "a") as file:
        days = ",".join(doctor.available_days)
        times = ",".join(doctor.available_times)

        file.write(
            f"{doctor.name}|"
            f"{doctor.specialization}|"
            f"{days}|"
            f"{times}\n"
        )


def convert_time_number(time_value):
    time_list = [
        "09:00 AM - 12:00 PM",
        "01:00 PM - 04:00 PM",
        "04:00 PM - 07:00 PM",
        "07:00 PM - 10:00 PM"
    ]

    time_value = time_value.strip()

    if time_value.isdigit():
        time_number = int(time_value)

        if 1 <= time_number <= 4:
            return time_list[time_number - 1]

    return time_value


def load_doctors():
    doctors = []

    try:
        with open(DOCTOR_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                if len(data) == 4:
                    name = data[0]
                    specialization = data[1]

                    available_days = [
                        day.strip()
                        for day in data[2].split(",")
                        if day.strip() != ""
                    ]

                    old_times = data[3].split(",")

                    available_times = []

                    for time in old_times:
                        converted_time = convert_time_number(time)

                        if converted_time != "":
                            available_times.append(
                                converted_time
                            )

                    doctors.append(
                        (
                            name,
                            specialization,
                            available_days,
                            available_times
                        )
                    )

    except FileNotFoundError:
        return []

    return doctors


def save_appointment(appointment):
    with open(APPOINTMENT_FILE, "a") as file:
        file.write(
            f"{appointment.patient.patient_id}|"
            f"{appointment.doctor.name}|"
            f"{appointment.appointment_day}|"
            f"{appointment.appointment_time}\n"
        )


def load_appointments():
    appointments = []

    try:
        with open(APPOINTMENT_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                data = line.split("|")

                if len(data) == 4:
                    appointments.append(data)

    except FileNotFoundError:
        return []

    return appointments