import streamlit as st
from openai import OpenAI

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Dream Architect Global", page_icon="🌙", layout="wide")

# --- 2. OPENROUTER SETUP ---
try:
    if "OPENROUTER_API_KEY" in st.secrets:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["OPENROUTER_API_KEY"],
        )
    else:
        st.error("⚠️ API Key missing! Add OPENROUTER_API_KEY to your Secrets.")
except Exception as e:
    st.error(f"⚠️ Connection Error: {e}")

# --- 3. GLOBAL TRANSLATIONS ---
languages = {
    "English": {"title": "🌙 AI Dream Architect", "btn": "Engineer Prompt", "success": "Analysis Complete!", "place": "Describe your dream..."},
    "العربية": {"title": "🌙 مهندس الأحلام الذكي", "btn": "هندسة المطالبة", "success": "تم التحليل!", "place": "صف حلمك هنا..."},
    "中文": {"title": "🌙 AI 梦境建筑师", "btn": "生成提示词", "success": "分析完成！", "place": "描述你的梦境..."}
}

# --- 4. SIDEBAR ---
with st.sidebar:
    lang_choice = st.selectbox("Select Language", list(languages.keys()))
    t = languages[lang_choice]
    st.markdown("---")
    # You can change this to any free model like "google/gemini-2.0-flash-exp:free" 
    # or "mistralai/mistral-7b-instruct:free" or "thu-coai/glm-4-9b-chat"
    model_choice = st.selectbox("Select AI Model", [
        "google/gemini-2.0-flash-exp:free",
        "mistralai/mistral-7b-instruct:free",
        "openchat/openchat-7b:free",
        "thu-coai/glm-4-9b-chat"
    ])
    st.info(f"Model: {model_choice}")

# --- 5. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    
    col1, col2 = st.columns(2)
    with col1:
        target_model = st.selectbox("Target Image Generator", ["Midjourney v6", "DALL-E 3", "Flux.1", "Sora"])
    with col2:
        creativity = st.slider("Creativity", 0.0, 1.0, 0.7)

# --- 6. OPENROUTER LOGIC ---
def call_ai(dream, target_gen, model_name, temp):
    prompt_msg = (
        f"You are a professional Prompt Engineer for {target_gen}. "
        f"The user describes this dream: '{dream}'. "
        "Expand this into a highly detailed, cinematic, and artistic prompt for image generation. "
        "Return ONLY the final prompt text. No conversational filler."
    )
    
    try:
        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that creates image prompts."},
                {"role": "user", "content": prompt_msg}
            ],
            temperature=temp
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {e}"

# --- 7. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("AI is architecting your dream..."):
            final_result = call_ai(dream_input, target_model, model_choice, creativity)
            st.success(t["success"])
            st.code(final_result, language="text")
    else:
        st.warning("Please enter a dream description!")
