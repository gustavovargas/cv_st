import streamlit as st
import requests

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


# Interfaz de usuario de Streamlit
st.title("CV Search App")

user_input = st.text_input("Search for:", "")

# Lógica para llamar a la función Lambda y mostrar resultados
if user_input:
    st.write("Results:")
    results = call_lambda_function(user_input)
    print("\nResults:", results)
    st.write(results)
