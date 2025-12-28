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
    st.title("Aryan Vishala")
    st.write("Modinagar / Haridwar, India")
    st.write("📞 9690107160")
    st.write("📧 aryanvishala@gmail.com")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/aryan-vishala)")

st.markdown("---")

st.header("🎯 Professional Summary")
st.write(
    "Highly motivated Computer Science undergraduate with a strong academic background "
    "and hands-on experience in building real-world web applications. Proficient in Flask "
    "and Streamlit, with a growing interest in backend development, problem-solving, and "
    "core Machine Learning concepts. Known for leadership, communication skills, and "
    "consistent academic performance."
)

st.header("🎓 Education")

st.subheader("B.Tech in Computer Science & Engineering (2024–2028)")
st.write("Gurukul Kangri Vishwavidyalaya, Haridwar")
st.write("📊 CGPA: **9.4**")

st.subheader("Class XII – CBSE (2023)")
st.write("Dayawati Modi Public School, Modinagar")
st.write("📊 Score: **93%**")

st.subheader("Class X – CBSE (2021)")
st.write("Summer Field Public School, Modinagar")
st.write("📊 Score: **94%**")

st.header("💻 Technical Skills")
st.write("**Programming & Web:** Python, HTML, CSS, JavaScript")
st.write("**Frameworks & Tools:** Flask, Streamlit")
st.write("**Version Control:** Git, GitHub")
st.write("**Data & ML Foundations:** NumPy, Pandas, Matplotlib, Seaborn, EDA, Feature Engineering")
st.write("**Currently Learning:** Core Machine Learning concepts")

st.header("🧩 DSA Problem Solving")
st.write(
    "• Solved **51+ problems on LeetCode** – "
    "[Profile](https://leetcode.com/u/Aryan_Vishala/)"
)
st.write(
    "• Solved **99+ problems on GeeksforGeeks** – "
    "[Profile](https://www.geeksforgeeks.org/profile/aryanvi341r)"
)

st.header("🛠️ Projects")
st.write(
    "**CV Web Application (Flask + Streamlit)**  \n"
    "Built a full-stack CV web application using Flask as a REST API backend "
    "and Streamlit as a frontend UI. The project demonstrates clean separation "
    "of backend and frontend with dynamic rendering of resume data."
)
st.markdown(
    "🔗 GitHub Repository: "
    "[cv-web-app](https://github.com/Aryan-Vishala/cv-web-app.git)"
)


st.header("🧠 Leadership & Communication Skills")
st.write(
    "• Served as **Senior Prefect** in Class XII, demonstrating leadership, "
    "responsibility, and team coordination skills."
)
st.write(
    "• Strong communication and public speaking skills with multiple **1st and 2nd "
    "position awards** in debates and speech competitions."
)

st.markdown("---")
st.caption("Made by Aryan. :)")


