# Render ke liye updated aur stable image
FROM nikolaik/python-nodejs:python3.11-nodejs19

# System dependencies aur cleanup
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends ffmpeg aria2 git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Working directory set karein
WORKDIR /app
COPY . /app/

# Pip upgrade aur requirements install karein
RUN python3 -m pip install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

# Bot ko start karne ki command
CMD ["bash", "start"]
