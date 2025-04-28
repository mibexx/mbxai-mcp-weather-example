import uvicorn
import asyncio
from .app import app, mcp_server

async def async_main():
    """Run the FastAPI application with MCP server."""
    # Get available tools using the list_tools() method
    tools = await mcp_server.list_tools()
    
    # Extract tool names from the Tool objects
    tool_names = [tool.name for tool in tools]
    print(f"Available tools: {', '.join(tool_names)}")
    
    # Run the server
    config = uvicorn.Config(app, host="0.0.0.0", port=5000)
    server = uvicorn.Server(config)
    await server.serve()

def main():
    """Entry point for the application."""
    asyncio.run(async_main())

if __name__ == "__main__":
    main() 