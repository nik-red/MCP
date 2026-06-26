import os
import asyncio
from mcp.client.stdio import stdio_client
from mcp import client, ClientSession, StdioServerParameters   

# Path to the MCP server script
mcp_server_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "1_first_mcpserver_stdio.py")

# Create server parameters for the stdio transport
server_params = StdioServerParameters(
    command = 'python',
    args = [str(mcp_server_path)],
    env = {}
)

# Create a client session to connect to the MCP server
async def main():
   
    async with stdio_client(server_params) as (read, write):
        
        async with ClientSession(read, write) as session:

            await session.initialize()
            # Fetch the tools
            tools = await session.list_tools()
            print("Available tools:", tools)

            # Use the fetch tool
            result = await session.call_tool("process",arguments={"path": "/path/to/data"})
            print("Result:", result)

if __name__ == "__main__":
    asyncio.run(main())