import os
import json
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import openai

# --- Load environment ---
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# --- Load knowledge base ---
BASE_DIR = os.path.dirname(__file__)
with open(os.path.join(BASE_DIR, "data/courses_data.json")) as f:
    courses_kb = json.load(f)
with open(os.path.join(BASE_DIR, "data/cyber_security_program_structure.json")) as f:
    program_kb = json.load(f)

# --- Flask app ---
app = Flask(__name__)

# Prompt template
SYSTEM_PROMPT = '''
You are RMIT's "AI-Assisted Supporter" for new computing students.
Use the following data to answer fact-based queries:

1. Course catalogue: {courses}
2. Program structure: {program}

When responding, be concise, friendly, and include links or next steps if relevant.
'''

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")
    prompt = SYSTEM_PROMPT.format(
        courses=json.dumps(courses_kb, indent=2),
        program=json.dumps(program_kb, indent=2),
    ) + f"\n\nStudent: {user_msg}\nAssistant:"
    
    resp = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250,
        temperature=0.3,
        stop=["\nStudent:", "\nAssistant:"]
    )
    answer = resp.choices[0].text.strip()
    return jsonify({"reply": answer})

if __name__ == "__main__":
    app.run(debug=True)
