from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrap import extract_reviews, name_and_note
from interface import generate_chart
from resume import analyze_comments_avec_gemini
import logging

app = FastAPI()

logging.basicConfig(level=logging.DEBUG)

class ReviewRequest(BaseModel):
    query: str  # Peut être une URL ou un nom d'entreprise

@app.post("/analyze_reviews")
def analyze_reviews(request: ReviewRequest):
    query = request.query
    logging.debug(f"Reçu la requête avec query: {query}")
    # Récupérer la note et le nom de l'entreprise
    note, entreprise = name_and_note(query)
    if not entreprise:
        raise HTTPException(status_code=404, detail="Entreprise introuvable.")
    
    # Extraire les avis
    reviews = extract_reviews(query)
    if not reviews:
        raise HTTPException(status_code=404, detail="Aucun avis trouvé.")
    
    # Analyser le sentiment des avis
    
    sentiments = generate_chart(query)
    
    # Générer un résumé des avis
    summary = analyze_comments_avec_gemini(query)
    
    return {
        "entreprise": entreprise,
        "note": note,
        "summary": summary,
    }


@app.get("/sentiment_chart/{query}")
def get_chart(query: str):
    return generate_chart(query)