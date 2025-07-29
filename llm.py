import streamlit as st
import asyncio
from google import genai
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport
import os
from dotenv import load_dotenv
import pandas as pd # Import pandas for DataFrame display

# Load environment variables from .env file
load_dotenv()

# Retrieve the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    st.error("GEMINI_API_KEY not found in .env file. Please set it up.")
    st.stop() # Stop the Streamlit app if the key is missing

# Initialize the Gemini client using genai.Client
gemini_client = genai.Client(api_key=gemini_api_key)

# Initialize the MCP client
transport = StreamableHttpTransport(url="http://127.0.0.1:8000/mcp")
mcp_client = Client(transport)

# Add Font Awesome for icons
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">', unsafe_allow_html=True)

# --- UI Enhancements ---
st.set_page_config(layout="centered") # Set page layout to centered

# Custom CSS for a colorful UI
st.markdown(
    """
    <style>
    /* General page background and text color */
    .stApp {
        background-color: #f0f2f6; /* Light gray background */
        color: #333333; /* Darker text for contrast */
    }

    /* Main title styling */
    h1 {
        color: #1E90FF !important; /* Dodger Blue for the title */
        font-family: 'Inter', sans-serif; /* A modern, readable font */
        font-size: 2.8em !important; /* Adjusted font size */
        font-weight: 800 !important; /* Extra bold */
        /* Removed white-space, overflow, text-overflow as text should now fit */
    }

    /* Subtitle styling */
    h3 {
        color: #4682B4 !important; /* Steel Blue for subtitle */
        font-family: 'Roboto', sans-serif; /* Another good font */
    }

    /* Paragraph text */
    p {
        color: #555555;
    }

    /* Input fields and selectbox styling */
    .stTextInput > div > div > input, .stSelectbox > div > div {
        border-radius: 10px;
        border: 1px solid #ADD8E6; /* Light blue border */
        box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
    }

    /* Button styling */
    .stButton > button {
        background-color: #28a745; /* Green for primary button */
        color: white;
        border-radius: 10px;
        border: none;
        padding: 10px 20px;
        font-size: 1.1em;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
        transition: all 0.2s ease-in-out;
    }
    .stButton > button:hover {
        background-color: #218838; /* Darker green on hover */
        box-shadow: 3px 3px 8px rgba(0,0,0,0.3);
    }

    /* Info, Success, Warning boxes */
    .stAlert {
        border-radius: 10px;
        box-shadow: 1px 1px 3px rgba(0,0,0,0.05);
    }
    .stAlert.info { background-color: #e0f7fa; border-left: 5px solid #00BCD4; } /* Cyan */
    .stAlert.success { background-color: #e8f5e9; border-left: 5px solid #4CAF50; } /* Green */
    .stAlert.warning { background-color: #fffde7; border-left: 5px solid #FFC107; } /* Amber */

    /* Dataframe styling */
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Custom Title with your name and creative emojis
st.markdown(
    """
    <h1 style='text-align: center;'>
        🤖 Seamless Sign-ups by Pallavi (AI-Driven) 
    </h1>
    <h3 style='text-align: center;'>
        Your personal assistant for seamless user management
    </h3>
    <p style='text-align: center;'>
        Hello, I'm your AI assistant, ready to help you manage registrations!
    </p>
    """,
    unsafe_allow_html=True
)

st.write("---") # Separator

st.markdown("#### Try out some examples:")

# Dropdown for example prompts
example_prompts = {
    "Register a new user": "Register user with email user@example.com and DOB 2000-01-01",
    "Register another user": "Register user with email user@example.com and DOB 2000-01-01",
    "Show all registrations": "Show all registrations",
    "List registered users": "List all users"
}

selected_example = st.selectbox(
    "Choose an example prompt:",
    options=[""] + list(example_prompts.keys()),
    format_func=lambda x: x if x else "Select an example..."
)

# Text input for user query
user_input = st.text_input(
    "Or type your own request here:",
    value=example_prompts.get(selected_example, ""), # Populate with selected example
    placeholder="e.g. 'Register Pallavi with pallavi@example.com and DOB 2003-08-02'" # Updated placeholder
)

# Submit button
if st.button("Submit Request", use_container_width=True, type="primary"):
    if user_input:
        async def process_input():
            async with mcp_client:
                prompt_parts = [
                    "Your job is to choose and call the appropriate tool from the available tools below to fulfill the user's request.",
                    "Respond ONLY by calling the tool, DO NOT answer directly.",
                    "",
                    "Available tools:",
                    "1. `store_data(name: str, email: str, dob: str)`: Use this tool to register a new user by saving their name, email, and date of birth (DOB) to a CSV file.",
                    "   Example usage: `store_data(name='John Doe', email='john.doe@example.com', dob='1990-05-15')`",
                    "   Only call `store_data` if the user explicitly asks to register a new user and provides all three pieces of information (name, email, DOB).",
                    "   If the user is already registered, do not call the tool again.",
                    "",
                    "2. `fetch_data()`: Use this tool to retrieve and display all previously stored user data from the CSV file.",
                    "   Example usage: `fetch_data()`",
                    "   Call `fetch_data` when the user asks to see all registrations, list users, or similar queries.",
                    "",
                    f"User Input: {user_input}"
                ]

                response = await gemini_client.aio.models.generate_content(
                    model="models/gemini-2.0-flash",
                    contents=[{"role": "user", "parts": [{"text": "\n".join(prompt_parts)}]}],
                    config=genai.types.GenerateContentConfig(
                        temperature=0.2,
                        tools=[mcp_client.session],
                    )
                )
                return response
        
        with st.spinner("Processing your request..."):
            llm_response = asyncio.run(process_input())

        st.markdown("---")
        st.markdown("#### LLM Response:")

        # Flag to track if fetch_data was explicitly called or inferred
        fetch_data_called_or_inferred = False
        llm_text_response_displayed = False # New flag to ensure text is displayed only once if needed

        if llm_response and llm_response.candidates:
            for candidate in llm_response.candidates:
                if candidate.content and candidate.content.parts:
                    for part in candidate.content.parts:
                        # Display LLM's text response if it exists and isn't displayed yet
                        # Added explicit check for part.text being not None
                        if hasattr(part, 'text') and part.text is not None:
                            llm_text = part.text.lower()
                            if not llm_text_response_displayed: # Only display text once
                                st.info(f"LLM said: {part.text}")
                                llm_text_response_displayed = True
                            
                            # Check if the LLM's text response indicates a fetch operation
                            if "list" in llm_text or "show" in llm_text or "retrieve" in llm_text or "users" in llm_text or "registrations" in llm_text:
                                fetch_data_called_or_inferred = True
                        
                        # Handle explicit tool calls
                        if hasattr(part, 'function_call') and part.function_call is not None:
                            # Display tool call details only if it's a valid call
                            st.success("Tool Call Detected!")
                            tool_call = part.function_call
                            st.write(f"Function Name: `{tool_call.name}`")
                            st.write(f"Arguments: `{tool_call.args}`")

                            # Dynamically import and execute the tool call
                            try:
                                if tool_call.name == "store_data":
                                    from tools.store import store_data
                                    result = store_data(
                                        name=tool_call.args.get('name'),
                                        email=tool_call.args.get('email'),
                                        dob=tool_call.args.get('dob')
                                    )
                                    if "already registered" in result.lower():
                                        st.warning(f"Tool execution result: {result}")
                                    else:
                                        st.success(f"Tool execution result: {result}")
                                elif tool_call.name == "fetch_data":
                                    # Set flag if fetch_data was explicitly called
                                    fetch_data_called_or_inferred = True
                                    # The actual display will happen after the loop or in a dedicated block
                                else:
                                    st.warning(f"Unknown tool called: {tool_call.name}")
                            except ImportError as ie:
                                st.error(f"Error importing tool: {ie}. Make sure tools are in the 'tools' directory.")
                            except Exception as e:
                                st.error(f"Error executing tool {tool_call.name}: {e}")
                        # Removed the specific warning for 'function_call is None'
                        # elif hasattr(part, 'function_call') and part.function_call is None:
                        #     st.warning("LLM attempted a function call but provided no details.")
                else:
                    # This warning is less critical and can remain for debugging unexpected LLM structures
                    st.warning("No content or parts in LLM response.")
        else:
            st.warning("No response from LLM.")
        
        # --- Display fetched data in a table if inferred or explicitly called ---
        if fetch_data_called_or_inferred:
            try:
                from tools.fetch import fetch_data
                users_data = fetch_data() # Call fetch_data here to ensure data retrieval
                
                st.markdown("##### Registered Users Data:")
                if users_data:
                    df = pd.DataFrame(users_data)
                    df.insert(0, 'S.No.', range(1, 1 + len(df))) # Add S.No. column starting from 1
                    st.dataframe(df, use_container_width=True) # Display as interactive table
                else:
                    st.info("No registered users found.")
            except ImportError as ie:
                st.error(f"Error importing fetch_data tool: {ie}.")
            except Exception as e:
                st.error(f"Error displaying fetched data: {e}")

    else:
        st.warning("Please enter a request or select an example.")

