"""Pytest configuration."""

import fastapi
import httpx
import pytest


@pytest.fixture
def app() -> fastapi.FastAPI:
    """Create a FastAPI application."""
    from first_uv.app import create_app

    return create_app()


@pytest.fixture
async def client(app: fastapi.FastAPI):
    """Create a FastAPI test client."""
    async with httpx.AsyncClient(
        transport=httpx.ASGITransport(app=app),
        base_url="http://testserver",
    ) as client:
        yield client
