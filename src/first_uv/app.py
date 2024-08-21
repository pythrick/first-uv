"""Module containing the application factory."""

from fastapi import FastAPI


def create_app() -> FastAPI:
    """Create the FastAPI application."""
    app = FastAPI()

    @app.get("/")
    def index():
        """Return a simple message."""
        return {"message": "Hello, World!"}

    return app
