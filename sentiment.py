from scrap import extract_reviews as list_commentaires
from transformers import pipeline

def class_sentiment(donnees):
  donnees=list_commentaires(donnees)
  if not donnees:
    return None
  # Chargement du modèle pré-entraîné DistilBERT pour l'analyse de sentiment
  classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment",truncation=True, max_length=512)
  resultat=classifier(donnees)
  # On sait que DistilBERT retourne comme resultat une liste d'un dictionnaire contenant un label et un score
  # On va définir une fonction permettant de retourner Positif, Négatif ou Neutre
  def Class_note(resultat):
    a = [int(res['label'][0]) for res in resultat]
    for i in range(len(a)) :
      if a[i] >= 4.0:
        a[i]="Positif"
      elif a[i]==3:
        a[i]="Neutre"
      else :
        a[i]="Négatif"
    return a
  return Class_note(resultat)