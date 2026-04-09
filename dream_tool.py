import streamlit as st
from openai import OpenAI

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Dream Architect v5", page_icon="🌙", layout="wide")

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

# --- 3. UPDATED MODEL LIST (GLM-5 Edition) ---
model_options = {
    "GLM-5.1 (Latest/Fast)": "z-ai/glm-5.1",
    "GLM-5-Air (Efficient)": "z-ai/glm-5-air:free",
    "GLM-5-V Turbo (Visual)": "z-ai/glm-5v-turbo",
    "Llama 3.3 70B (Reliable)": "meta-llama/llama-3.3-70b-instruct:free"
}

# --- 4. UI ---
with st.sidebar:
    st.title("AI Settings")
    selected_name = st.selectbox("Choose Engine", list(model_options.keys()))
    model_choice = model_options[selected_name]
    st.info(f"Model ID: {model_choice}")

st.title("🌙 AI Dream Architect Pro")

with st.container(border=True):
    dream_input = st.text_area("✍️ Describe the dream...", height=150)
    col1, col2 = st.columns(2)
    with col1:
        target_gen = st.selectbox("Target AI", ["Midjourney v8", "Sora 3.1", "Flux.2", "DALL-E 4"])
    with col2:
        creativity = st.slider("Creativity", 0.0, 1.0, 0.7)

# --- 5. EXECUTION ---
if st.button("Engineer Prompt", type="primary", use_container_width=True):
    if dream_input:
        with st.spinner(f"GLM-5 is imagining..."):
            try:
                completion = client.chat.completions.create(
                    model=model_choice,
                    messages=[
                        {"role": "system", "content": "You are a master of visual prompt engineering."},
                        {"role": "user", "content": f"Create a cinematic {target_gen} prompt for: {dream_input}"}
                    ],
                    temperature=creativity,
                    extra_headers={
                        "HTTP-Referer": "https://dream-architect.streamlit.app", 
                        "X-Title": "Dream Architect Pro"
                    }
                )
                st.success("Analysis Complete!")
                st.code(completion.choices[0].message.content, language="text")
            except Exception as e:
                st.error(f"Model Error: {e}")
    else:
        st.warning("Please enter a dream first.")
