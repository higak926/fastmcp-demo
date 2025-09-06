## Introduction

This repository is a demo of FastMCP.  
For details on FastMCP, please refer to the link below.
https://github.com/jlowin/fastmcp

## setup

This project uses Python 3.12.0.  
Also, following the official tutorial, we use **uv** for package management, so please set up uv as well.  
https://modelcontextprotocol.io/quickstart/server

We have also included a tool called **mcptools** so that you can easily verify the server set up with FastMCP from your client. Please refer to the following for installation instructions.
https://github.com/f/mcptools

The code in this repository uses the **gemini API**.
Please refer to the following website to set your API key.
https://ai.google.dev/gemini-api/docs/api-key?hl=ja  
※ please manage your API key carefully so that it is not leaked to outside parties.

## start app

Once you have completed these settings, start the MCP server with the following command.

```
uv run main.py
```

And you can verify the MCP server in your browser by launching mcptools with the following command.

```
mcp web http://127.0.0.1:8000/sse
```

<img width="1190" height="523" alt="FastMCP" src="https://github.com/user-attachments/assets/60f59028-e53f-4b28-8a7a-454ea3de2d5b" />

Have a great development experience!
