# BBC News NLP – Text Classification Project

## Objectif du projet
Ce projet a pour objectif de réaliser une **classification automatique d’articles de presse** issus du corpus **BBC News** à l’aide de différentes approches en **traitement automatique du langage naturel (NLP)**.  
Plusieurs familles de modèles ont été comparées afin d’évaluer leurs performances, leur complexité et leurs temps de calcul.

---

## Corpus
Le corpus utilisé est le jeu de données **BBC News**, composé d’articles textuels répartis en plusieurs catégories thématiques (politique, sport, économie, technologie, etc.).

---

## Structure du dépôt

```text
bbc-news-nlp/
│
├── notebooks/
│   ├── notebook_01_preprocessing.ipynb
│   ├── notebook_02_embeddings.ipynb
│   ├── notebook_03_word2vec_glove.ipynb
│   ├── notebook_04_sequential_models.ipynb
│   ├── notebook_05_transformers.ipynb
│   └── notebook_07_evaluation.ipynb
│
├── results/
│   └── results_transformers.csv
│
├── app/
│   └── app.py
│
└── README.md
