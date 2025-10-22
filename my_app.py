import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import random
import io
import os
import textwrap

# ---------------------------------------------------------
# 🌸 CONFIG PAGE
# ---------------------------------------------------------
st.set_page_config(
    page_title="Generador de Mensajes Bonitos",
    page_icon="🌸",
    layout="centered"
)

# ---------------------------------------------------------
# 🎨 STYLES
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
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 🌸 TITLE
# ---------------------------------------------------------
st.markdown("## 🌸 Generador de Mensajes Bonitos ✨")
st.write("Escribe cómo te sientes, elige el estilo y recibe un mensajito bonito para tu corazón 💜")

# ---------------------------------------------------------
# 🌸 SELECTORS
# ---------------------------------------------------------
emocion = st.selectbox("¿Cómo te sientes hoy? 💭",
                       ["Triste", "Estresada", "Ansiosa", "Motivada", "Cansada", "Con miedo"])

estilo = st.radio("Elige el estilo del mensaje 🌈",
                  ["Cute Pastel", "Poético Suave", "Divertido y Dulce"])

# ---------------------------------------------------------
# 🌸 MESSAGES & FOOTER
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
# Helper: cargar fuente con fallback
# ---------------------------------------------------------
def load_font(size):
    # Rutas candidatas (revisa /fonts/ si quieres subir una fuente personalizada)
    candidates = [
        "./fonts/Inter-Regular.ttf",
        "./fonts/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "C:/Windows/Fonts/arial.ttf",
        "arial.ttf"
    ]
    for path in candidates:
        try:
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
            # also try to load by name (some envs resolve it)
            ImageFont.truetype(path, size)
            return ImageFont.truetype(path, size)
        except Exception:
            continue
    # Fallback: font por defecto (no .ttf) — siempre funciona
    return ImageFont.load_default()

# ---------------------------------------------------------
# Helper: dibujar texto multiline centrado
# ---------------------------------------------------------
def draw_centered_multiline(draw, text, font, image_width, start_y, line_spacing=10, fill=(85,75,150)):
    # envolver texto para que no salga del ancho
    wrap_width = 28  # ajusta según tamaño de fuente y canvas
    lines = []
    for raw_line in text.split("\n"):
        wrapped = textwrap.wrap(raw_line, width=wrap_width) or [""]
        lines.extend(wrapped)
    # calcular alto total
    total_h = 0
    line_heights = []
    for line in lines:
        w, h = draw.textsize(line, font=font)
        line_heights.append((w, h))
        total_h += h + line_spacing
    total_h -= line_spacing  # quitar spacing extra del final

    y = start_y
    for i, line in enumerate(lines):
        w, h = line_heights[i]
        x = (image_width - w) // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += h + line_spacing

# ---------------------------------------------------------
# 🌸 GENERAR MENSAJE Y PNG
# ---------------------------------------------------------
if st.button("✨ Generar Mensajito ✨"):
    mensaje = mensajes[emocion][estilo]
    st.markdown(f"<div class='message-card'>{mensaje}</div>", unsafe_allow_html=True)

    # Crear imagen
    img_w, img_h = 900, 500
    img = Image.new("RGB", (img_w, img_h), color="#EAE7FF")
    draw = ImageDraw.Draw(img)

    # Soft Clouds (formas simples)
    cloud_color = (221, 225, 255)
    draw.ellipse((30, 50, 300, 190), fill=cloud_color)
    draw.ellipse((200, 80, 480, 230), fill=cloud_color)
    draw.ellipse((380, 40, 700, 180), fill=cloud_color)
    draw.ellipse((600, 90, 870, 240), fill=cloud_color)

    # Marco redondeado (simulado con rect y bordes)
    margin = 40
    draw.rounded_rectangle((margin, margin, img_w - margin, img_h - margin), radius=20, outline="#DDD6FF", width=3)

    # Cargar fuente con fallback
    font_size = 30
    font = load_font(font_size)

    # Dibujar texto centrado y envuelto
    draw_centered_multiline(draw, mensaje, font, img_w, start_y=260, line_spacing=8, fill=(85, 75, 150))

    # Opcional: pequeña firma/emoji
    try:
        small_font = load_font(18)
        draw.text((img_w - 180, img_h - 60), "🌸 Generador Cute", font=small_font, fill=(120, 100, 180))
    except Exception:
        pass

    # Guardar a buffer
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
