import requests
from bs4 import BeautifulSoup as bs
import re
import unidecode
import emoji
def normalize_string(s):
    s=unidecode.unidecode(s)
    string_normalise=s.replace("_","").replace("-","").replace(" ","")
    return string_normalise.lower()

def recup_link(donnee):
    # Expression régulière pour la vérification d'un lien
    regex=r'^(https?://)?([a-z0-9]+([-.])*[a-z0-9]+)*(\.[a-z]{2,})+(/.*)?$'


    if re.match(regex,donnee):
        try:

            response=requests.get(donnee)

            if response.status_code == 200:
              match=re.search(r'^(https?://)?(www\.)?([a-z0-9]+([-.])*[a-z0-9]+)*(\.[a-z]{2,})', donnee)
              if match:
                  domain=match.group(3)
                  return domain.split('.')[0]
              else:
                return f"Erreur : domaine non valide"
            else:
                return f"Le lien ne fonction pas vérifi ton lien"

        except requests.exceptions.RequestException as e:
            return f"Erreur lors de la requete : {e}"


    else:

        donnee_normalise=normalize_string(donnee)
        return donnee_normalise

def fetch_html(donnee):
    domain=recup_link(donnee)
    link=[f"https://fr.trustpilot.com/review/{domain}.fr", f"https://fr.trustpilot.com/review/{domain}.com"]

    # Récupère le contenu HTML d'une page donnée.
    for url in link:
      try:
          headers = {'User-Agent': 'Mozilla/5.0'}
          response = requests.get(url, headers=headers, timeout=10)
          response.raise_for_status()
          if response.status_code == 200:
                return bs(response.content, "html.parser")
          
      except requests.exceptions.RequestException as e:
            continue
    return None

def name_and_note(donnee):
  html=fetch_html(donnee)
  if html is None:
        return None, None
  note=html.find('p',{'class':'typography_body-l__v5JLj'})
  entreprises=html.find('span',{'class':'typography_display-s__pKPhT'})
  return note.text, entreprises.text.strip()

def extract_reviews(donnee):
    """Extrait les avis clients depuis une page Trustpilot."""
    html = fetch_html(donnee)
    if not html:
        return []
    
    commentaires= []
    for review in html.find_all('p', {'class': 'typography_body-l__v5JLj'}):
        commentaires.append(emoji.replace_emoji(review.get_text(strip=True),' '))
    
    return commentaires[2:]
