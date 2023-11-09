import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "courier_auth_token",
                    company_name = "Shims",
                    width = 200, height = 250,
                    logout_button_name = 'Logout', hide_menu_bool = False,
                    hide_footer_bool = False,
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN= __login__obj.build_login_ui()
username= __login__obj.get_username()

if LOGGED_IN == True:



  # Título de la aplicación
  st.title("LeybotGt")
  st.markdown("Esta aplicación responde preguntas relacionadas con la legislación de Guatemala.")
  st.text("Por Moris Polanco")
  
  # Campo de entrada para la pregunta o caso
  pregunta = st.text_area("Pregunta o caso")
  
  # Botón para obtener la respuesta
  if st.button("Obtener Respuesta"):
      if not pregunta:
          st.warning("Por favor, escriba una pregunta o caso.")
      else:
          # Realizar la solicitud a la API de Respell.ai
          response = requests.post(
              "https://api.respell.ai/v1/run",
              headers={
                  "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
                  "Accept": "application/json",
                  "Content-Type": "application/json"
              },
              data=json.dumps({
                  "spellId": "k0GhQkJOn7IKEY-BdghY6",
                  "inputs": {
                      "pregunta": pregunta
                  }
              })
          )
          
          # Procesar la respuesta de la API
          if response.status_code == 200:
              respuesta = response.json().get("outputs", {}).get("respuesta", "No se pudo obtener una respuesta")
              st.write("Respuesta:", respuesta)
          else:
              st.error("Error al enviar la solicitud a la API")
                                        
