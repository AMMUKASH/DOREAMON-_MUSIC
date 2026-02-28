FROM python:3.11-slim-buster

# System dependencies setup
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg git python3-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

# Python requirements install karna
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Bot ko start karne ki command
CMD ["bash", "start"]
