import streamlit as st
import requests
from PIL import Image

st.set_page_config(page_title="Aryan Vishala - CV", layout="wide")

API_URL = "http://127.0.0.1:5000/cv"

@st.cache_data(show_spinner=False)
def fetch_cv():
    response = requests.get(API_URL, timeout=5)
    response.raise_for_status()
    return response.json()

try:
    cv = fetch_cv()
except requests.exceptions.RequestException:
    st.error("❌ Flask backend is not running.\n\nStart backend/app.py first.")
    st.stop()

# ===== UI STARTS HERE =====

col1, col2 = st.columns([1, 3])

with col1:
    try:
        img = Image.open("profile.jpg")
        st.image(img, width=180)
    except:
        st.info("Add profile.jpg to frontend folder")

with col2:
    st.title(cv["name"])
    st.write(cv["location"])
    st.write(f"📞 {cv['phone']}")
    st.write(f"📧 {cv['email']}")
    st.markdown(f"[LinkedIn]({cv['linkedin']})")

st.markdown("---")

# Education
st.header("🎓 Education")
for edu in cv["education"]:
    st.subheader(edu["degree"])
    st.write(edu["institute"])
    if "year" in edu:
        st.write(f"📅 {edu['year']}")
    if "score" in edu:
        st.write(f"📊 Score: {edu['score']}")

# Skills
st.header("💻 Technical Skills")
st.write("**Programming:**", ", ".join(cv["skills"]["programming"]))
st.write("**Frameworks:**", ", ".join(cv["skills"]["frameworks"]))
st.write("**Data:**", ", ".join(cv["skills"]["data"]))
st.write("**ML:**", ", ".join(cv["skills"]["ml"]))

# Achievements
st.header("🏆 Achievements")
for a in cv["achievements"]:
    st.write(f"• {a}")

# Leadership
st.header("🧠 Leadership")
st.write(cv["leadership"])

# Activities
st.header("🎤 Extra-Curricular Activities")
for act in cv["activities"]:
    st.write(f"• {act}")

st.markdown("---")
st.caption("References available upon request")

