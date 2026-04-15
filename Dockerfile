FROM python:3.12-slim

LABEL maintainer="Nilton Pimentel <contato@niltonpimentel.com.br>"

# Environment variables to prevent Python from writing pyc files to disc
# and to ensure unbuffered mode for better logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Create a new user to run the app
RUN useradd --create-home --shell /usr/sbin/nologin appuser

# Copy requirements first to maximize layer cache reuse
COPY requirements.txt .

# Install Python dependencies
RUN pip install wheel && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code after dependencies are installed
COPY --chown=appuser:appuser . .

# Switch to the unprivileged user
USER appuser

EXPOSE 8000

CMD ["gunicorn", "nilton_pimentel.wsgi:application", "--bind", ":8000", "--threads", "1", "--timeout", "80", "--workers", "2"]
