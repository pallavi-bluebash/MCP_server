import csv
import os

def store_data(name: str, email: str, dob: str) -> str:
    """
    Registers a new user by saving their name, email, and date of birth (DOB)
    to a local CSV file named 'registration.csv'.
    Prevents duplicate registrations based on the email address.

    Args:
        name (str): The name of the user.
        email (str): The email address of the user.
        dob (str): The date of birth of the user (e.g., 'YYYY-MM-DD').

    Returns:
        str: A confirmation message indicating whether the registration was successful,
             or a message indicating that the user is already registered.
    """
    file_path = 'registration.csv'
    fieldnames = ['Name', 'email', 'dob']
    
    existing_users = []
    file_exists = os.path.isfile(file_path)

    # Step 1: Read all existing data if the file exists
    if file_exists:
        try:
            with open(file_path, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    existing_users.append(row)
        except Exception as e:
            print(f"Warning: Could not read existing registration.csv: {e}")
            # If reading fails, we might proceed, but it's safer to assume no existing users
            # or handle this as an error that prevents new registration for safety.
            # For now, we'll let it proceed as if no users were read.

    # Step 2: Check for duplicates in the read data
    for user in existing_users:
        if user.get('email', '').lower() == email.lower():
            return f"Registration failed: User with email '{email}' is already registered."

    # Step 3: If no duplicate, append the new data
    try:
        # Open in append mode, but handle header writing carefully
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # Write header only if the file was just created (i.e., it didn't exist before)
            if not file_exists:
                writer.writeheader()

            writer.writerow({'Name': name, 'email': email, 'dob': dob})
        return f"User '{name}' registered successfully with email '{email}' and DOB '{dob}'."
    except Exception as e:
        return f"Error registering user '{name}': {e}"

