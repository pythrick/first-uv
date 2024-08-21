"""Test application creation."""


async def test_index(client):
    """Test the index route."""
    response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
