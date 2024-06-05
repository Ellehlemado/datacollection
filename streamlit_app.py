import streamlit as st
import pandas as pd
import math
from pathlib import Path
import os

# Chemins vers les fichiers de données
cleaned_data_path = 'scraped_data.csv'
raw_data_path = 'web_scraper_raw_data.csv'

# Charger les données si les fichiers existent
cleaned_data = pd.read_csv(cleaned_data_path) if os.path.exists(cleaned_data_path) else pd.DataFrame()
raw_data = pd.read_csv(raw_data_path) if os.path.exists(raw_data_path) else pd.DataFrame()

# Configuration de la page
st.set_page_config(page_title="Dashboard des Animaux", layout="wide")

# Titre de l'application
st.title("Dashboard des Animaux")

# Sidebar pour la navigation
st.sidebar.header("Navigation")
options = ["Voir les données nettoyées", "Voir les données non nettoyées", "Formulaire d'évaluation"]
choice = st.sidebar.selectbox("Choisissez une option", options)

if choice == "Voir les données nettoyées":
    st.header("Données Nettoyées")
    if not cleaned_data.empty:
        st.dataframe(cleaned_data)
    else:
        st.write("Aucune donnée nettoyée disponible.")

elif choice == "Voir les données non nettoyées":
 st.header("Données Nettoyées")
    if not cleaned_data.empty:
        st.dataframe(cleaned_data)
 else:
        st.write("Aucune donnée nettoyée disponible.")

elif choice == "Voir les données non nettoyées":
    st.header("Données Non Nettoyées")
    if not raw_data.empty:
        st.dataframe(raw_data)
    else:
        st.write("Aucune donnée non nettoyée disponible.")

elif choice == "Formulaire d'évaluation":
    st.header("Formulaire d'évaluation")
    with st.form("eval_form"):
        nom = st.text_input("Nom")
        email = st.text_input("Email")
        commentaire = st.text_area("Commentaire")
        submitted = st.form_submit_button("Soumettre")
        if submitted:
            st.write(f"Merci {nom}, votre évaluation a été soumise!")
            # Vous pouvez ajouter du code ici pour enregistrer l'évaluation si nécessaire
