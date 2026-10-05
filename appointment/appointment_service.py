from appointment.appointment import Appointment
from database.doctor_table import get_doctor_available_times
from database.appointment_table import is_time_booked


def create_appointment():

    print("\n===== Book Appointment =====")


    # ==============================
    # Patient ID
    # ==============================

    while True:

        try:
            patient_id = int(
                input("Enter patient ID: ")
            )

            if patient_id > 0:
                break

            else:
                print(
                    "Patient ID must be greater than 0."
                )

        except ValueError:

            print(
                "Please enter a valid patient ID."
            )


    # ==============================
    # Doctor ID
    # ==============================

    while True:

        try:
            doctor_id = int(
                input("Enter doctor ID: ")
            )

            if doctor_id > 0:
                break

            else:
                print(
                    "Doctor ID must be greater than 0."
                )

        except ValueError:

            print(
                "Please enter a valid doctor ID."
            )


    # ==============================
    # Doctor Available Times
    # ==============================

    available_times = get_doctor_available_times(
        doctor_id
    )


    # Doctor exist nahi karta
    if available_times is None:

        print("\nDoctor not found.")

        return None


    # Doctor ki availability empty hai
    if len(available_times) == 0:

        print(
            "\nThis doctor has no available "
            "appointment times."
        )

        return None


    # ==============================
    # Appointment Date
    # ==============================

    appointment_date = input(
        "\nEnter appointment date (YYYY-MM-DD): "
    ).strip()


    # ==============================
    # Remove Already Booked Times
    # ==============================

    free_times = []

    for time in available_times:

        if not is_time_booked(
            doctor_id,
            appointment_date,
            time
        ):

            free_times.append(time)


    # ==============================
    # Check Free Times
    # ==============================

    if len(free_times) == 0:

        print(
            "\nSorry, all available times "
            "are already booked for this date."
        )

        return None


    # ==============================
    # Available Appointment Times
    # ==============================

    print(
        "\n===== Available Appointment Times ====="
    )


    for index, time in enumerate(
        free_times,
        start=1
    ):

        print(index, ".", time)


    # ==============================
    # Select Appointment Time
    # ==============================

    while True:

        try:

            time_choice = int(
                input(
                    "\nSelect appointment time: "
                )
            )


            if (
                time_choice >= 1
                and time_choice <= len(free_times)
            ):

                appointment_time = free_times[
                    time_choice - 1
                ]

                break


            else:

                print(
                    "Please select a valid time option."
                )


        except ValueError:

            print(
                "Please enter a valid option number."
            )


    # ==============================
    # Appointment Object Create
    # ==============================

    appointment = Appointment(
        patient_id,
        doctor_id,
        appointment_date,
        appointment_time
    )


    return appointment