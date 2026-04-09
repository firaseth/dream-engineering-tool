import streamlit as st
from openai import OpenAI

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Dream Prompt", page_icon="🌙", layout="wide")

# --- 2. OPENROUTER SETUP ---
try:
    if "OPENROUTER_API_KEY" in st.secrets:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["OPENROUTER_API_KEY"],
        )
    else:
        st.error("⚠️ OPENROUTER_API_KEY missing in Secrets!")
except Exception as e:
    st.error(f"⚠️ Connection Error: {e}")

# --- 3. LANGUAGES ---
languages = {
    "English": {"title": "🌙 AI Dream Prompt", "btn": "Engineer Prompt", "success": "Done!", "place": "Describe your dream...", "ai_lang": "English"},
    "العربية": {"title": "🌙 مهندس ملقن الأحلام", "btn": "هندسة المطالبة", "success": "تم!", "place": "صف حلمك هنا...", "ai_lang": "Arabic"},
    "中文": {"title": "🌙 AI 梦境提示词", "btn": "生成提示词", "success": "完成！", "place": "描述你的梦境...", "ai_lang": "Chinese"}
}

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    lang_choice = st.selectbox("Language / اللغة", list(languages.keys()))
    t = languages[lang_choice]
    st.info("System: Automatic Free Model Selection")

# --- 5. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    col1, col2 = st.columns(2)
    with col1:
        target_gen = st.selectbox("Target AI", ["Midjourney", "Sora", "Flux", "DALL-E"])
    with col2:
        creativity = st.slider("Creativity", 0.0, 1.0, 0.7)

# --- 6. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("Analyzing..."):
            try:
                completion = client.chat.completions.create(
                    model="openrouter/free",
                    messages=[
                        {"role": "system", "content": f"You are a professional prompt engineer. Respond only in {t['ai_lang']}."},
                        {"role": "user", "content": f"Create a detailed cinematic {target_gen} prompt for: {dream_input}"}
                    ],
                    temperature=creativity,
                    max_tokens=800, 
                    extra_headers={
                        "HTTP-Referer": "https://github.com/firaseth/dream-engineering-tool", 
                        "X-Title": "AI Dream Prompt"
                    }
                )
                st.success(t["success"])
                st.code(completion.choices[0].message.content, language="text")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a dream first!")
