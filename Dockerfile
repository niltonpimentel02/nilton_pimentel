FROM python:3.11-slim

LABEL maintainer="Nilton Pimentel <contato@niltonpimentel.com.br>"

# Set working directory
WORKDIR /app

# Copy source code to container
COPY . .

# Install system dependencies and clean up
RUN apt update -y && \
    apt upgrade -y && \
    apt autoremove -y && \
    apt clean && \
    rm -rf /var/lib/apt/lists/*

# Install Python dependencies
RUN pip install wheel && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements-dev.txt

EXPOSE 8000
