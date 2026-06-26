from fastmcp import FastMCP

# create a new instance of FastMCP
mcp = FastMCP()

@mcp.tool()
def fetch():
    '''Use this tool to fetch data from the source.'''

    # fetch data from the source and return it
    '''You can make the API Calls here to fetch the data from the source/database.'''
    return { "data": "Hello, MCP!" }

@mcp.tool()
async def process(path:str):
    '''Use this tool to process the fetched data.'''

    # Simulate processing the fetched data
    ''' You can perform some data transformations here '''
    return {"processed_data": "Data has been processed! at path: " + path}


if __name__ == "__main__":
    # run the MCP server
    mcp.run(transport="stdio")