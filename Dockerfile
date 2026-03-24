FROM python:3.13-slim

WORKDIR /app

RUN apt-get update && apt-get install -y     git     curl     && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY . .

RUN pip install .

RUN mkdir -p results dataflows

CMD ["python", "-m", "cli.main"]
