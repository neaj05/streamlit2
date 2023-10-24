import streamlit as st
import joblib
import numpy as np
from sklearn.linear_model import LogisticRegression

st.title("Prédiction de la probabilité d’attrition des clients.")
st.subheader("Application réalisé par N'DAH ARNAUD")
st.markdown("*Cette applicaion permet de prédire si des personnes sont les plus susceptibles d’avoir ou d’utiliser un compte bancaire.")

# Chargement du modèle

mon_model = joblib.load(filename="projet_streamlit2.joblib")

# Définition d'une fonction d'inférence

def predit_model(id_country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,code_relationship,code_marital_status,code_job_type):
    data_model = np.array([id_country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,code_relationship,code_marital_status,code_job_type])
    pred = mon_model.predict(data_model.reshape(1,-1))
    return pred

# L'utilisateur doit saisir une valeur pour chaque caractéritique


st.text("Les codes des pays{ 0:Kenya;1:Rwanda;2:Tanzania;3:Uganda}")
id_country = st.number_input(label="Code pays :",min_value=0,max_value=3, value=1)
year = st.number_input(label="Année :",min_value=1900,max_value=9999, value=2023)
st.text("Les codes des types location{ 0:Rural;1:Urban}")
location_type = st.number_input(label="Type location :",min_value=0,max_value=10, value=3)
st.text("Réponse pour accès au phone{ 0:No;1:Yes}")
cellphone_access = st.number_input(label="Accès au phone? :",min_value=0,max_value=1, value=1)
household_size = st.number_input(label="Taille du ménage :",min_value=0,max_value=999, value=5)
age_of_respondent = st.number_input(label="Age :",min_value=18,max_value=99, value=35)
st.text("Les codes du genre{ 1:Female;2:Male}")
gender_of_respondent = st.number_input(label="Genre :",min_value=1,max_value=2, value=2)
st.text("Les codes des liens{0:Child;1:Head of Household;2:Other non-relatives;3:Other relative;4:Parent;5:Spouse}")
code_relationship = st.number_input(label="Code de lien de parenté :",min_value=0,max_value=5, value=3)
st.text("Les codes statut matrimonial {0:Divorced/Seperated;1:Dont know;2:Married/Living together;3:Single/Never Married;4:Widowed}")
code_marital_status = st.number_input(label="Code statut matrimonial :",min_value=0,max_value=4, value=2)
st.text("Les codes des types job {0:Dont Know/Refuse to answer;1:Farming and Fishing;2:Formally employed Government;3:Formally employed Private;4:Government Dependent;}")
st.text("{5:Informally employed;6:No Income;7:Other Income;8:Remittance Dependent;9:Self employed}")
code_job_type = st.number_input(label="Code du type de job :",min_value=0,max_value=9, value=3)

# Création du bouton "Prédict" qui retourne la prédiction du modèle

if st.button("Prédict"):
    prediction = predit_model(id_country,year,location_type,cellphone_access,household_size,age_of_respondent,gender_of_respondent,code_relationship,code_marital_status,code_job_type)
    if prediction == 0:
        st.success("Cette personne n'est pas susceptible d’avoir ou d’utiliser un compte bancaire.")
    if prediction == 1:
        st.success("Cette personne est plus susceptible d’avoir ou d’utiliser un compte bancaire.")
