import pytest
from mbxai_mcp_weather_example.project.weather import get_weather

@pytest.mark.asyncio
async def test_get_weather():
    result = await get_weather("London")
    assert isinstance(result, dict)
    assert "location" in result
    assert "temperature" in result
    assert "condition" in result
    assert "humidity" in result
    assert result["location"] == "London" 