import csv
import os
from typing import List, Dict, Any

def fetch_data() -> List[Dict[str, Any]]:
    """
    Fetches all previously stored user data from the 'registration.csv' file
    and returns it as a list of dictionaries, suitable for table display.

    Returns:
        List[Dict[str, Any]]: A list of dictionaries, where each dictionary
                               represents a registered user with 'Name', 'email', and 'dob' keys.
                               Returns an empty list if no users are registered or an error occurs.
    """
    file_path = 'registration.csv'
    if not os.path.exists(file_path):
        return [] # Return empty list if file doesn't exist

    users = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Ensure consistent keys, even if some are missing in a row
                user_data = {
                    'Name': row.get('Name', 'N/A'),
                    'Email': row.get('email', 'N/A'), # Changed key to 'Email' for better display
                    'DOB': row.get('dob', 'N/A')       # Changed key to 'DOB' for better display
                }
                users.append(user_data)
        return users
    except Exception as e:
        # Do not use st.error here as this is a backend tool.
        # The calling Streamlit app (llm.py) will handle displaying errors
        # based on the empty list returned.
        print(f"Error fetching data in fetch.py: {e}") # Log the error for debugging
        return [] # Return empty list on error

