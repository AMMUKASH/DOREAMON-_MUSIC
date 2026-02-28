FROM python:3.11-slim-buster

# System dependencies install karein
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg git python3-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Requirements install karein
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Bot start command
CMD ["bash", "start"]
