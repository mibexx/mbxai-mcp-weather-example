from typing import Any
from mcp.server.fastmcp import FastMCP

# Create a FastMCP instance for this module
mcp = FastMCP("weather")

@mcp.tool()
async def get_weather(location: str) -> dict[str, Any]:
    """Get weather information for a location."""
    # This is a mock implementation
    return {
        "location": location,
        "temperature": 20,
        "condition": "sunny",
        "humidity": 65,
    }