import streamlit as st

# --- CONFIG & TRANSLATION DICTIONARY ---
languages = {
    "English": {"title": "🌙 Dream-to-Prompt Tool", "input": "Describe your dream:", "btn": "Generate", "model": "Target Model:"},
    "Spanish": {"title": "🌙 Herramienta de Sueños", "input": "Describe tu sueño:", "btn": "Generar", "model": "Modelo:"},
    "Arabic": {"title": "🌙 أداة هندسة الأحلام", "input": "صف حلمك:", "btn": "توليد", "model": "النموذج:"},
    "French": {"title": "🌙 Outil d'Ingénierie des Rêves", "input": "Décrivez votre rêve:", "btn": "Générer", "model": "Modèle:"}
}

# --- SIDEBAR (Language Selection) ---
st.sidebar.title("Settings / الإعدادات")
lang = st.sidebar.selectbox("Choose Language:", list(languages.keys()))
t = languages[lang]

# --- MAIN UI ---
st.title(t["title"])

dream_text = st.text_area(t["input"])

col1, col2 = st.columns(2)
with col1:
    target_model = st.selectbox(t["model"], ["Midjourney v8", "Sora 2", "Veo 3.1", "Flux.1"])
with col2:
    # --- EXPANDED STYLE LIST ---
    style_preset = st.selectbox("Style / النمط:", [
        "Cinematic", "Cyberpunk", "Surrealism", "Hyper-Realistic", 
        "Vintage Film", "Studio Ghibli", "Oil Painting", "Noir"
    ])

# --- SMART ENGINE ---
def engineer_prompt(text, model, style):
    # Professional prompt structure
    return (f"{text}, {style} style, high-end production, "
            f"volumetric lighting, ray-tracing, 8k, --v 8")

if st.button(t["btn"]):
    if dream_text:
        result = engineer_prompt(dream_text, target_model, style_preset)
        st.divider()
        st.subheader("Engineered Prompt:")
        st.code(result)
    else:
        st.warning("Input required!")
