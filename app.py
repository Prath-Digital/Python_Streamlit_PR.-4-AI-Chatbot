import streamlit as st
from groq import Groq
import datetime

# -------------------- App Setup --------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")
st.markdown("<h1 style='text-align:center'>AI Chatbot 🤖</h1>", unsafe_allow_html=True)

# -------------------- API Key Input --------------------
with st.sidebar:
    st.header("🔑 API Key Setup")
    api_key = st.text_input("Enter your Groq API Key", type="password", key="user_api_key")
    with st.expander("How to get API Key?"):
        st.markdown("""
        **Steps to get your Groq API Key:**
        1. Go to [Groq Console](https://console.groq.com/).
        2. Sign up or log in to your Groq account.
        3. Navigate to the 'API Keys' section in the dashboard.
        4. Click 'Create API Key'.
        5. Copy the generated API key and paste it here.
        6. Keep your API key secure and do not share it publicly.
        """)

# -------------------- API Setup --------------------
if api_key:
    client = Groq(api_key=api_key)
else:
    st.warning("Please enter your Groq API Key in the sidebar to use the chatbot.")
    st.stop()

model_name = "llama-3.3-70b-versatile"

# -------------------- Session State --------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "all_conversations" not in st.session_state:
    st.session_state.all_conversations = []  # List of dicts with "timestamp" and "messages"

# -------------------- Sidebar Features --------------------
with st.sidebar:
    st.header("💡 Features")
    if st.button("New Chat"):
        st.session_state.chat_history = []
    if st.button("Save Current Chat"):
        if st.session_state.chat_history:
            st.session_state.all_conversations.append({
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "messages": st.session_state.chat_history.copy()
            })
            st.success("Conversation saved!")
    st.subheader("All Saved Conversations")
    for i, conv in enumerate(st.session_state.all_conversations[::-1]):
        if st.expander(f"{conv['timestamp']}"):
            for msg in conv['messages']:
                if msg["role"] == "user":
                    st.markdown(f"**You:** {msg['content']}")
                else:
                    st.markdown(f"**Bot:** {msg['content']}")

# -------------------- Chat Display --------------------
chat_container = st.container()
with chat_container:
    # Ensure chat history is not empty before displaying
    if st.session_state.chat_history:
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.markdown(
                    f"""
                    <div style="
                        background-color:#DCF8C6;
                        color:#111111;
                        padding:10px 15px;
                        border-radius:15px;
                        text-align:right;
                        margin:5px 0;
                        max-width:70%;
                        float:right;
                        clear:both;">
                        <strong>You:</strong> {message['content']}
                    </div>
                    """, unsafe_allow_html=True
                )
            elif message["role"] == "assistant":
                st.markdown(
                    f"""
                    <div style="
                        background-color:#F1F0F0;
                        color:#111111;
                        padding:10px 15px;
                        border-radius:15px;
                        text-align:left;
                        margin:5px 0;
                        max-width:70%;
                        float:left;
                        clear:both;">
                        <strong>Bot:</strong> {message['content']}
                    </div>
                    """, unsafe_allow_html=True
                )
    else:
        st.info("No conversation yet. Start by sending a message!")

# -------------------- Input at Bottom (Auto-send on Enter) --------------------
prompt = st.text_input("Type your message...", key="chat_input")

if prompt and prompt.strip() != "" and st.session_state.get("last_prompt", "") != prompt:
    # Add user message
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    st.session_state.last_prompt = prompt  # Track last sent prompt

    try:
        # Send full chat history for context
        response = client.chat.completions.create(
            model=model_name,
            messages=st.session_state.chat_history
        )
        reply = response.choices[0].message.content

        # Add bot response
        st.session_state.chat_history.append({"role": "assistant", "content": reply})
    except Exception as e:
        st.error(f"Error: {e}")

    # Rerun to clear input (do NOT set st.session_state.chat_input directly)
    st.rerun()

# -------------------- Clear Chat Button --------------------
if st.button("Clear Chat"):
    st.session_state.chat_history = []
