import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="Dream Engineering 2026", page_icon="🌙", layout="centered")

st.title("🌙 Dream-to-Prompt Engineering Tool")
st.info("Professional tool for Midjourney v8, Sora 2, and Veo 3.1")

# --- INPUT SECTION ---
with st.container():
    dream_text = st.text_area("✍️ Describe your dream in detail:", 
                              placeholder="Example: A white wolf running through a city made of emerald glass...")
    
    col1, col2 = st.columns(2)
    with col1:
        target_model = st.selectbox("🎯 Target AI Model:", 
                                    ["Midjourney v8", "Flux 2 Pro", "Sora 2 (Video)", "Google Veo 3.1 (Video)"])
    with col2:
        style_preset = st.selectbox("🎨 Style Preset:", 
                                    ["Cinematic", "Cyberpunk", "Surrealism", "Hyper-Realistic", "Vintage Film"])

# --- THE ENGINEERING ENGINE ---
def engineer_prompt(text, model, style):
    # Base engineering logic for 2026 models
    if "Video" in model:
        return (f"Video Motion: 60fps, fluid physics. Subject: {text}. "
                f"Style: {style}, cinematic lighting, high temporal consistency, "
                f"8k resolution. Optimized for {model}.")
    else:
        return (f"{text}, {style} style, shot on 35mm lens, f/1.8, "
                f"volumetric lighting, ray-traced reflections, --ar 16:9 --v 8")

# --- ACTION BUTTON ---
if st.button("🚀 Generate Engineered Prompts"):
    if dream_text:
        result = engineer_prompt(dream_text, target_model, style_preset)
        
        st.divider()
        st.subheader("Final Engineered Prompt:")
        st.code(result, language="text")
        
        st.success("Prompt ready! Copy and paste this into your AI generator.")
        
        # Additional tips based on selection
        if "Midjourney" in target_model:
            st.caption("💡 Tip: Use '--stylize 250' for more artistic freedom.")
    else:
        st.warning("Please enter a dream description first!")