import streamlit as st
from gtts import gTTS
import tempfile
import os

# Simulación de usuario y contraseña
USUARIO = "edbenson"
CONTRASENA = "1234"

# Inicializar estado de sesión
if "logueado" not in st.session_state:
    st.session_state.logueado = False

if not st.session_state.logueado:
    st.title("🔐 AccesoLab - Iniciar Sesión")
    usuario = st.text_input("Usuario")
    contrasena = st.text_input("Contraseña", type="password")

    if st.button("Ingresar"):
        if usuario == USUARIO and contrasena == CONTRASENA:
            st.session_state.logueado = True
            st.success("Inicio de sesión exitoso ✅")
        else:
            st.error("Usuario o contraseña incorrectos")

else:
    # Página principal después de iniciar sesión
    st.set_page_config(page_title="AccesoLab", layout="wide")
    st.title("🧩 AccesoLab - Navegación y Lectura Accesible")

    menu = st.sidebar.radio("Funciones disponibles", [
        "Navegación con teclado ⌨️",
        "Lectura de texto 📖",
        "Comandos de voz 🎙️",
        "Cambio de fuente 🔡",
        "Feedback sonoro 🔔"
    ])

    if menu == "Navegación con teclado ⌨️":
        st.header("Navegación con teclado ⌨️")
        st.info("Puedes moverte con TAB y activar elementos con ENTER.")
        st.code("TAB = siguiente\nSHIFT + TAB = anterior\nENTER = activar botón")

    elif menu == "Lectura de texto 📖":
        st.header("Lectura de texto 📖")
        texto = st.text_area("Escribe el texto que quieres escuchar")
        if st.button("🔊 Leer texto"):
            if texto.strip():
                tts = gTTS(text=texto, lang='es')
                with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
                    tts.save(tmpfile.name)
                    audio_bytes = open(tmpfile.name, 'rb').read()
                st.audio(audio_bytes, format='audio/mp3')
                os.remove(tmpfile.name)
            else:
                st.warning("Por favor, escribe algo de texto para escuchar.")

    elif menu == "Comandos de voz 🎙️":
        st.header("Comandos de voz 🎙️")
        st.write("Función deshabilitada temporalmente para evitar errores.")
        st.warning("Reconocimiento de voz no disponible actualmente.")

    elif menu == "Cambio de fuente 🔡":
        st.header("Cambio de fuente 🔡")
        opcion = st.selectbox("Elige un tipo de fuente", ["Normal", "Grande", "Muy grande"])
        if opcion == "Grande":
            st.markdown('<style>body { font-size: 24px !important; }</style>', unsafe_allow_html=True)
        elif opcion == "Muy grande":
            st.markdown('<style>body { font-size: 30px !important; }</style>', unsafe_allow_html=True)
        st.success("Fuente aplicada (recarga si no ves cambios)")

    elif menu == "Feedback sonoro 🔔":
        st.header("Feedback sonoro 🔔")
        st.write("Esta función no está disponible en la versión web.")
        st.warning("Feedback sonoro deshabilitado temporalmente.")
