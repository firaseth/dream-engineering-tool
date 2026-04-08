import streamlit as st

# 1. Page Config
st.set_page_config(page_title="Dream Engineering 2026", page_icon="🌙")

st.title("🌙 Dream-to-Prompt Engineering Tool")

# 2. Input Section
dream_text = st.text_area("✍️ Describe your dream:")
col1, col2 = st.columns(2)
with col1:
    target_model = st.selectbox("🎯 Model:", ["Midjourney v8", "Sora 2", "Veo 3.1"])
with col2:
    style_preset = st.selectbox("🎨 Style:", ["Cinematic", "Cyberpunk", "Surrealism"])

# 3. The "Smart" Function (This is the part we improved)
def engineer_prompt(text, model, style):
    # This prevents double-typing if your dream already has pro terms
    if "--v" in text or "8k" in text:
        return f"{text} | Refined with {style} for {model}"
    
    # Standard engineering for simple dreams
    return (f"{text}, {style} style, shot on 35mm lens, f/1.8, "
            f"volumetric lighting, ray-traced reflections, --ar 16:9 --v 8")

# 4. Action Button
if st.button("🚀 Generate Engineered Prompt"):
    if dream_text:
        result = engineer_prompt(dream_text, target_model, style_preset)
        st.divider()
        st.subheader("Final Result:")
        st.code(result)
    else:
        st.warning("Please enter your dream first!")
