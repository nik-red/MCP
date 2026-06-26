import os
import asyncio
from unittest import result
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
load_dotenv()


async def main():
    # Correctly initialized client
    client = MultiServerMCPClient(
        {
            "tavily-remote-mcp": {
                "transport": "streamable-http",
                "url": f"https://mcp.tavily.com/mcp/?tavilyApiKey={os.getenv('tavily_api_key')}"
            }
        }
    )

    
    tools = await client.get_tools()
    print("Available Tools:", len(tools))

    tool_research = [tool for tool in tools if tool.name == "tavily_research"][0]

    # Pass the query string directly as the value for the "input" key
    result = await tool_research.ainvoke({
    "input": "What will be the future of Data Engineers with AI?"
    })

    print("Research Result:", result)

    for tool in tools:
        print("Tool Name:", tool.name, 
              "Description:", tool.description)
    

if __name__ == "__main__":
    asyncio.run(main())