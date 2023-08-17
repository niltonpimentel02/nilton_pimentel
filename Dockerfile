FROM python:3.11-slim

LABEL maintainer="Nilton Pimentel <contato@niltonpimentel.com.br>"

# Environment variables to prevent Python from writing pyc files to disc
# and to ensure unbuffered mode for better logging
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /app

# Create a new user 'appuser' without a home directory and switch to it
RUN useradd appuser && chown -R appuser /app
USER appuser

# Copy source code to container
COPY . .

# Switch back to root to install system and Python dependencies
USER root

# Install system dependencies and clean up
RUN apt update -y && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install wheel && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Switch back to appuser
USER appuser

EXPOSE 8000
