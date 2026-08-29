import base64
from pathlib import Path

import streamlit as st


st.set_page_config(
    page_title="Gabriela Michelotto — Inteligência Comercial & Sales Operations",
    page_icon="GM",
    layout="wide",
    initial_sidebar_state="collapsed",
)

ROOT = Path(__file__).parent


def data_uri(filename: str) -> str:
    path = ROOT / filename
    if not path.exists():
        return ""
    mime = "image/jpeg" if path.suffix.lower() in {".jpg", ".jpeg"} else "image/png"
    encoded = base64.b64encode(path.read_bytes()).decode()
    return f"data:{mime};base64,{encoded}"


language = st.query_params.get("lang", "pt")
template = "portfolio_en.html" if language == "en" else "portfolio.html"
html = (ROOT / template).read_text(encoding="utf-8")
for filename in ("foto-profissional-v2.png", "spb_preview.png", "painel_bi_preview.png"):
    html = html.replace(f'src="{filename}"', f'src="{data_uri(filename)}"')

st.markdown(html, unsafe_allow_html=True)
