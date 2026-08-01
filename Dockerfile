# syntax=docker/dockerfile:1.7

# Build stage for installing dependencies
FROM python:3.12-slim AS builder

# Environment variables to prevent Python from writing pyc files to disk
# and to ensure unbuffered mode for better logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy requirements first to maximize layer cache reuse
COPY requirements.txt .

# Cache downloaded packages between BuildKit builds
RUN --mount=type=cache,target=/root/.cache/pip \
    python -m pip install \
        --prefix=/install \
        --no-warn-script-location \
        -r requirements.txt


# Runtime stage containing only the application and production dependencies
FROM python:3.12-slim AS runtime

LABEL maintainer="Nilton Pimentel <contato@niltonpimentel.com.br>"

# Environment variables to prevent Python from writing pyc files to disk
# and to ensure unbuffered mode for better logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Create a new user to run the app
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy installed dependencies from the builder stage
COPY --from=builder /install /usr/local/

# Remove the package installer from the final runtime image
RUN python -m pip uninstall --yes pip

# Copy source code after dependencies are installed
COPY --chown=appuser:appuser . .

# Switch to the unprivileged user
USER appuser

EXPOSE 8000

CMD ["gunicorn", "nilton_pimentel.wsgi:application", "--bind", "0.0.0.0:8000", "--worker-class", "gthread", "--workers", "2", "--threads", "2", "--timeout", "80", "--max-requests", "1000", "--max-requests-jitter", "100"]
