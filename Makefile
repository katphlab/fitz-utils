install:
	uv sync --all-extras
	uv run pre-commit install
	uv run pre-commit autoupdate

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run ruff format --check .
