FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y \
    mc \
    curl \
    procps \
    python3-dev \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install --no-cache-dir --upgrade pip

WORKDIR /app
COPY . /app/

RUN pip3 install --no-cache-dir .

RUN python ComponentSpellcheckerServiceSetup.py

RUN chmod +x start.sh

EXPOSE 9699

CMD ["./start.sh"]
