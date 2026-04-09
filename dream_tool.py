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

# --- 3. SESSION STATE (HISTORY) ---
if "history" not in st.session_state:
    st.session_state.history = []

# --- 4. LANGUAGES & ASPEC RATIOS ---
languages = {
    "English": {"title": "🌙 AI Dream Prompt", "btn": "Engineer Prompt", "success": "Done!", "place": "Describe your dream...", "ai_lang": "English", "hist": "Prompt History"},
    "العربية": {"title": "🌙 مهندس ملقن الأحلام", "btn": "هندسة المطالبة", "success": "تم!", "place": "صف حلمك هنا...", "ai_lang": "Arabic", "hist": "سجل المطالبات"},
    "中文": {"title": "🌙 AI 梦境提示词", "btn": "生成提示词", "success": "完成！", "place": "描述你的梦境...", "ai_lang": "Chinese", "hist": "提示词历史"}
}

aspect_ratios = {
    "Cinema (16:9)": "--ar 16:9",
    "TikTok/Reels (9:16)": "--ar 9:16",
    "Square (1:1)": "--ar 1:1",
    "Photography (3:2)": "--ar 3:2"
}

# --- 5. SIDEBAR ---
with st.sidebar:
    st.title("Settings")
    lang_choice = st.selectbox("Language / اللغة", list(languages.keys()))
    t = languages[lang_choice]
    
    st.markdown("---")
    st.subheader("Frame Configuration")
    ar_choice = st.selectbox("Aspect Ratio", list(aspect_ratios.keys()))
    ar_suffix = aspect_ratios[ar_choice]
    
    if st.button("Clear History"):
        st.session_state.history = []
        st.rerun()

# --- 6. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    col1, col2 = st.columns(2)
    with col1:
        target_gen = st.selectbox("Target AI", ["Midjourney", "Sora", "Flux", "DALL-E"])
    with col2:
        creativity = st.slider("Creativity", 0.0, 1.0, 0.7)

# --- 7. EXECUTION ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_input:
        with st.spinner("Analyzing..."):
            try:
                # Engineering the prompt with the Aspect Ratio Improvement
                completion = client.chat.completions.create(
                    model="openrouter/free",
                    messages=[
                        {"role": "system", "content": f"You are a professional prompt engineer. Respond only in {t['ai_lang']}."},
                        {"role": "user", "content": f"Create a detailed cinematic {target_gen} prompt for: {dream_input}. Important: Append '{ar_suffix}' to the end of the prompt."}
                    ],
                    temperature=creativity,
                    max_tokens=800,
                    extra_headers={
                        "HTTP-Referer": "https://github.com/firaseth/dream-engineering-tool",
                        "X-Title": "AI Dream Prompt"
                    }
                )
                
                result = completion.choices[0].message.content
                st.session_state.history.insert(0, result) # Add to Gallery
                st.success(t["success"])
                st.code(result, language="text") # Standard copy button included here
                
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a dream first!")

# --- 8. PROMPT GALLERY ---
if st.session_state.history:
    st.markdown("---")
    st.subheader(f"🖼️ {t['hist']}")
    for i, old_prompt in enumerate(st.session_state.history):
        with st.expander(f"Prompt {len(st.session_state.history) - i}"):
            st.text(old_prompt)
            if st.button(f"Select Prompt {i}", key=f"btn_{i}"):
                st.info("Copy the text above using the code block in the main view!")
