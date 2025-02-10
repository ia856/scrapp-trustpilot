# On utilise une image Python officielle comme base
FROM python:3.10-slim

# Le répertoire de travail dans le conteneur
WORKDIR /app

# Copie des fichiers nécessaires 
COPY requirements.txt /app

# Installation des dépendances
RUN pip install --no-cache-dir -r requirements.txt
 
COPY . /app
# Le port qu'on utiliseras pour l'API par défaut FastAPI écoute sur le port 8000
EXPOSE 8000

# Commande pour démarrer l'application avec Uvicorn (le serveur ASGI pour FastAPI)
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
