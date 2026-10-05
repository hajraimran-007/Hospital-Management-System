from operations import (
    initialize_database,
    register_patient,
    view_patients,
    register_doctor,
    view_doctors,
    book_appointment,
    check_appointments
)


def main():

    print("===== Hospital Management System =====")

    initialize_database()

    while True:

        print("\n===== Main Menu =====")

        print("1. Register Patient")
        print("2. View Patients")
        print("3. Register Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. Check Appointments")
        print("7. Exit")

        choice = input(
            "\nEnter your choice: "
        ).strip()

        if choice == "1":

            register_patient()

        elif choice == "2":

            view_patients()

        elif choice == "3":

            register_doctor()

        elif choice == "4":

            view_doctors()

        elif choice == "5":

            book_appointment()

        elif choice == "6":

            check_appointments()

        elif choice == "7":

            print(
                "\nThank you for using "
                "Hospital Management System."
            )

            break

        else:

            print(
                "\nInvalid choice. "
                "Please select 1 to 7."
            )


if __name__ == "__main__":
    main()