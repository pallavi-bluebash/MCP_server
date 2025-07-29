# 🤖 **Seamless Sign-ups by Pallavi (AI-Driven)**

Welcome to the future of user registration! This isn't just another form; it's a dynamic, AI-powered assistant designed by Pallavi to streamline how you manage user sign-ups. Built with the cutting-edge **Google Gemini 2.0 Flash** and a custom **Model Calling Protocol (MCP) server**, this project brings intelligent automation right to your fingertips.

Forget manual data entry and duplicate headaches. With **Seamless Sign-ups by Pallavi (AI-Driven)**, you simply tell the system what you need, and it intelligently handles the rest – from registering new users to instantly fetching your entire database.

---

## ✨ **What Makes This Hub Shine?**

* **Intelligent Conversational Interface:** Powered by Gemini 2.0 Flash, understand and respond to natural language commands for registration and data retrieval.
* **Local & Secure Data Management:** All user details (Name, Email, DOB) are safely stored in a local `registration.csv` file, giving you full control.
* **No More Duplicates!** Our smart backend ensures that each user's email is unique, preventing redundant entries with a clear "already registered" alert.
* **Instant Data Insights:** Ask for all registered users, and watch as your data magically appears in a beautifully formatted, interactive table, complete with serial numbers.
* **Sleek & User-Friendly Design:**
    * **Customized Title:** "🤖 Seamless Sign-ups by Pallavi (AI-Driven) 🚀" – bold, blue, and brimming with personality!
    * **Vibrant UI:** A refreshing color palette and modern styling for inputs, buttons (now green!), and alert messages, making every interaction a delight.
    * **Guided Examples:** A handy dropdown offers quick prompts to get you started, from registering new users to listing existing ones.
    * **Clear Feedback:** Intuitive success, warning, and info messages keep you informed every step of the way.

---

## 🛠️ **Under the Hood: The Architecture**

This project seamlessly integrates a Streamlit frontend with a custom Python backend (the MCP server) acting as a bridge to your local CSV database.


your_mcp_assignment/
├── tools/                 # Your intelligent backend functions
│   ├── init.py        # Python package marker
│   ├── fetch.py           # Reads user data from CSV
│   └── store.py           # Writes new user data to CSV (with duplicate check!)
├── .env                   # Your secret Gemini API key lives here
├── llm.py                 # The dazzling Streamlit UI & Gemini interaction logic
├── server.py              # The heart of your custom MCP server
├── registration.csv       # Your user database (CSV format)
├── requirements.txt       # All the Python magic you need to install
├── README.md              # (You're reading it!) Project guide
├── pyproject.toml         # Project metadata

---

## 🚀 **Get Started in a Flash!**

Follow these simple steps to bring **Seamless Sign-ups by Pallavi (AI-Driven)** to life on your machine:

1.  **Set Up Your Project Space:**
    * Create a main directory (e.g., `my_ai_registration_app`).
    * Inside, create a `tools` subdirectory.
    * Place all the provided Python files (`llm.py`, `server.py`, `tools/fetch.py`, `tools/store.py`, `tools/__init__.py`), along with `registration.csv`, `requirements.txt`, `.env`, `pyproject.toml`, `python-version`, and `uv.lock` in their respective locations.

2.  **Your Secret Key (`.env`):**
    * Open the `.env` file in your project root.
    * Add your Google Gemini API key:
        ```
        GEMINI_API_KEY=YOUR_GEMINI_API_KEY
        ```
        **Remember to replace `YOUR_GEMINI_API_KEY` with your actual key!**

3.  **Install the Magic Ingredients:**
    * Open your terminal.
    * Navigate to your project's root directory.
    * **(Highly Recommended!) Create and activate a Python virtual environment:**
        ```bash
        python -m venv venv
        source venv/bin/activate  # On Windows: .\venv\Scripts\activate
        ```
    * Install all necessary Python libraries:
        ```bash
        pip install -r requirements.txt
        ```

4.  **Ignite the MCP Server!**
    * In your **first terminal** window (still in your project root), run:
        ```bash
        python server.py
        ```
    * Keep this window open – it's the backbone of your AI assistant!

5.  **Launch the AI Registration Hub!**
    * Open a **second terminal** window.
    * Navigate to your project's root directory.
    * Run the Streamlit application:
        ```bash
        streamlit run llm.py
        ```
    * Your default web browser will automatically open the beautiful **Seamless Sign-ups by Pallavi (AI-Driven)**!

---

## 💬 **Interact with Your AI Assistant!**

Now, dive in and experience the seamless registration process:

* **To Register a New User:**
    Type or select from examples:
    `Register John Doe with email john.doe@example.com and DOB 1990-05-15`
    *(Try registering yourself using the pre-filled example for Pallavi Sharma!)*

* **Test Duplicate Prevention:**
    Attempt to register the same user (with the exact same email) again. Watch for the friendly warning that prevents duplicates!

* **View All Registrations:**
    Type or select from examples:
    `Show all registrations`
    `List all users`
    Your AI assistant will fetch and display all registered users in a clear, interactive table.

---

Enjoy the power of AI-driven registration, crafted with care by Pallavi!
