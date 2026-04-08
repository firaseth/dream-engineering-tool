import streamlit as st
from google import genai
from google.genai import types

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Dream Architect Pro v3", page_icon="🌙", layout="wide")

# --- 2. THE AI ENGINE SETUP ---
try:
    if "GEMINI_API_KEY" in st.secrets:
        # Initializing the latest Google GenAI Client
        client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
    else:
        st.error("⚠️ API Key missing! Add GEMINI_API_KEY to your Secrets.")
except Exception as e:
    st.error(f"⚠️ Connection Error: {e}")

# --- 3. GLOBAL TRANSLATIONS (10 Languages) ---
languages = {
    "English": {"title": "🌙 AI Dream Architect", "btn": "Engineer Prompt", "success": "Analysis Complete!", "place": "Describe your dream...", "side": "Settings"},
    "العربية": {"title": "🌙 مهندس الأحلام الذكي", "btn": "هندسة المطالبة", "success": "تم التحليل!", "place": "صف حلمك هنا...", "side": "الإعدادات"},
    "中文": {"title": "🌙 AI 梦境建筑师", "btn": "生成提示词", "success": "分析完成！", "place": "描述你的梦境...", "side": "设置"},
    "Français": {"title": "🌙 Architecte de Rêves IA", "btn": "Générer le Prompt", "success": "Analyse terminée !", "place": "Décrivez votre rêve...", "side": "Paramètres"},
    "Español": {"title": "🌙 Arquitecto de Sueños IA", "btn": "Diseñar Prompt", "success": "¡Análisis completo!", "place": "Describe tu sueño...", "side": "Ajustes"},
    "Deutsch": {"title": "🌙 KI-Traumarchitekt", "btn": "Prompt erstellen", "success": "Analyse abgeschlossen!", "place": "Beschreibe deinen Traum...", "side": "Einstellungen"},
    "日本語": {"title": "🌙 AI 夢の建築家", "btn": "プロンプトを生成", "success": "分析完了！", "place": "夢の内容を入力してください...", "side": "設定"},
    "Русский": {"title": "🌙 ИИ Архитектор Снов", "btn": "Создать Промпт", "success": "Анализ завершен!", "place": "Опишите свой сон...", "side": "Настройки"},
    "हिन्दी": {"title": "🌙 AI स्वप्न वास्तुकार", "btn": "प्रॉम्ट तैयार करें", "success": "विश्लेषण पूरा हुआ!", "place": "अपने सपने का वर्णन करें...", "side": "सेटअप"},
    "Português": {"title": "🌙 Arquiteto de Sonhos IA", "btn": "Gerar Prompt", "success": "Análise concluída!", "place": "Descreva seu sonho...", "side": "Configurações"}
}

# --- 4. SIDEBAR ---
with st.sidebar:
    lang_choice = st.selectbox("Select Language / اختر اللغة", list(languages.keys()))
    t = languages[lang_choice]
    st.markdown("---")
    st.markdown("### Model Information")
    st.info("Core: Gemini 3 Flash")
    st.caption("v3.1.0-Release-2026")

# --- 5. MAIN INTERFACE ---
st.title(t["title"])

with st.container(border=True):
    dream_input = st.text_area("✍️", placeholder=t["place"], height=150)
    
    col1, col2 = st.columns(2)
    with col1:
        target_model = st.selectbox("Target Image Generator", ["Midjourney v8", "Sora 3", "Flux.2 Pro", "DALL-E 4"])
    with col2:
        # Creativity now maps to Gemini 3's temperature logic
        creativity = st.slider("Architect Creativity", 0.0, 1.0, 0.7)

# --- 6. GEMINI 3 LOGIC ---
def call_gemini(dream, model_target, temp):
    prompt_instruction = (
        f"You are a professional Prompt Engineer for {model_target}. "
        f"The user describes this dream: '{dream}'. "
        "Expand this into a master-level cinematic image generation prompt. "
        "Include lighting, atmospheric effects, specific textures, and camera settings. "
        "Return ONLY the final prompt text. No introduction or closing remarks."
    )
    
    try:
        # Using the March/April 2026 Model String
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
