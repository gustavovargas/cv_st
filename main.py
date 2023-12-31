import streamlit as st
import requests

# Función para llamar a la función Lambda de AWS
def call_lambda_function(input_text):
    lambda_endpoint = "https://your-api-gateway-url"
    # response = requests.post(lambda_endpoint, json={"text": input_text})
    # response = response.json()
    response = {"text": "texto de respuesta"}
    return response

# Interfaz de usuario de Streamlit
st.title("CV Search App")

user_input = st.text_input("Search for:", "")

# Lógica para llamar a la función Lambda y mostrar resultados
if user_input:
    st.write("Results:")
    results = call_lambda_function(user_input)

    st.write(results["text"])
