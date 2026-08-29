import base64
from pathlib import Path
from urllib.parse import quote

import streamlit as st
import streamlit.components.v1 as components


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
if isinstance(language, list):
    language = language[0] if language else "pt"
language = str(language).lower().strip()
if language not in {"pt", "en"}:
    language = "pt"

profile = st.query_params.get("profile", "")
if isinstance(profile, list):
    profile = profile[0] if profile else ""

if str(profile).lower().strip() == "professional":
    st.markdown(
        """
        <style>
        header[data-testid="stHeader"] {display:none;}
        .stApp {background:#f4efe8;}
        .block-container {padding:0; max-width:100%;}
        </style>
        """,
        unsafe_allow_html=True,
    )
    pdf_url = "https://raw.githubusercontent.com/gabrielamichelotto-byte/professional-profile/main/Gabriela_Michelotto_Recruiter_Preview_EN(1).pdf"
    viewer_url = "https://docs.google.com/gview?embedded=1&url=" + quote(pdf_url, safe="")
    components.iframe(viewer_url, height=1100, scrolling=True)
    st.stop()

template = "portfolio_en.html" if language == "en" else "portfolio.html"
html = (ROOT / template).read_text(encoding="utf-8")

# Use an absolute query link so the language switch always reloads
# the app with the corresponding template.
html = html.replace('href="?lang=en"', 'href="/?lang=en"')
html = html.replace('href="?lang=pt"', 'href="/?lang=pt"')

for filename in ("foto-profissional-v2.png", "spb_preview.png", "painel_bi_preview.png"):
    html = html.replace(f'src="{filename}"', f'src="{data_uri(filename)}"')

st.markdown(html, unsafe_allow_html=True)
