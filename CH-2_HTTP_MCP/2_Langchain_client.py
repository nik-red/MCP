import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

# Create the dynamic path to the MCP server script
mcp_server_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "CH-1_CreateMCP","1_first_mcpserver_stdio.py")

# Path to venv python executable
venv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".venv")

async def main():
    # Correctly initialized client
    client = MultiServerMCPClient(
        {
            "data_fetch_mcp_stdio": {
                "transport": "stdio",
                "command": os.path.join(venv_path, "Scripts", "python.exe"),
                "args": [str(mcp_server_path)]
            },
            "data_fetch_mcp_http": {
                "transport": "streamable-http",
                "url": "http://localhost:8050/mcp"
            }
        }
    )

    
    tools = await client.get_tools()
    print("Available tools:", tools)

if __name__ == "__main__":
    asyncio.run(main())