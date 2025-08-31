import pytest

from src import utility

@pytest.mark.asyncio
async def test_logout():
    result = await utility.logout()
    assert result is None
