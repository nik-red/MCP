import os
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient

async def main():
    # Correctly initialized client
    client = MultiServerMCPClient(
        {
            "duckduckgo_mcp_stdio": {
                "transport": "stdio",
                "command": "uvx",
                "args": ["duckduckgo-mcp-server"]
            }
        }
    )

    
    tools = await client.get_tools()
    for tool in tools:
        print("Tool Name:", tool.name, 
              "Description:", tool.description)
    
    # call the fetch tool
    search_tool = tools[0]
    search_result = await search_tool.ainvoke({"query": "What is the capital of Bulgaria?"})
    print("Search Result:", search_result)

if __name__ == "__main__":
    asyncio.run(main())