# Projet d'Analyse des Avis Clients avec FastAPI

## Description

Ce projet permet d'extraire, analyser et résumer les avis clients sur une entreprise en utilisant FastAPI, scraping, analyse de sentiment et modèles LLM.
Il demande à l'utilisateur de donner un url ou le nom d'un entreprise pour donner un résumé des avis clients et aussi un graphique montrant la répartition des sentiments : positif, négatif et neutre.

## Fonctionnalités

- Scraping des avis depuis Trustpilot

- Analyse de sentiment des avis avec DistilBERT

- Génération de résumé avec Gemini

- Visualisation des sentiments sous forme de graphique

API REST avec FastAPI

## Installation et Exécution

### 1. Cloner le projet

`git clone https://github.com/scapp-trustpilot.git`

`cd scapp-trustpilot`

### 2. Installer les dépendances

` pip install -r requirements.txt`

### 3. Lancer l'API

`uvicorn api:app --host 0.0.0.0 --port 8000`

L'API sera accessible sur http://127.0.0.1:8000/docs.


## Utilisation avec Docker

### 1. Construire l'image Docker

` docker build -t sentiment-api .`

### 2. Lancer le conteneur

` docker run -p 8000:8000 sentiment-api`

L'API sera accessible depuis l'hôte et d'autres machines sur le réseau.

## Points Importants

-API en FastAPI : api.py

-Scraping des avis : scrap.py

-Analyse de sentiment : sentiment.py

-Génération de résumé : resume.py

-Génération de graphiques : interface.py

-Configuration Docker : Dockerfile

## Exemple d'Appel API

POST /analyze_reviews

Requête :

{
  "query": "amazon.fr" ou "amazon"
}

Réponse :

{
  "entreprise": "Amazon",
  "note": "4.5",
  "summary": "Les clients apprécient la livraison rapide, mais critiquent le service client.",
}


POST /sentiment_chart

Requête :

{
  "query": amazon
}

"sentiments": "...image..."




## Auteur

👤 Mouhamed DIALLO  

