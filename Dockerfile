FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy project files
COPY . .

# Install the package
RUN pip install .

# Create directories for data
RUN mkdir -p results dataflows

ENTRYPOINT ["python", "-m", "cli.main"]
