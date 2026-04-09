# 🌙 AI Dream Prompt

A professional engineering tool that transforms dream descriptions into high-fidelity, cinematic prompts for **Midjourney, Sora, Flux, and DALL-E**.

Built with **Streamlit** and powered by the **OpenRouter API** for universal AI model access.

---

## 🌍 1. Integrated AI Setup (Streamlit Cloud / "Unlocal")
The easiest way to use the app without installing anything on your computer.

1. **Fork** this repository to your own GitHub account.
2. Login to [Streamlit Community Cloud](https://share.streamlit.io/).
3. Click **"New app"** and select your forked repository.
4. Set the Main file path to: `dream_tool.py`.
5. **Crucial Step:** Go to **App Settings > Secrets** and paste your API key:
   ```toml
   OPENROUTER_API_KEY = "your_openrouter_key_here"
