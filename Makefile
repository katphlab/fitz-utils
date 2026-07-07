install:
	uv sync --all-extras --all-groups
	uv run pre-commit install
	uv run pre-commit autoupdate

test:
	uv run pytest

lint:
	uv run ruff format --check .
	uv run mypy .
