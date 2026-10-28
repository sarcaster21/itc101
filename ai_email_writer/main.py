from email_generator import generate_email


def main():
    while True:
        print("\n===== AI EMAIL WRITER =====")
        print("1. Generate Email")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            purpose = input("\nPurpose of the email: ")
            recipient = input("Who is the email for? ")
            tone = input("Tone (formal/professional/friendly): ")
            details = input("Important details to include: ")

            email = generate_email(
                purpose,
                recipient,
                tone,
                details
            )

            print("\n===== GENERATED EMAIL =====\n")
            print(email)

        elif choice == "2":
            print("\nThank you for using AI Email Writer!")
            break

        else:
            print("\nInvalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()