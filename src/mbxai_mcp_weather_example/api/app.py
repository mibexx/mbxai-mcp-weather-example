from fastapi import FastAPI, Body
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel
from typing import Any
from ..config import get_config

config = get_config()

# Import the weather tool
from ..project.weather import get_weather

# Create FastAPI app
app = FastAPI(
    title=config.name,
    description="A Model Context Protocol (MCP) tool server",
    version="0.1.0",
)

# Initialize MCP server
mcp_server = FastMCP(config.name)

# Register the weather tool with the MCP server
mcp_server.add_tool(get_weather)


# Legacy endpoints for backward compatibility
@app.get("/tools")
async def get_tools():
    """Get all available MCP tools."""
    # Use the list_tools() method to get the tools
    tools = await mcp_server.list_tools()
    return tools


class ToolRequest(BaseModel):
    """Base model for tool requests."""

    parameters: dict[str, Any] = {}


@app.post("/tools/{tool_name}/invoke")
async def invoke_tool(tool_name: str, request: ToolRequest = Body(...)):
    """Invoke a specific MCP tool."""
    try:
        result = await mcp_server.call_tool(tool_name, **request.parameters)
        return result
    except Exception as e:
        return {"error": f"Error invoking tool {tool_name}: {str(e)}"}
