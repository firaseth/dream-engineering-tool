import streamlit as st
from google import genai

# --- 1. CONFIG & AI SETUP ---
st.set_page_config(page_title="Dream Architect Pro", page_icon="🧠", layout="wide")

# Securely load Gemini
try:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
except Exception:
    st.error("⚠️ API Key missing! Add it to your Streamlit Secrets or .streamlit/secrets.toml")

# --- 2. TRANSLATIONS ---
languages = {
    "English": {"title": "🌙 AI Dream Architect", "btn": "Ask AI to Engineer Prompt", "success": "AI Analysis Complete!"},
    "Arabic": {"title": "🌙 مهندس الأحلام الذكي", "btn": "اطلب من الذكاء الاصطناعي هندسة المطالبة", "success": "اكتمل تحليل الذكاء الاصطناعي!"},
    "Chinese": {"title": "🌙 AI 梦境建筑师", "btn": "让 AI 设计提示词", "success": "AI 分析完成！"}
    # ... you can add the others back here easily!
}

# --- 3. UI SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    lang_choice = st.selectbox("Language", list(languages.keys()))
    t = languages[lang_choice]
    st.info("Powered by Gemini 3 Flash")

# --- 4. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder="Describe your dream here...")
    
    col1, col2 = st.columns(2)
    with col1:
        target_model = st.selectbox("Target AI", ["Midjourney v8", "Sora 2", "Flux.1"])
    with col2:
        creativity = st.slider("AI Creativity Level", 0.0, 1.0, 0.7)

# --- 5. THE AI ENGINE ---
def call_gemini(dream, model_target):
    prompt_instruction = (
        f"You are a professional Prompt Engineer for {model_target}. "
        f"The user has this dream: '{dream}'. "
        "Expand this into a highly detailed, cinematic prompt. "
        "Include lighting, camera lens (e.g. 35mm), and textures. "
        "Return ONLY the final prompt text. No conversational filler."
    )
    
    response = client.models.generate_content(
        model="gemini-1.5-flash", # Or gemini-2.0-flash in 2026
        contents=prompt_instruction
    )
    return response.text

# --- 6. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("Gemini is architecting your dream..."):
            final_result = call_gemini(dream_input, target_model)
            st.success(t["success"])
            st.code(final_result)
            st.copy_to_clipboard(final_result)
            st.toast("Copied to clipboard! ✅")
    else:
        st.warning("Please enter a dream first.")
