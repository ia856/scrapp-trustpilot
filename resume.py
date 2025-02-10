
from scrap import extract_reviews as list_commentaires

from langchain.prompts import PromptTemplate
import google.generativeai as genai
import pandas as pd

# Ma clé API
genai.configure(api_key="AIzaSyDQWWJzPQicXnl4EVWKkWn_205-RxyMfyo")

# Fonction pour générer le résumé des commentaires à l'aide de Gemini
def generateur_resume_gemini(comments_texte):
    """ Utilise Gemini pour générer un résumé des commentaires. """

    model = genai.GenerativeModel("gemini-1.5-flash")  # Remplacer par le modèle adapté si nécessaire

    # Demander à Gemini de générer un résumé à partir des commentaires
    response = model.generate_content(f"Voici une série de commentaires sur une entreprise :\n\n{comments_texte}\n\nVeuillez générer un résumé clair et concis des points clés.")

    # Extraire et retourner le résumé
    resultat = response.text.strip()
    return resultat

# Définir le modèle de prompt pour l'analyse des commentaires
prompt_template = PromptTemplate(
    input_variables=["comments_data"],
    template="""
    Vous êtes un analyste de feedbacks sur une entreprise.
    Voici les commentaires suivants sur l'entreprise :\n{comments_data}

    Ne pas réécrire les commentaires et veuillez générer un résumé clair et concis des points suivants :
    1. Identifiez les aspects les plus appréciés par les clients.
    2. Identifiez les principaux problèmes soulevés par les clients.

    """
)

def analyze_comments_avec_gemini(comments_data):
    """ Utilise directement Gemini pour analyser et résumer les commentaires. """
    comments_data = list_commentaires(comments_data)
    if not comments_data :
        return f"Il n'ya pas de données pour faire un résumé"
    # Convertir les données en chaîne de caractères (assurez-vous que comments_data est un DataFrame ou une chaîne formatée)
    comments_string = '\n'.join(comments_data) # Si tu as un DataFrame

    # Formater les données avec le modèle de prompt
    formatted_input = prompt_template.format(comments_data=comments_string)

    # Résumer les commentaires à l'aide de Gemini
    summary = generateur_resume_gemini(formatted_input)

    return f"Résumé des commentaires :\n{summary}.strip()"
