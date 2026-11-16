
FROM mcr.microsoft.com/playwright/python:v1.56.0-noble

WORKDIR /app

RUN apt-get update && apt-get install -y \
    xvfb \
    x11vnc \
    novnc \
    websockify \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p reports test-results auth

ENV DISPLAY=:99

EXPOSE 6080

CMD ["pytest", "-v", "tests/"]
