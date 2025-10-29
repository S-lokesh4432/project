import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests
from PIL import Image, ImageDraw, ImageFont
import io
import random
import os

# ✅ Use Gemini API Key from Streamlit secrets
genai.configure(api_key=st.secrets["AIzaSyCO6t310sIgf9ZWRZGJSdMAFCd_04CqnmQ"])

# ✅ Set full-page background image using CSS
def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ Load Lottie animation
def load_lottie_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return None

# ✅ Generate motivational quote using Gemini
def get_motivation(prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Generate a quote image with random background
def generate_quote_image(quote):
    # ✅ List of random scenic aesthetic backgrounds
    background_urls = [
        "https://images.unsplash.com/photo-1506784983877-45594efa4cbe",  # Planner
        "https://images.unsplash.com/photo-1496307653780-42ee777d4833",  # Forest
        "https://images.unsplash.com/photo-1505489304217-0c2f20504c0b",  # Ocean
        "https://images.unsplash.com/photo-1503676260728-1c00da094a0b",  # Desk
        "https://images.unsplash.com/photo-1501426026826-31c667bdf23d",  # Sunset
    ]
    selected_url = random.choice(background_urls)

    # ✅ Download and resize image
    response = requests.get(selected_url)
    background = Image.open(io.BytesIO(response.content)).convert("RGB")
    background = background.resize((800, 400))

    # ✅ Add white semi-transparent overlay for quote box
    overlay = Image.new('RGBA', background.size, (255, 255, 255, 0))
    overlay_draw = ImageDraw.Draw(overlay)
    overlay_draw.rectangle([(50, 100), (750, 300)], fill=(255, 255, 255, 200))
    background = Image.alpha_composite(background.convert("RGBA"), overlay)

    # ✅ Draw text
    draw = ImageDraw.Draw(background)
    try:
        font = ImageFont.truetype("arial.ttf", 28)
    except:
        font = ImageFont.load_default()

    # ✅ Wrap text
    lines = []
    words = quote.split()
    line = ""
    for word in words:
        if draw.textlength(line + word, font=font) < 700:
            line += word + " "
        else:
            lines.append(line.strip())
            line = word + " "
    lines.append(line.strip())

    # ✅ Center text vertically
    y = 140
    for line in lines:
        width = draw.textlength(line, font=font)
        draw.text(((800 - width) / 2, y), line, font=font, fill=(0, 0, 0))
        y += 40

    # ✅ Show and allow download
    buf = io.BytesIO()
    background.convert("RGB").save(buf, format="PNG")
    st.image(buf.getvalue(), caption="Your Motivational Quote", use_column_width=True)
    st.download_button("📥 Download as Image", data=buf.getvalue(), file_name="motivation.png", mime="image/png")

# ✅ Streamlit page setup
st.set_page_config(page_title="Motivation Generator", page_icon="✨")
set_background("https://images.unsplash.com/photo-1506784983877-45594efa4cbe")  # Page-wide BG

# ✅ Lottie Animation
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json"
lottie_animation = load_lottie_url(lottie_url)
if lottie_animation:
    st_lottie(lottie_animation, height=200, key="motivation")

# ✅ Title + Input
st.markdown("<h1 style='text-align: center;'>🌟 Daily Motivation Generator 🌟</h1>", unsafe_allow_html=True)
user_input = st.text_input("What do you need motivation for today?", placeholder="e.g., confidence, studies, career...")

# ✅ Generate Quote + Image
if st.button("Generate My Motivation"):
    with st.spinner("Generating inspiration..."):
        prompt = f"Give me a short, powerful motivational quote about {user_input}."
        quote = get_motivation(prompt)
        st.success("Here's your quote:")
        st.markdown(f"> *{quote}*")
        generate_quote_image(quote)







