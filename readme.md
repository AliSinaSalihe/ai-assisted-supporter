# AI-Assisted Supporter

A simple Flask + OpenAI-based chatbot to help new RMIT students:
- Course enrolment guidance
- Program structure lookup
- FAQ & policy clarifications
- Study-support signposting

## Setup

1. `git clone <repo-url>`
2. `cd ai-assisted-supporter`
3. `python -m venv venv && source venv/bin/activate`
4. `pip install -r requirements.txt`
5. Copy your JSON files into `data/`:
   - `courses_data.json`
   - `cyber_security_program_structure.json`
6. Create a `.env` with:
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```
7. `flask run`

Visit http://127.0.0.1:5000 to chat!
