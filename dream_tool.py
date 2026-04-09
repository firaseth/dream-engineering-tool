import streamlit as st
from openai import OpenAI

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Dream Architect v5.1", page_icon="🌙", layout="wide")

# --- 2. OPENROUTER SETUP ---
try:
    if "OPENROUTER_API_KEY" in st.secrets:
        client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=st.secrets["OPENROUTER_API_KEY"],
        )
    else:
        st.error("⚠️ Add OPENROUTER_API_KEY to your Streamlit Secrets!")
except Exception as e:
    st.error(f"⚠️ Connection Error: {e}")

# --- 3. LANGUAGES & MODELS ---
languages = {
    "English": {"title": "🌙 AI Dream Architect", "btn": "Engineer Prompt", "success": "Done!", "place": "Describe your dream...", "ai_lang": "English"},
    "العربية": {"title": "🌙 مهندس الأحلام الذكي", "btn": "هندسة المطالبة", "success": "تم!", "place": "صف حلمك هنا...", "ai_lang": "Arabic"},
    "中文": {"title": "🌙 AI 梦境建筑师", "btn": "生成提示词", "success": "完成！", "place": "描述你的梦境...", "ai_lang": "Chinese"}
}

model_options = {
    "GLM-5-Air (Free)": "z-ai/glm-5-air:free",
    "Llama 3.3 70B (Free)": "meta-llama/llama-3.3-70b-instruct:free",
    "Qwen 3 Plus (Free)": "qwen/qwen3-plus:free"
}

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    lang_choice = st.selectbox("Language / اللغة", list(languages.keys()))
    t = languages[lang_choice]
    
    selected_name = st.selectbox("AI Engine", list(model_options.keys()))
    model_choice = model_options[selected_name]
    st.info(f"Using: {selected_name}")

# --- 5. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    col1, col2 = st.columns(2)
    with col1:
        target_gen = st.selectbox("Target AI", ["Midjourney v8", "Sora 3.1", "Flux.2", "DALL-E 4"])
    with col2:
        creativity = st.slider("Creativity", 0.0, 1.0, 0.7)

# --- 6. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("GLM-5 is imagining..."):
            try:
                # The prompt now explicitly asks for the specific language
                sys_msg = f"You are a prompt engineer. Respond ONLY in {t['ai_lang']}."
                
                completion = client.chat.completions.create(
                    model=model_choice,
                    messages=[
                        {"role": "system", "content": sys_msg},
                        {"role": "user", "content": f"Create a cinematic {target_gen} prompt for: {dream_input}"}
                    ],
                    temperature=creativity,
                    # FIX: Lowering max_tokens prevents the 402 Credit Error
                    max_tokens=1000, 
                    extra_headers={
                        "HTTP-Referer": "https://dream-architect.streamlit.app", 
                        "X-Title": "Dream Architect Pro"
                    }
                )
                st.success(t["success"])
                st.code(completion.choices[0].message.content, language="text")
            except Exception as e:
                st.error(f"Model Error: {e}")
    else:
        st.warning("Please enter a dream first!")
