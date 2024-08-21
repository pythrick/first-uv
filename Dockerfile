FROM python:3.12-slim-bullseye
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app
COPY pyproject.toml uv.lock README.md ./
RUN mkdir -p src/first_uv
RUN touch src/first_uv/__init__.py
RUN uv sync

COPY . .

CMD ["uv", "run", "uvicorn", "first_uv:app", "--host", "0.0.0.0", "--port", "8000"]
