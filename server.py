from fastmcp import FastMCP
# Import tools from the 'tools' package
from tools.fetch import fetch_data
from tools.store import store_data

# Initialize the MCP server
mcp = FastMCP("Registration APP")

# Register tools with descriptions for the LLM
mcp.tool(description="""Register a new user by saving their info to a CSV.
The tool takes 'name' (string), 'email' (string), and 'dob' (string, format YYYY-MM-DD) as arguments.
Example: "Register John Doe with email john.doe@example.com and DOB 1990-05-15"
""")(store_data)

mcp.tool(description="""
This tool fetches all previously stored user data from the CSV file and formats it for display.
Example: "Show all registrations" or "List all users"
""")(fetch_data)

if __name__ == "__main__":
    # Run the MCP server using the streamable-http transport
    # This makes the server accessible via HTTP for the client (llm.py)
    mcp.run(transport="streamable-http")

