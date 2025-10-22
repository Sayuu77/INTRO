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

# ========== FRASES SEGÚN EMOCIÓN ==========
frases = {
    "Triste": [
        "Está bien sentirte así.\nIncluso las flores lloran antes de florecer 🌸",
        "No te abandones.\nTu corazón aún tiene luz 💜",
        "Un mal día no define tu historia 🌙"
    ],
    "Estresada": [
        "Respira.\nPaso a pasito, tú puedes ☁️",
        "No cargues el mundo sola.\nTe mereces calma ✨",
        "Relaja tus hombros.\nLa paz es tuya 💜"
    ],
    "Ansiosa": [
        "Estás a salvo.\nEl ahora es suficiente 🌷",
        "Un pensamiento no es una sentencia 💫",
        "Tu mente hace ruido,\npero tu alma sabe la verdad 💜"
    ],
    "Motivada": [
        "Hoy brillas con más fuerza ✨",
        "Tus sueños tienen prisa por verte triunfar 🌟",
        "Lo que siembras hoy será magia mañana 💜"
    ]
}

styles = {
    "Cute Pastel": lambda t: t + "\n\n(｡•ᴗ-)✧",
    "Poético Suave": lambda t: t.replace("\n", " ") + "\n\n— florece, alma bonita —",
    "Divertido y Dulce": lambda t: t + "\n\n🍭✨"
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
st.title("✨ Generador de Mensajitos Bonitos ✨")

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

    draw_centered_multiline(draw, mensaje, font, img.width, start_y=260, fill=(85,75,150))

    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)

    st.download_button(
        label="📥 Descargar mensaje en PNG",
        data=buffer,
        file_name="mensaje.png",
        mime="image/png"
    )

# ========== FOOTER ALEATORIO ==========
frases_footer = [
    "Aunque hoy duela, mañana floreces 🌷",
    "La calma también es un avance ☁️",
    "Mereces cosas bonitas, no lo dudes 💜"
]

st.write("---")
st.caption(random.choice(frases_footer))
