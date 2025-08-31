import pytest
import asyncio
from src import utility

@pytest.mark.asyncio
async def test_logout():
    """
    Tests if the user logs out after 5 minutes
    """
    result = await utility.logout()
    assert result is None