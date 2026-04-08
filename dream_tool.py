import streamlit as st
from google import genai
from google.genai import types

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Dream Architect Pro", page_icon="🌙", layout="wide")

# --- 2. THE AI ENGINE SETUP ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        # We initialize the client with the 2026 standard library
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    else:
        st.error("⚠️ API Key missing! Add GEMINI_API_KEY to your Secrets.")
except Exception as e:
    st.error(f"⚠️ Connection Error: {e}")

# --- 3. GLOBAL TRANSLATIONS ---
languages = {
    "English": {"title": "🌙 AI Dream Architect", "btn": "Engineer Prompt", "success": "Done!", "place": "Describe your dream..."},
    "العربية": {"title": "🌙 مهندس الأحلام الذكي", "btn": "هندسة المطالبة", "success": "تم!", "place": "صف حلمك هنا..."},
    "中文": {"title": "🌙 AI 梦境建筑师", "btn": "生成提示词", "success": "完成！", "place": "描述你的梦境..."}
}

# --- 4. SIDEBAR ---
with st.sidebar:
    lang_choice = st.selectbox("Language", list(languages.keys()))
    t = languages[lang_choice]
    st.markdown("---")
    # In 2026, 'gemini-flash' is the universal stable ID
    st.info("Engine: Gemini 3 Flash (Stable)")

# --- 5. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    target_model = st.selectbox("Target AI", ["Midjourney v8", "Sora 3.1", "Flux.2 Pro", "DALL-E 4"])
    creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7)

# --- 6. GEMINI LOGIC (Using 2026 Stable ID) ---
def call_gemini(dream, model_target, temp):
    prompt_instruction = (
        f"You are a professional Prompt Engineer for {model_target}. "
        f"The user had this dream: '{dream}'. "
        "Expand this into a master-level cinematic image generation prompt. "
        "Return ONLY the final prompt text."
    )
    
    try:
        # 'gemini-flash' is the correct 2026 stable name for the v1 API
        response = client.models.generate_content(
            model="gemini-flash", 
            contents=prompt_instruction,
            config=types.GenerateContentConfig(
                temperature=temp
            )
        )
        return response.text
    except Exception as e:
        # If even that fails, we try the 'gemini-pro' alias
        try:
            response = client.models.generate_content(
                model="gemini-pro", 
                contents=prompt_instruction
            )
            return response.text
        except:
            return f"Architectural Error: {e}"

# --- 7. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("Analyzing Dream..."):
            final_result = call_gemini(dream_input, target_model, creativity)
            st.success(t["success"])
            st.code(final_result, language="text")
    else:
        st.warning("Please describe your dream first!")
