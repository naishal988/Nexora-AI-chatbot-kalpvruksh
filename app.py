from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables from .env file securely
load_dotenv()

app = Flask(__name__)
CORS(app) 

# Initialize Groq Client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# UPGRADE: Emojis and strict Quiz parameters added to System Prompt
SYSTEM_PROMPT = """
You are 'EduNova', an elite, highly interactive AI Learning Tutor aligned with UN SDG 4 (Quality Education).
Your goal is not just to give answers, but to actively teach and test the user's understanding.

CORE RULES:
1. THE SOCRATIC METHOD: Never just hand over the final answer immediately. Guide the user to discover it.
2. ANALOGIES: Explain complex technical or scientific concepts using simple, everyday analogies.
3. MICRO-QUIZ: ALWAYS end your response with a quick, engaging 1-question quiz to test if they understood your explanation.
4. TONE & EMOJIS: Be encouraging, brilliant, and slightly witty. ALWAYS use relevant emojis (like 🎓, 💡, 🚀, 🧠, 📊) naturally in your responses to make learning fun!
5. FORMATTING: Use bullet points and **bold text** for readability. Keep responses concise (under 150 words).
6. SAFETY: Do not provide harmful advice or medical diagnoses.
7. QUIZ MODE: If the user specifically asks for a "Quiz", provide a 3-question multiple choice test based on the conversation history.
"""

@app.route('/', methods=['GET'])
def home():
    return "EduNova API is running perfectly! Waiting for queries at /chat endpoint."    

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    
    # Strictly adhere to Arena Evaluator rule: Must accept {"message": "..."}
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid request. Expected JSON with 'message' key."}), 400
    
    user_message = data['message']
    
    # UPGRADE: Optional memory/history feature. 
    # If the UI sends it, we use it. If the Arena Evaluator doesn't send it, it defaults to empty list [].
    history = data.get('history', []) 

    try:
        # Build the message array dynamically with memory
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        
        # Inject memory so AI remembers context
        for msg in history:
            if isinstance(msg, dict) and 'role' in msg and 'content' in msg:
                messages.append({"role": msg['role'], "content": msg['content']})
                
        # Inject current prompt
        messages.append({"role": "user", "content": user_message})

        # Send to Groq API
        chat_completion = client.chat.completions.create(
            messages=messages,
            model="openai/gpt-oss-120b", # Keeping your specific model
            temperature=0.7,
            max_tokens=500,
        )
        
        # Extract Response
        bot_reply = chat_completion.choices[0].message.content
        
        # Return exact JSON format required by Arena Evaluator: {"response":"..."}
        return jsonify({
            "response": bot_reply
        })

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"response": "I encountered a technical glitch while processing that. Let's try again!"}), 500

if __name__ == '__main__':
    # Render requires binding to 0.0.0.0 and dynamically assigning the PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
