FROM python:3.10

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y \
    build-essential \
    libglib2.0-0 \
    libxrender1 \
    libxext6 \
    libsm6 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask pandas rdkit-pypi

EXPOSE 8000

CMD ["python", "app.py"]
