from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask Backend Running"

@app.route("/cv", methods=["GET"])
def get_cv():
    data = {
        "name": "Aryan Vishala",
        "location": "Modinagar / Haridwar, India",
        "phone": "9690107160",
        "email": "aryanvishala@gmail.com",
        "linkedin": "https://www.linkedin.com/in/aryan-vishala",
        "education": [
            {
                "degree": "B.Tech CSE",
                "institute": "Gurukul Kangri Vishwavidyalaya",
                "year": "2024–2028"
            },
            {
                "degree": "Class XII (CBSE)",
                "institute": "Dayawati Modi Public School",
                "score": "93%"
            },
            {
                "degree": "Class X (CBSE)",
                "institute": "Summer Field Public School",
                "score": "94%"
            }
        ],
        "skills": {
            "programming": ["Python", "Java (Basic)", "HTML", "CSS", "JavaScript"],
            "frameworks": ["Flask", "Streamlit"],
            "data": ["NumPy", "Pandas", "Matplotlib", "Seaborn"],
            "ml": ["EDA", "Feature Engineering", "Learning Core ML"]
        },
        "achievements": [
            "JEE Mains – 94.6 Percentile",
            "Elite Certification – NPTEL Python"
        ],
        "leadership": "Head Prefect (Investiture Ceremony)",
        "activities": [
            "Debates",
            "Public Speeches",
            "Awarded multiple times"
        ]
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
