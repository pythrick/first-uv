"""Main module for running the FastAPI application."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("first_uv:app", host="127.0.0.1", port=8000, reload=True)
