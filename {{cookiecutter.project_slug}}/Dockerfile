# Install Python dependencies
FROM python:3.13.0-bookworm AS python-base

ENV LC_CTYPE=C.utf8 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    UV_PROJECT_ENVIRONMENT="/app/.venv" \
    UV_PYTHON_INSTALL_DIR="/python" \
    UV_COMPILE_BYTECODE=1

WORKDIR /app

# Install uv

COPY --from=ghcr.io/astral-sh/uv:0.4 /uv /usr/local/bin/uv

# Install Python dependencies

COPY ./pyproject.toml ./uv.lock /app/

RUN uv sync --frozen --no-dev --no-install-project

ENV PATH="/app/.venv/bin:$PATH"

# Build static assets

FROM python-base AS staticfiles

COPY . /app

RUN python manage.py tailwind build && \
    python manage.py collectstatic --no-input

FROM python-base AS webapp

COPY --from=staticfiles /app/staticfiles /app/staticfiles

COPY . /app
