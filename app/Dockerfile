FROM python:3.11-slim

WORKDIR /app

# Copier requirements (s'il existe) ou installer directement
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code
COPY app.py .

# Lancer l'app
CMD ["python", "app.py"]