import streamlit as st
import requests
import os

@st.cache_data(show_spinner=False)
def get_css() -> str:
    # Read CSS code from style.css file
    with open(os.path.join(".", "style.css"), "r") as f:
        return f"<style>{f.read()}</style>"
    
# Función para llamar a la función Lambda de AWS
def call_lambda_function(input_text):
    lambda_endpoint = st.secrets["LAMBDA_URL"]
    list_words = input_text.split(",")
    list_words = [word.strip() for word in list_words]
    params = {
        "bucket": "data-kaigen-cv",
        "palabras_clave": list_words
    }
    
    response = requests.post(lambda_endpoint, json=params)
    print("\nResponse from Lambda function:", response)
    response = response.json()
    return response

st.set_page_config(
    page_title="SkillsMapper",
    page_icon="https://www.kairosds.com/favicon.png",
)

html = f"""
    <div style="padding: 0px;">
        <img src="https://www.kairosds.com/assets/images/logo-k.svg" alt="Logo" style="height: 20px;">
    </div>
    """

st.markdown(html, unsafe_allow_html=True)

# Interfaz de usuario de Streamlit
title_html = """
    <style>
        .title {
            padding-top: 5px;
        }
    </style>
    <h1 class="title">SkillsMapper</h1>
    """
st.markdown(title_html, unsafe_allow_html=True)

user_input = st.text_input("Search for:", "")

# Lógica para llamar a la función Lambda y mostrar resultados
if user_input:
    st.write("Results:")
    results = call_lambda_function(user_input)
    print("\nResults:", results)
    st.write(results)
