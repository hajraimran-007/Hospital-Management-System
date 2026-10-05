from patient.patient import Patient


def create_patient():

    print("\n===== Add Patient =====")

    # ==============================
    # Patient Name
    # ==============================

    name = input("Enter patient name: ")


    # ==============================
    # Patient Age
    # ==============================

    while True:

        try:
            age = int(input("Enter patient age: "))

            if age > 0:
                break
            else:
                print("Age must be greater than 0.")

        except ValueError:
            print("Please enter a valid age.")


    # ==============================
    # Patient Gender
    # ==============================

    print("\nSelect Gender:")
    print("1. Male")
    print("2. Female")
    print("3. Other")

    while True:

        gender_choice = input(
            "Enter gender choice or gender name: "
        ).strip().lower()

        if gender_choice == "1" or gender_choice == "male":

            gender = "Male"
            break

        elif gender_choice == "2" or gender_choice == "female":

            gender = "Female"
            break

        elif gender_choice == "3" or gender_choice == "other":

            gender = "Other"
            break

        else:

            print(
                "Invalid choice. Enter 1, 2, 3 "
                "or Male, Female, Other."
            )


    # ==============================
    # Patient Disease
    # ==============================

    print("\nSelect Disease:")
    print("1. Heart Disease")
    print("2. Skin Disease")
    print("3. Eye Disease")
    print("4. Bone Disease")
    print("5. Stomach Disease")
    print("6. Child Disease")
    print("7. General Disease")

    while True:

        disease_choice = input(
            "Enter disease choice or disease name: "
        ).strip().lower()

        if (
            disease_choice == "1"
            or disease_choice == "heart disease"
        ):

            disease = "Heart Disease"
            break

        elif (
            disease_choice == "2"
            or disease_choice == "skin disease"
        ):

            disease = "Skin Disease"
            break

        elif (
            disease_choice == "3"
            or disease_choice == "eye disease"
        ):

            disease = "Eye Disease"
            break

        elif (
            disease_choice == "4"
            or disease_choice == "bone disease"
        ):

            disease = "Bone Disease"
            break

        elif (
            disease_choice == "5"
            or disease_choice == "stomach disease"
        ):

            disease = "Stomach Disease"
            break

        elif (
            disease_choice == "6"
            or disease_choice == "child disease"
        ):

            disease = "Child Disease"
            break

        elif (
            disease_choice == "7"
            or disease_choice == "general disease"
        ):

            disease = "General Disease"
            break

        else:

            print(
                "Invalid choice. Enter 1 to 7 "
                "or a valid disease name."
            )


    # ==============================
    # Patient Object Create
    # ==============================

    patient = Patient(
        name,
        age,
        gender,
        disease
    )

    return patient