# ✨ Nexora - Next Gen Learning Tutor

![SDG](https://img.shields.io/badge/UN_SDG-Goal_4_Quality_Education-blue?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Frontend-Tailwind_CSS_|_Vanilla_JS-34C759?style=for-the-badge)
![Tech Stack](https://img.shields.io/badge/Backend-Python_|_Flask_|_Groq-007AFF?style=for-the-badge)

Nexora is an elite, highly interactive AI Learning Tutor built to address **UN SDG 4 (Quality Education)**. Unlike standard LLM chatbots that simply hand over answers, this AI acts as a genuine mentor. It utilizes the Socratic method, breaks down complex concepts using real-world analogies, and actively tests the user's understanding through micro-quizzes.

## 🚀 Key Features

*   **The Socratic Method Engine:** The AI is strictly prompt-engineered to guide students to answers rather than doing their homework for them.
*   **Automated Micro-Quizzes:** Generates context-aware MCQ quizzes at the end of explanations to solidify learning retention.
*   **Multi-Thread Memory System:** Uses `localStorage` to save and manage multiple chat histories natively in the browser without requiring a heavy database.
*   **Premium Liquid Glass UI:** A flawless, modern aesthetic featuring 3D tilt effects, magnetic buttons, dynamic ambient parallax blobs, and smooth Apple-style modal popups.
*   **Robust Security:** Decoupled architecture. The Groq API key is locked deep within server environment variables, ensuring zero exposure to the client side.

## 🔗 Live Deployment

The platform is fully deployed, secure, and accessible online:

*   **Live Web Application:** https://nexora.naishalpnadiya988.workers.dev/
*   **Backend API Endpoint:** `https://nexora-backend-8ssg.onrender.com/chat`

*(The frontend securely fetches from the live Render API endpoint automatically. No local server setup or configuration is required to use the platform).*

## 🛠️ Architecture & Tech Stack

This project operates on a completely decoupled architecture for maximum speed and security.

*   **Frontend (UI/UX):** Custom HTML, Vanilla JavaScript, and Tailwind CSS. Hosted globally on **Cloudflare Pages**.
*   **Backend (API):** Python, Flask, and Flask-CORS. Hosted as a Web Service on **Render**.
*   **LLM Brain:** Groq API utilizing the `openai/gpt-oss-120b` model for hyper-fast, intelligent inferences.

## 👨‍💻 Developer / Architect

Developed and Architected entirely from scratch by:
*   **Naishal Nadiya** 
*   B.Tech Cybersecurity | Silver Oak University
*   🌐 Connect & Read my technical write-ups: **naishal988** across major blogging platforms.

*Part of the Nexus Ecosystem. Built with passion during the Next Gen Chatbot Arena Hackathon.*
