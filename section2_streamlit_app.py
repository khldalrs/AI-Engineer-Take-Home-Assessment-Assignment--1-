"""
Section 2: Streamlit Interface for GreenThumb Goods
This script creates a Streamlit interface using the open-source Phi-3-mini model.
"""

import streamlit as st
import json
import os
import requests

# Hugging Face API setup (optional: add your HF token if needed)
HF_MODEL_ID = "microsoft/phi-3-mini-4k-instruct"
HF_API_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL_ID}"
HF_HEADERS = {
    "Authorization": f"Bearer {os.getenv('HF_API_KEY', '')}"
} if os.getenv("HF_API_KEY") else {}

# ──────────────────────────────────────────────────────────────
# Set Streamlit page configuration
st.set_page_config(
    page_title="GreenThumb Goods AI Assistant",
    page_icon="🌱",
    layout="wide"
)

# Custom styling
st.markdown("""
<style>
    .main { background-color: #f5f7f2; }
    .stTextInput > div > div > input { background-color: white; }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 4px;
    }
    .chat-message { padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex; }
    .chat-message.user { background-color: #e6f7e6; }
    .chat-message.bot { background-color: #ffffff; border: 1px solid #e0e0e0; }
    .chat-message .avatar { width: 40px; height: 40px; border-radius: 50%; object-fit: cover; margin-right: 1rem; }
    .chat-message .message { flex: 1; }
</style>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# Load example data (optional fallback)
@st.cache_data
def load_example_data():
    try:
        path = os.path.join(os.path.dirname(__file__), "greenthumb_dataset.json")
        with open(path, "r") as f:
            return json.load(f)
    except:
        return [{"query": "What herbs grow well indoors?", "response": "Try basil, mint, and parsley. All thrive in indirect light!"}]

# System prompt for each mode
def create_prompt(user_query, mode):
    if mode == "Zero-shot":
        return (
            "You are a helpful assistant for GreenThumb Goods, a company that sells eco-friendly gardening supplies.\n\n"
            f"Customer: {user_query}\nAssistant:"
        )
    else:  # Few-shot
        examples = (
            "Customer: What plants are good for beginners?\n"
            "Assistant: Our Herb Garden Starter Kit and Indoor Succulent Collection are great for beginners.\n\n"
            "Customer: What's your return policy?\n"
            "Assistant: We offer a 30-day satisfaction guarantee on all items. Perishables must be returned within 7 days.\n\n"
        )
        return examples + f"Customer: {user_query}\nAssistant:"

# Query Hugging Face model endpoint
def get_phi3_response(prompt):
    payload = {"inputs": prompt, "parameters": {"max_new_tokens": 300, "temperature": 0.7}}
    try:
        res = requests.post(HF_API_URL, headers=HF_HEADERS, json=payload)
        res.raise_for_status()
        generated = res.json()
        return generated[0]["generated_text"].split("Assistant:")[-1].strip()
    except Exception as e:
        return f"Error from Hugging Face API: {str(e)}"

# Display chat-style messages
def display_chat_message(message, is_user=False):
    avatar = "👤" if is_user else "🌱"
    role_class = "user" if is_user else "bot"
    st.markdown(f"""
    <div class="chat-message {role_class}">
        <div class="avatar">{avatar}</div>
        <div class="message">{message}</div>
    </div>
    """, unsafe_allow_html=True)

# ──────────────────────────────────────────────────────────────
# Chat UI
st.title("🌱 GreenThumb Goods AI Assistant")
st.markdown("Ask anything about our gardening products, sustainability policies, or recommendations!")

# Sidebar prompt mode
st.sidebar.title("Model Settings")
prompt_mode = st.sidebar.radio("Select Prompt Strategy", ["Zero-shot", "Few-shot"])

# Sample prompts
with st.sidebar.expander("Example Queries"):
    st.markdown("""
    - What plants are good for small apartments?
    - What's your return policy for tools?
    - How do I compost kitchen waste at home?
    - Do your pots support hydroponics?
    """)

# Initialize chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display prior chat history
for msg in st.session_state.messages:
    display_chat_message(msg["content"], msg["role"] == "user")

# Input and submit
query = st.text_input("Ask a question:", key="query_input")
if st.button("Submit") and query:
    st.session_state.messages.append({"role": "user", "content": query})
    display_chat_message(query, is_user=True)

    with st.spinner("Thinking..."):
        prompt = create_prompt(query, prompt_mode)
        reply = get_phi3_response(prompt)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    display_chat_message(reply)

# Footer
st.markdown("---")
st.markdown("*Running on `microsoft/phi-3-mini-4k-instruct` via Hugging Face Inference API.*")
