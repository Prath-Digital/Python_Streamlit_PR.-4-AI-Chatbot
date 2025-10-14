# 🤖 AI Chatbot with Streamlit  

An interactive **AI-powered chatbot** built with [Streamlit](https://streamlit.io/) and [Groq API](https://groq.com/).  
This app lets you chat with a powerful LLaMA model, save conversations, and view your entire chat history—all inside a clean, WhatsApp-style interface.  

---

## 📂 Project Structure  

```
├── .streamlit/
│   └── secrets.toml    # 🔑 API keys & secrets
├── app.py              # 🐍 Main Streamlit app
├── app.py              # 🔗 Main Streamlit app Url
├── requirements.txt    # 📦 Dependencies
└── readme.md           # 📘 Documentation
```

---

## ✨ Features  

- 💬 Real-time chatbot (LLaMA-3.3-70B via Groq API)  
- 💾 Save and view chat history  
- 🗂️ Sidebar with all saved conversations  
- 🎨 WhatsApp-like chat UI (green for user, grey for bot)  
- 🧹 Clear chat / start new chat anytime  

---

## 🚀 Installation & Setup  

### 1️⃣ Clone the repo  
```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### 2️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```

### 3️⃣ Configure secrets 🔑  
Create a file `.streamlit/secrets.toml` and add your Groq API key:  

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

*(You can also add other API keys later if needed.)*  

### 4️⃣ Run the app 🎉  
```bash
streamlit run app.py
```

Now open your browser at [http://localhost:8501](http://localhost:8501) 🚀  

---

## 📸 Screenshots  

### 🖥️ Chat Interface  
💬 WhatsApp-style design with user (green bubble) and bot (grey bubble).  

*(Add screenshot here if you want)*  

---

## ⚡ Tech Stack  

- 🐍 Python  
- 🎨 Streamlit (frontend & UI)  
- 🤖 Groq API (LLaMA 3.3 70B model)  
- 🗄️ Supabase (optional, for storage if you extend)  

---

## 🔮 Future Improvements  

- 📝 Export chat history as `.txt` or `.json`  
- ☁️ Connect with Supabase/Postgres for persistent storage  
- 🌐 Deploy on Streamlit Cloud / Hugging Face Spaces  

---

## 🤝 Contributing  

PRs are welcome! 🎉  
If you’d like to contribute, fork the repo and submit a pull request.  

---

## 🛡️ License  

MIT License © 2025