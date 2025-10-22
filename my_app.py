import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

# ========== ESTILOS ==========
st.set_page_config(page_title="Mensajitos Bonitos ✨", page_icon="✨", layout="centered")

st.markdown("""
    <style>
    body { background: #F3ECFF; }
    .main { background-color: rgba(255,255,255,0.75); border-radius: 15px; padding: 20px; }
    h1, h2, h3, label { color: #6A5ACD; }
    </style>
""", unsafe_allow_html=True)

# ========== FRASES HUMANAS Y EMPÁTICAS ==========
frases = {
    "Triste": [
        "Está bien no estar bien. No te exijas sanar de golpe.",
        "No te sueltes. Incluso en días grises sigues siendo luz.",
        "Hoy duele, pero no será así para siempre.",
        "Tu corazón merece descanso, no presión.",
        "Un mal capítulo no borra toda tu historia."
    ],
    "Estresada": [
        "Respira. No tienes que resolverlo todo hoy.",
        "Haz una pausa. A veces el alma solo pide un respiro.",
        "No cargues con más de lo que tu pecho puede sostener.",
        "Paso a paso. Lo estás haciendo mejor de lo que crees.",
        "El mundo puede esperar. Tú también importas."
    ],
    "Ansiosa": [
        "Estás a salvo. Un pensamiento no define tu realidad.",
        "La mente exagera, el momento presente no.",
        "No estás sola en esto. Un respiro a la vez.",
        "Tu paz vale más que tu preocupación.",
        "No te castigues por sentir. Estás haciendo tu mejor intento."
    ],
    "Motivada": [
        "Sigue. Lo que sueñas también te está buscando.",
        "Hoy es un buen día para avanzar, aunque sea un poquito.",
        "Confía en lo que puedes llegar a ser.",
        "Brillas más cuando no dudas de ti.",
        "Tu esfuerzo construye futuros que aún no ves."
    ]
}

styles = {
    "Acompañamiento cálido": lambda t: t + "\n\nCon cariño, sigue adelante 🤍",
    "Directo": lambda t: t,
    "Suave y esperanzador": lambda t: t + "\n\nMereces calma. Mereces luz."
}

# ========== FUNCIÓN DE TEXTO CENTRADO ==========
def draw_centered_multiline(draw, text, font, img_width, start_y, line_spacing=10, fill=(0,0,0)):
    lines = text.split("\n")
    y = start_y
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=font)
        w = bbox[2] - bbox[0]
        h = bbox[3] - bbox[1]
        x = (img_width - w) // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += h + line_spacing

# ========== UI ==========
st.title("✨Generador de Mensajes✨")

emocion = st.selectbox("¿Cómo te sientes hoy?", list(frases.keys()))
estilo = st.selectbox("Elige el estilo del mensaje", list(styles.keys()))

if st.button("✨ Generar Mensajito ✨"):
    base = random.choice(frases[emocion])
    mensaje = styles[estilo](base)

    st.success(mensaje)

    # Generar PNG
    bg = Image.open("clouds.png").convert("RGBA")
    img = bg.copy()
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    draw_centered_multiline(draw, mensaje, font, img.width, start_y=260, fill=(70,60,120))

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.download_button(
        label="📥 Descargar mensaje en PNG",
        data=buffer,
        file_name="mensaje.png",
        mime="image/png"
    )
