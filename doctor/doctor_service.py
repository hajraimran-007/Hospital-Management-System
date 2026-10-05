from doctor.doctor import Doctor


def create_doctor():

    print("\n===== Add Doctor =====")


    # ==============================
    # Doctor Name
    # ==============================

    name = input("Enter doctor name: ")


    # ==============================
    # Doctor Specialization
    # ==============================

    print("\nSelect Specialization:")

    print("1. Cardiologist")
    print("2. Dermatologist")
    print("3. Ophthalmologist")
    print("4. Orthopedic")
    print("5. Gastroenterologist")
    print("6. Pediatrician")
    print("7. General Physician")


    while True:

        specialization_choice = input(
            "Enter specialization choice or specialization name: "
        ).strip().lower()


        if (
            specialization_choice == "1"
            or specialization_choice == "cardiologist"
        ):

            specialization = "Cardiologist"
            break


        elif (
            specialization_choice == "2"
            or specialization_choice == "dermatologist"
        ):

            specialization = "Dermatologist"
            break


        elif (
            specialization_choice == "3"
            or specialization_choice == "ophthalmologist"
        ):

            specialization = "Ophthalmologist"
            break


        elif (
            specialization_choice == "4"
            or specialization_choice == "orthopedic"
        ):

            specialization = "Orthopedic"
            break


        elif (
            specialization_choice == "5"
            or specialization_choice == "gastroenterologist"
        ):

            specialization = "Gastroenterologist"
            break


        elif (
            specialization_choice == "6"
            or specialization_choice == "pediatrician"
        ):

            specialization = "Pediatrician"
            break


        elif (
            specialization_choice == "7"
            or specialization_choice == "general physician"
        ):

            specialization = "General Physician"
            break


        else:

            print(
                "Invalid choice. Enter 1 to 7 "
                "or a valid specialization name."
            )


    # ==============================
    # Doctor Available Time Slots
    # ==============================

    print("\nSelect Doctor Available Times:")

    print("1. 09:00")
    print("2. 10:00")
    print("3. 11:00")
    print("4. 14:00")
    print("5. 15:00")


    while True:

        time_choices = input(
            "\nEnter available time choices "
            "(example: 1,3,5): "
        ).strip()


        try:

            choices = time_choices.split(",")

            available_times = []

            for choice in choices:

                choice = choice.strip()

                if choice == "1":

                    time = "09:00"

                elif choice == "2":

                    time = "10:00"

                elif choice == "3":

                    time = "11:00"

                elif choice == "4":

                    time = "14:00"

                elif choice == "5":

                    time = "15:00"

                else:

                    raise ValueError


                if time not in available_times:

                    available_times.append(time)


            if len(available_times) > 0:

                break

            else:

                print(
                    "Please select at least one available time."
                )


        except ValueError:

            print(
                "Invalid choice. Please enter numbers from 1 to 5."
            )


    # ==============================
    # Doctor Object Create
    # ==============================

    doctor = Doctor(
        name,
        specialization,
        available_times
    )


    return doctor