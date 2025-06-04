# Utilise une image Python officielle légère
FROM python:3.12-slim

WORKDIR /app

# Copie les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie le code source
COPY src/ src/

# Par défaut, lance le programme principal
CMD ["python", "src/main.py"]
