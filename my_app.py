import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io

# ---------------------------------------------------------
# 🌸 CONFIGURACIÓN DE LA PÁGINA
# ---------------------------------------------------------
st.set_page_config(
    page_title="Generador de Mensajes Bonitos",
    page_icon="🌸",
    layout="centered"
)

# ---------------------------------------------------------
# 🎨 ESTILOS AESTHETIC
# ---------------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #F3EDFF;
}
h1, h2, h3 {
    color: #6C63FF;
    text-align: center;
}
.stButton>button {
    background: linear-gradient(90deg, #A9C9FF, #FFBBEC);
    color: white;
    border-radius: 10px;
    height: 45px;
    border: none;
    font-size: 17px;
}
.message-card {
    background-color: #ffffffd9;
    border-radius: 15px;
    padding: 18px;
    border: 1px solid #E7DFFF;
    box-shadow: 0px 4px 10px #EAE4FF;
    text-align: center;
    font-size: 18px;
}
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 🌸 TÍTULO
# ---------------------------------------------------------
st.markdown("## 🌸 Generador de Mensajes Bonitos ✨")
st.write("Escribe cómo te sientes, elige el estilo y recibe un mensajito bonito para tu corazón 💜")

# ---------------------------------------------------------
# 🌸 SELECTORES
# ---------------------------------------------------------
emocion = st.selectbox("¿Cómo te sientes hoy? 💭", 
                       ["Triste", "Estresada", "Ansiosa", "Motivada", "Cansada", "Con miedo"])

estilo = st.radio("Elige el estilo del mensaje 🌈", 
                  ["Cute Pastel", "Poético Suave", "Divertido y Dulce"])

# ---------------------------------------------------------
# 🌸 MENSAJES BONITOS
# ---------------------------------------------------------
mensajes = {
    "Triste": {
        "Cute Pastel": "Aun con nubecitas en tu cielo, sigues brillando. 🌈💜",
        "Poético Suave": "Hay inviernos que enseñan a florecer. Resiste, que tu primavera llega. 🌸",
        "Divertido y Dulce": "Abrazo virtual, galleta y mantita para ti. Todo mejora, lo prometo 🫶🍪"
    },
    "Estresada": {
        "Cute Pastel": "Respira despacito. No tienes que con todo hoy. 🌿💜",
        "Poético Suave": "El caos también descansa. Permítete pausar y volver a ti. 🌙",
        "Divertido y Dulce": "Tú puedes. Y si no puedes, café. Y si no, siesta. ✨😴"
    },
    "Ansiosa": {
        "Cute Pastel": "Estás a salvo. Un pasito, un día, un respiro. 💕",
        "Poético Suave": "No corras con la mente. Abraza el ahora, que es suave contigo. 🌸",
        "Divertido y Dulce": "Detente: hidrátate, respira y piensa en perritos. Funcionará 🐶💗"
    },
    "Motivada": {
        "Cute Pastel": "¡Brillas! Sigue así, el mundo necesita tu luz. ✨💜",
        "Poético Suave": "Hoy floreces con decisión. Que nada te detenga. 🌼",
        "Divertido y Dulce": "Modo protagonista ACTIVADO. 🎬💪😎"
    },
    "Cansada": {
        "Cute Pastel": "Descansar también es avanzar. Permítelo. 🌙💤",
        "Poético Suave": "El cuerpo habla. Escúchalo, abrázalo, cuídalo. 🌾",
        "Divertido y Dulce": "Hoy: cobija, tecito, serie y paz. Receta infalible 🧸☕"
    },
    "Con miedo": {
        "Cute Pastel": "No estás sola. La valentía comienza con intentarlo. 💜🫶",
        "Poético Suave": "Incluso la noche teme al amanecer… y aun así amanece. 🌅",
        "Divertido y Dulce": "Miedo: apagado. Confianza: encendida. *click* 😌✨"
    }
}

footer_frases = [
    "Aunque hoy duela, mañana floreces 🌷",
    "Eres más fuerte de lo que piensas 💜",
    "Un paso pequeño también cuenta ✨",
    "Mereces cosas bonitas, no lo olvides 🌸",
    "Siempre hay luz en algún rincón del camino 🔮"
]

# ---------------------------------------------------------
# 🌸 BOTÓN PRINCIPAL
# ---------------------------------------------------------
if st.button("✨ Generar Mensajito ✨"):
    mensaje = mensajes[emocion][estilo]
    st.markdown(f"<div class='message-card'>{mensaje}</div>", unsafe_allow_html=True)

    # Generar PNG
    img = Image.new("RGB", (900, 500), color="#EAE7FF")
    draw = ImageDraw.Draw(img)

    # Nubes Soft Clouds
    cloud_color = (200, 210, 255)
    draw.ellipse((50, 60, 300, 200), fill=cloud_color)
    draw.ellipse((200, 90, 450, 240), fill=cloud_color)
    draw.ellipse((400, 50, 700, 200), fill=cloud_color)
    draw.ellipse((600, 90, 850, 240), fill=cloud_color)

    font = ImageFont.truetype("arial.ttf", 32)
    draw.text((100, 280), mensaje, font=font, fill=(85, 75, 150))

    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button("📥 Descargar mensaje como PNG", data=byte_im, file_name="mensaje.png", mime="image/png")

# ---------------------------------------------------------
# 🌸 FOOTER ALEATORIO
# ---------------------------------------------------------
st.markdown("---")
st.write(random.choice(footer_frases))
st.markdown("<br><br>", unsafe_allow_html=True)
