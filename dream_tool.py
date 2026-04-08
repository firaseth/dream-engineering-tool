import streamlit as st
from google import genai
from google.genai import types

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Dream Architect Pro", page_icon="🌙", layout="wide")

# --- 2. THE AI ENGINE SETUP ---
# We keep this as simple as possible to avoid handshake errors
try:
    if "GEMINI_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    else:
        st.error("⚠️ API Key missing! Check your Streamlit Secrets.")
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
    st.info("Using Stable Gemini Engine")

# --- 5. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    target_model = st.selectbox("Target AI", ["Midjourney", "DALL-E", "Sora", "Flux"])
    creativity = st.slider("Creativity", 0.0, 1.0, 0.7)

# --- 6. GEMINI LOGIC (Ultra-Stable Version) ---
def call_gemini(dream, model_target, temp):
    prompt_instruction = (
        f"Create a professional image prompt for {model_target} based on this dream: {dream}. "
        "Make it cinematic and detailed. Return only the prompt."
    )
    
    try:
        # Using the standard stable alias. 
        # Even in 2026, this name is kept as a 'pointer' for backward compatibility.
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt_instruction,
            config=types.GenerateContentConfig(temperature=temp)
        )
        return response.text
    except Exception as e:
        # Final fallback: Try the most basic model name possible
        try:
            response = client.models.generate_content(model="gemini-pro", contents=prompt_instruction)
            return response.text
        except:
            return f"Error: {e}"

# --- 7. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("Processing..."):
            result = call_gemini(dream_input, target_model, creativity)
            st.success(t["success"])
            st.code(result, language="text")
    else:
        st.warning("Please enter a dream!")
