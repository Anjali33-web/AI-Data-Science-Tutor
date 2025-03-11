# 📚 Conversational AI Data Science Tutor

A **Conversational AI Chatbot** built with **Streamlit, LangChain, and Google Gemini **.  
This AI tutor answers **only Data Science-related doubts** while maintaining **conversation awareness with memory**.  

---

## 🚀 Features
✅ Uses **Google Gemini 1.5 Pro (Free API)**  
✅ **Conversation Memory** (Remembers past interactions)  
✅ **Built with LangChain & Streamlit** for a simple UI  
✅ **Free Deployment on Streamlit Cloud**  

---

## 🛠 Tech Stack
- **Frontend:** [Streamlit](https://streamlit.io/)  
- **AI Model:** [Google Gemini 1.5 Pro](https://aistudio.google.com/) (via LangChain)  
- **Memory:** [LangChain ConversationBufferMemory](https://python.langchain.com/)  
- **Deployment:** [Streamlit Cloud](https://streamlit.io/cloud)  

---

## 📂 Project Structure
📦 AI-Data-Science-Tutor ┣ 📜 .env # Stores Google API Key (DO NOT SHARE) ┣ 📜 config.py # Loads API key from .env ┣ 📜 app.py # Main Chatbot App (Streamlit) ┣ 📜 requirements.txt # Python Dependencies ┗ 📜 README.md # This File


---

## 🔧 Installation & Setup (Run Locally)
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/YOUR-USERNAME/AI-Data-Science-Tutor.git
cd AI-Data-Science-Tutor
2️⃣ Create a Virtual Environment (Recommended)

python -m venv venv
Activate it:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate
3️⃣ Install Dependencies

pip install -r requirements.txt
4️⃣ Get Google Gemini API Key
Go to Google AI Studio
Sign in → Get API Key
Copy the API key
Create a .env file in the project folder & add:

GOOGLE_API_KEY=your-api-key
5️⃣ Run the Chatbot

streamlit run app.py
🌍 Deploy on Streamlit Cloud (Free)
Push your code to GitHub
bash
git add .
git commit -m "Initial commit"
git push origin main
Go to Streamlit Cloud
Sign in with GitHub
Deploy App → Set app.py as the main file
Click "Deploy" 🎉

🤖 How It Works
Enter your Data Science-related question
The AI responds with an explanation
Conversation Memory maintains context
🛠 Troubleshooting
LangChain Community Module Not Found?
Run this:

bash
pip install --upgrade langchain langchain-community langchain-google-genai
Streamlit Not Found?
bash
pip install streamlit
🎯 Next Steps
Improve UI design
Add more AI capabilities
Deploy on Hugging Face Spaces
💡 Credits
Developed by: Your Name
Model: Google Gemini 
Frameworks: LangChain, Streamlit
⭐ Like This Project? Give It a Star on GitHub! ⭐


---

### **💡 What’s Included?**
✔️ Installation Steps  
✔️ API Key Setup  
✔️ Running Instructions  
✔️ Deployment Guide  
✔️ Troubleshooting Section  

💡 **Next Steps:**  
- Upload this **`README.md`** to GitHub  
- Create a **`requirements.txt`** by running:
  ```bash
  pip freeze > requirements.txt
