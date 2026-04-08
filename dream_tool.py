import streamlit as st

# --- 1. SETTINGS & TRANSLATIONS ---
st.set_page_config(page_title="Dream Engineer Pro", page_icon="🚀", layout="wide")

languages = {
    "English": {
        "title": "🌙 Dream-to-Prompt Engineering Tool",
        "desc": "✍️ Describe your dream:",
        "model": "🎯 Target Model",
        "style": "🎨 Artistic Style",
        "btn": "Generate Professional Prompt",
        "history": "Recent Generations",
        "copy": "Copy to Clipboard",
        "success": "Prompt generated successfully!"
    },
    "Arabic": {
        "title": "🌙 أداة هندسة الأحلام",
        "desc": "✍️ صف حلمك بالتفصيل:",
        "model": "🎯 النموذج المستهدف",
        "style": "🎨 النمط الفني",
        "btn": "توليد المطالبة الاحترافية",
        "history": "السجل الأخير",
        "copy": "نسخ إلى الحافظة",
        "success": "تم توليد المطالبة بنجاح!"
    }
}

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Settings")
    lang_choice = st.selectbox("Select Language / اختر اللغة", ["English", "Arabic"])
    t = languages[lang_choice]
    st.divider()
    st.info("Version 2.0 - High Fidelity Engineering")

# --- 3. MAIN INTERFACE ---
st.title(t["title"])
st.caption("Optimized for Midjourney v8, Sora 2, and Flux Pro")

# Use a container for a clean "card" look
with st.container(border=True):
    dream_text = st.text_area(t["desc"], height=150, placeholder="A giant neon jellyfish floating over a rainy Tokyo street...")
    
    col1, col2 = st.columns(2)
    with col1:
        target_model = st.selectbox(t["model"], ["Midjourney v8", "Sora 2 (Video)", "Flux.1 Pro", "Veo 3.1"])
    with col2:
        style_preset = st.selectbox(t["style"], [
            "Cinematic", "Cyberpunk", "Surrealism", "Hyper-Realistic", 
            "Studio Ghibli", "Vintage Film", "Oil Painting", "3D Render"
        ])

# --- 4. THE ENGINEERING ENGINE ---
def engineer_prompt(text, model, style):
    # Professional string building
    base = f"{text}, {style} style"
    tech_specs = "8k resolution, volumetric lighting, ray-traced reflections, shot on 35mm, f/1.8"
    
    if "Sora" in model or "Veo" in model:
        return f"Motion Video: {base}, {tech_specs}, high temporal consistency, 60fps --v 2.0"
    else:
        return f"{base}, {tech_specs}, ultra-detailed, photorealistic --ar 16:9 --v 8"

# --- 5. EXECUTION & OUTPUT ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_text:
        with st.spinner('Engineering your prompt...'):
            final_prompt = engineer_prompt(dream_text, target_model, style_preset)
            
            st.success(t["success"])
            
            # The Professional Output Box
            st.subheader("Engineered Result")
            st.code(final_prompt, language="text")
            
            # --- COPY TO CLIPBOARD FEATURE ---
            st.copy_to_clipboard(final_prompt)
            st.toast("Copied to clipboard!", icon="✅")
            
    else:
        st.warning("Please enter a dream description!")

# --- 6. FOOTER ---
st.divider()
st.center = st.caption("© 2026 Dream Engineering Tool | Powered by Streamlit")
