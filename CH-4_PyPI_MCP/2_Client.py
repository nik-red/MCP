import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    # Correctly initialized client
    client = MultiServerMCPClient(
        {
            "agentic_terminal": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["agentic-terminal"]
            }
        }
    )
    
    tools = await client.get_tools()
    for tool in tools:
        print("Available Tool Name:", tool.name)
    

if __name__ == "__main__":
    asyncio.run(main())