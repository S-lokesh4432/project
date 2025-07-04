import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests

# ✅ Configure Gemini API Key
genai.configure(api_key="AIzaSyCLNfAJ35lS6IuUvGAyRGYhr7iyUBCh-2A")

# ✅ Load Lottie animation
def load_lottie_url(url):
    res = requests.get(url)
    if res.status_code == 200:
        return res.json()
    return None

# ✅ Trophy animation
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_qp1q7mct.json"
lottie_animation = load_lottie_url(lottie_url)

# ✅ Streamlit UI setup
st.set_page_config(page_title="Motivation Generator", page_icon="✨")
st.title("🌟 Motivation Generator")
st.write("Get a personalized motivational message based on your need.")

# ✅ Center animation
if lottie_animation:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st_lottie(lottie_animation, height=250, key="motivate")
else:
    st.warning("⚠️ Couldn't load animation.")

# ✅ Input prompt
prompt = st.text_input("💬 What do you need motivation for?", placeholder="e.g., exams, failure, tired")

# ✅ Initialize session state
if "response" not in st.session_state:
    st.session_state.response = ""

# ✅ Function to call Gemini
def generate_motivation():
    try:
        model = genai.GenerativeModel("models/gemini-1.5-flash-latest")
        response = model.generate_content(f"Give a motivational quote for: {prompt}")
        st.session_state.response = response.text.strip()
    except Exception as e:
        st.error(f"❌ Error: {e}")

# ✅ Main button
if st.button("✨ Get Motivation"):
    if not prompt.strip():
        st.warning("Please enter something.")
    else:
        generate_motivation()

# ✅ Regenerate button
if st.session_state.response:
    if st.button("🔁 Regenerate"):
        generate_motivation()

# ✅ Display result
if st.session_state.response:
    st.success("💡 Here's your motivational message:")
    st.markdown(f"**{st.session_state.response}**")
