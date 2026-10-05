from doctor.doctor import Doctor


def get_doctors():
    doctors = [
        Doctor(
            "Dr. Ahmed Khan",
            "Cardiologist",
            ["Monday", "Wednesday", "Friday"],
            [
                "09:00 AM - 12:00 PM",
                "04:00 PM - 07:00 PM"
            ]
        ),

        Doctor(
            "Dr. Sara Ali",
            "Dermatologist",
            ["Tuesday", "Thursday", "Saturday"],
            [
                "01:00 PM - 03:00 PM",
                "07:00 PM - 09:00 PM"
            ]
        ),

        Doctor(
            "Dr. Usman Malik",
            "Ophthalmologist",
            ["Monday", "Tuesday", "Thursday"],
            [
                "09:00 AM - 12:00 PM",
                "04:00 PM - 07:00 PM"
            ]
        ),

        Doctor(
            "Dr. Hamza Ahmed",
            "Orthopedic",
            ["Wednesday", "Friday", "Saturday"],
            [
                "01:00 PM - 03:00 PM",
                "07:00 PM - 09:00 PM"
            ]
        ),

        Doctor(
            "Dr. Ayesha Noor",
            "Gastroenterologist",
            ["Monday", "Wednesday", "Saturday"],
            [
                "09:00 AM - 12:00 PM",
                "04:00 PM - 07:00 PM"
            ]
        ),

        Doctor(
            "Dr. Bilal Shah",
            "Pediatrician",
            ["Tuesday", "Thursday", "Friday"],
            [
                "01:00 PM - 03:00 PM",
                "04:00 PM - 07:00 PM"
            ]
        ),

        Doctor(
            "Dr. Fatima Zahra",
            "General Physician",
            ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            [
                "09:00 AM - 12:00 PM",
                "04:00 PM - 07:00 PM"
            ]
        )
    ]

    return doctors