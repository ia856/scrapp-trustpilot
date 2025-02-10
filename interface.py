import sentiment
from fastapi.responses import JSONResponse, StreamingResponse
import matplotlib.pyplot as plt
import io
import pandas as pd


def generate_chart(donnee):
  #Vérification du nom de l'entreprise
    donnee=sentiment.class_sentiment(donnee)
    if not donnee:
        return JSONResponse(status_code=404, content={
            "message": f"Aucune entreprise trouvée pour '{donnee}'. Vérifiez l'orthographe."
        })

  
    counts = pd.Series(donnee).value_counts()

    categories = ["Positif", "Neutre", "Négatif"]
    counts = counts.reindex(categories, fill_value=0)  # Ajoute les catégories manquantes avec 0

    # Définir un dictionnaire de couleurs fixes
    color_map = {"Positif": "green", "Négatif": "red", "Neutre": "gray"}

    # Création du graphique
    plt.figure(figsize=(5, 3))
    counts.plot(kind='bar', color=[color_map[c] for c in categories])  # Couleurs fixes

    plt.xlabel("Sentiment")
    plt.ylabel("Nombre d'avis")
    plt.title("Répartition des sentiments")

    # Sauvegarde en mémoire
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return StreamingResponse(img, media_type="image/png")