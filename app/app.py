import streamlit as st
import pandas as pd

st.set_page_config(page_title="BBC News NLP", layout="wide")

st.title("BBC News – Classification NLP")
st.write("Application de démonstration des résultats du projet NLP.")

# Charger les résultats
@st.cache_data
def load_results():
    return pd.read_csv("../results/results_transformers.csv")

results_df = load_results()

st.subheader("Évaluation comparative des modèles")
st.dataframe(results_df)

st.subheader("Conclusion")
st.write("""
BERT obtient les meilleures performances globales sur le corpus BBC News.
DistilBERT est plus léger mais moins performant dans cette configuration.
""")

