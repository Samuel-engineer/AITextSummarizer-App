import streamlit as st
from src.model import load_model
from src.summarizer import summarize_text

# Chargement du modèle et du tokenizer
st.title("Résumé Financier avec Pegasus")

st.write("Entrez un texte financier et obtenez un résumé optimisé grâce au modèle Pegasus.")

# Initialisation du modèle
@st.cache_resource()
def get_model():
    return load_model()

tokenizer, model = get_model()

# Champ de saisie du texte
txt_input = st.text_area("Texte à résumer", "")

# Curseur pour choisir la longueur du résumé
max_length = st.slider("Longueur max du résumé", min_value=20, max_value=100, value=50, step=5)

# Bouton pour générer le résumé
if st.button("Générer le résumé"):
    if txt_input.strip():
        summary = summarize_text(txt_input, tokenizer, model, max_length)
        st.subheader("Résumé ou idée principale généré")
        st.write(summary)
    else:
        st.warning("Veuillez entrer un texte avant de générer un résumé.")
