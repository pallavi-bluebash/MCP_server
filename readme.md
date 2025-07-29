🤖 Seamless Sign-ups by Pallavi (AI-Driven) 
This is a demo project that leverages Google Gemini 2.0 Flash to interact with a locally hosted MCP (Model Calling Protocol) server. The MCP server exposes tools (functions) for managing user registration data, which Gemini can call directly through its powerful tool-use capabilities. This application stores user registration details in a local CSV file, providing a robust and self-contained solution for user management.

Project Features
AI-Powered Registration: Utilize Google Gemini 2.0 Flash for natural language understanding and tool invocation.

Local Data Storage: User registration data (Name, Email, DOB) is securely stored in a local registration.csv file.

Duplicate Registration Prevention: Ensures that a user cannot register multiple times with the same email address.

User Data Retrieval: Fetch and display all stored user data from the CSV file.

Interactive Table Display: Registered users are presented in a clean, sortable, and interactive table directly on the Streamlit UI, complete with serial numbers.

Enhanced User Interface:

Custom Title: A creative and personalized title: "🤖 Seamless Sign-ups by Pallavi (AI-Driven) " with vibrant blue color and bold font.

Colorful Theme: A visually appealing UI with custom CSS for background, input fields, buttons, and alert messages.

Example Prompts: A dropdown menu provides pre-defined example prompts for easy interaction.

Clear Feedback: Distinct visual feedback (green for success, yellow for warnings) for tool execution results.

Project Structure
your_mcp_assignment/
├── tools/
│   ├── __init__.py
│   ├── fetch.py
│   └── store.py
├── .env
├── llm.py
├── server.py
├── registration.csv
├── requirements.txt
├── README.md
├── pyproject.toml

File Descriptions:
tools/: Directory containing backend tool functions.

__init__.py: Makes tools a Python package.

fetch.py: Contains the fetch_data function to read user data from registration.csv and return it as a list of dictionaries.

store.py: Contains the store_data function to write new user data to registration.csv, including a check for duplicate emails.

.env: Stores your Gemini API key (e.g., GEMINI_API_KEY=YOUR_API_KEY).

llm.py: The Streamlit client application. This is the main UI that interacts with the user, sends requests to the LLM, and displays results from the MCP server.

server.py: The local MCP server application. It registers the fetch_data and store_data functions as callable tools for the LLM.

registration.csv: The CSV file where all user registration data is stored.

requirements.txt: Lists all Python package dependencies required for the project.

README.md: This file, providing project overview and instructions.

pyproject.toml: Project metadata and dependencies configuration (used by uv).

Setup Instructions
Clone or Create the Project Structure:
Ensure you have the folder structure as described above. If you're starting fresh, create the your_mcp_assignment directory and the tools subdirectory within it.

Create/Prepare registration.csv:
Make sure you have an empty registration.csv file in the root of your project (your_mcp_assignment/). If it exists with old data, you might want to clear it (keeping only the header Name,email,dob) or delete it to test duplicate prevention effectively.

Set up Environment Variables:
Create a file named .env in the root of your project (your_mcp_assignment/) and add your Gemini API key:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY

Replace YOUR_GEMINI_API_KEY with your actual Gemini API key.

Install Dependencies:
Navigate to your project's root directory (your_mcp_assignment/) in your terminal and install all required Python packages. It's recommended to use a virtual environment.

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate # On Windows: .\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

How to Run
To run the application, you need to start two separate processes in two different terminal windows:

1. Start the MCP Server
In your first terminal window, navigate to the project's root directory (your_mcp_assignment/) and run:

python server.py

This will start your local MCP server, typically listening on http://127.0.0.1:8000/mcp. Keep this terminal window open and running.

2. Run the Streamlit Client
In your second terminal window, navigate to the same project's root directory (your_mcp_assignment/) and run:

streamlit run llm.py

This will open the Streamlit application in your default web browser (usually at http://localhost:8501).

Usage
Once both the MCP server and Streamlit client are running, you can interact with the AI Registration Assistant through the web interface:

Register a new user:
Select "Register a new user" from the dropdown or type a command like:
Register John Doe with email john.doe@example.com and DOB 1990-05-15

Attempt duplicate registration:
Try registering the same user (with the same email) again. The system will prevent the duplicate and provide a warning message.

Show all registered users:
Select "Show all registrations" or "List registered users" from the dropdown, or type a command like:
Show all registrations
List all users
The registered users will be displayed in a formatted table on the UI.

Enjoy your AI-powered registration system!