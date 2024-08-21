
lint:
	uv run pre-commit install
	uv run pre-commit run -a -v

update:
	uv lock --upgrade
	uv run pre-commit autoupdate -j 10

sync:
	uv sync --all-extras

test:
	uv run pytest

build:
	docker compose build

run:
	docker compose up
