import streamlit as st

# --- 1. SETTINGS & TRANSLATIONS ---
st.set_page_config(page_title="Dream Engineer Pro", page_icon="🚀", layout="wide")

# Dictionary of all UI text including Chinese (Simplified)
languages = {
    "English": {
        "title": "🌙 Dream-to-Prompt Engineering Tool",
        "desc": "✍️ Describe your dream:",
        "model": "🎯 Target Model",
        "style": "🎨 Artistic Style",
        "btn": "Generate Professional Prompt",
        "copy": "Copied to clipboard!",
        "success": "Prompt generated successfully!",
        "input_req": "Please enter a dream description!"
    },
    "Arabic": {
        "title": "🌙 أداة هندسة الأحلام",
        "desc": "✍️ صف حلمك بالتفصيل:",
        "model": "🎯 النموذج المستهدف",
        "style": "🎨 النمط الفني",
        "btn": "توليد المطالبة الاحترافية",
        "copy": "تم النسخ!",
        "success": "تم توليد المطالبة بنجاح!",
        "input_req": "الرجاء إدخال وصف للحلم!"
    },
    "Chinese": {
        "title": "🌙 梦境提示词工程工具",
        "desc": "✍️ 描述你的梦境：",
        "model": "🎯 目标模型",
        "style": "🎨 艺术风格",
        "btn": "生成专业提示词",
        "copy": "已复制到剪贴板！",
        "success": "提示词生成成功！",
        "input_req": "请输入梦境描述！"
    },
    "Spanish": {
        "title": "🌙 Ingeniería de Prompts de Sueños",
        "desc": "✍️ Describe tu sueño:",
        "model": "🎯 Modelo Objetivo",
        "style": "🎨 Estilo Artístico",
        "btn": "Generar Prompt Profesional",
        "copy": "¡Copiado al portapapeles!",
        "success": "¡Prompt generado con éxito!",
        "input_req": "¡Por favor ingrese una descripción!"
    },
    "French": {
        "title": "🌙 Ingénierie de Prompts de Rêves",
        "desc": "✍️ Décrivez votre rêve:",
        "model": "🎯 Modèle Cible",
        "style": "🎨 Style Artistique",
        "btn": "Générer le Prompt Professionnel",
        "copy": "Copié dans le presse-papiers!",
        "success": "Prompt généré avec succès!",
        "input_req": "Veuillez entrer une description!"
    },
    "German": {
        "title": "🌙 Traum-zu-Prompt Engineering",
        "desc": "✍️ Beschreibe deinen Traum:",
        "model": "🎯 Ziel-Modell",
        "style": "🎨 Künstlerischer Stil",
        "btn": "Professionellen Prompt generieren",
        "copy": "In Zwischenablage kopiert!",
        "success": "Prompt erfolgreich generiert!",
        "input_req": "Bitte geben Sie eine Beschreibung ein!"
    },
    "Japanese": {
        "title": "🌙 ドリーム・プロンプト・エンジニアリング",
        "desc": "✍️ 夢の内容を入力してください:",
        "model": "🎯 ターゲットモデル",
        "style": "🎨 アートスタイル",
        "btn": "プロンプトを生成する",
        "copy": "クリップボードにコピーしました！",
        "success": "プロンプトの生成に成功しました！",
        "input_req": "夢の説明を入力してください！"
    }
}

# --- 2. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("Settings")
    lang_choice = st.selectbox("Select Language", list(languages.keys()))
    t = languages[lang_choice]
    st.divider()
    st.markdown(f"**Current Language:** {lang_choice}")
    st.info("Version 2.5 - Global Release")

# --- 3. MAIN INTERFACE ---
st.title(t["title"])
st.caption("Optimized for Midjourney v8, Sora 2, and Flux Pro")

with st.container(border=True):
    dream_text = st.text_area(t["desc"], height=120)
    
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
    # Professional string building for 2026 AI models
    base = f"{text}, {style} style"
    tech_specs = "8k resolution, volumetric lighting, ray-traced reflections, shot on 35mm, f/1.8"
    
    if "Sora" in model or "Veo" in model:
        return f"Motion Video: {base}, {tech_specs}, high temporal consistency, 60fps --v 2.0"
    else:
        return f"{base}, {tech_specs}, ultra-detailed, photorealistic --ar 16:9 --v 8"

# --- 5. EXECUTION & OUTPUT ---
if st.button(t["btn"], type="primary", use_container_width=True):
    if dream_text:
        with st.spinner('Processing...'):
            final_prompt = engineer_prompt(dream_text, target_model, style_preset)
            st.success(t["success"])
            
            # Displaying Result
            st.code(final_prompt, language="text")
            
            # Automatic Copy & User Notification
            st.copy_to_clipboard(final_prompt)
            st.toast(t["copy"], icon="✅")
    else:
        st.warning(t["input_req"])

# --- 6. FOOTER ---
st.divider()
st.caption("© 2026 Dream Engineering Tool | Hosted on Streamlit Cloud")
