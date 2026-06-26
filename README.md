# MCP Python Server - Streamable HTTP

A simple **Model Context Protocol (MCP)** server built using **FastMCP** that exposes multiple tools over **Streamable HTTP**. This project demonstrates how AI assistants (such as Claude Desktop, LangChain Agents, Cursor, or any MCP-compatible client) can discover and execute Python functions as tools.

---

## Features

* Streamable HTTP transport
* Automatic tool discovery
* Execute Bash commands
* Execute Python code
* Execute Python files
* Read and write files
* Search files using glob patterns
* Search text inside files
* Create and delete folders

---

## Project Structure

```text
.
├── server.py          # Starts the MCP HTTP Server
├── tools.py           # Tool definitions exposed to MCP clients
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Available Tools

### `bash(command: str)`

Executes a Bash/Command Prompt command and returns the output.

Example:

```python
bash("dir")
```

---

### `python_code(code: str)`

Executes Python code directly.

Example:

```python
python_code("print('Hello MCP')")
```

---

### `python_file(file: str)`

Runs a Python script.

Example:

```python
python_file("sample.py")
```

---

### `glob(pattern: str)`

Returns files matching a pattern.

Example:

```python
glob("*.py")
```

---

### `grep(pattern: str, file: str)`

Searches for matching text inside a file.

Example:

```python
grep("TODO", "notes.txt")
```

---

### `read_file(file: str)`

Reads the contents of a file.

---

### `write_file(file: str, content: str)`

Creates or overwrites a file with the provided content.

---

### `create_folder(folder: str)`

Creates a directory.

---

### `delete_folder(folder: str)`

Deletes an existing directory.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/nik-red/MCP.git
cd MCP
```

Create a virtual environment:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the MCP server:

```bash
python server.py
```

The server starts using **Streamable HTTP** on:

```text
http://localhost:8050
```

---

## Testing with MCP Inspector

Install MCP Inspector (if not already installed):

```bash
npx @modelcontextprotocol/inspector
```

Connect to:

```text
http://localhost:8050
```

You can:

* Discover available tools
* Execute tools interactively
* Inspect requests and responses
* Verify tool metadata

---

## How It Works

1. The server starts and registers all functions decorated with `@mcp.tool()`.
2. An MCP client connects using the Streamable HTTP protocol.
3. The client requests the list of available tools.
4. FastMCP automatically generates tool metadata from the Python function signatures and docstrings.
5. When a tool is invoked, FastMCP executes the corresponding Python function and returns the result to the client.

---

## Technologies Used

* Python 3.x
* FastMCP
* Model Context Protocol (MCP)
* Streamable HTTP

---

## Learning Objectives

This project demonstrates:

* Building an MCP Server
* Creating custom MCP tools
* Tool discovery
* Streamable HTTP transport
* Function execution through MCP
* Integrating AI agents with Python applications

---

## Future Improvements

* Add authentication
* Restrict dangerous shell commands
* Add logging
* Improve error handling
* Deploy as a Databricks App or Docker container
* Add Databricks, Azure, and SQL tools
* Package and publish reusable tools to PyPI

