import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Gabriela Michelotto — Professional Profile",
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
    photo = data_uri("foto-profissional-v2.png")
    st.markdown(f"""
    <style>
      header[data-testid="stHeader"], footer {{display:none;}}
      .block-container {{padding:0!important; max-width:100%!important;}}
      .stApp {{background:#efe9df;}}
      * {{box-sizing:border-box}}
      .pp {{font-family:Arial,Helvetica,sans-serif;color:#1c1c1c;max-width:1180px;margin:0 auto;padding:56px 54px 70px}}
      .hero {{display:grid;grid-template-columns:1.35fr .65fr;gap:44px;align-items:center;border-bottom:1px solid #c9c0b3;padding-bottom:38px}}
      .eyebrow {{font-size:12px;letter-spacing:.18em;text-transform:uppercase;color:#746d63;margin-bottom:18px}}
      h1 {{font-family:Georgia,serif;font-size:62px;line-height:.95;margin:0 0 16px;font-weight:500}}
      .role {{font-size:18px;letter-spacing:.09em;text-transform:uppercase;margin-bottom:20px}}
      .lead {{font-family:Georgia,serif;font-size:24px;line-height:1.4;max-width:760px;color:#3c3935}}
      .photo {{width:100%;aspect-ratio:4/5;object-fit:cover;border-radius:2px}}
      .section {{padding:34px 0;border-bottom:1px solid #d6cec3}}
      .section h2 {{font-family:Georgia,serif;font-size:28px;margin:0 0 16px;font-weight:500}}
      .section p {{font-size:16px;line-height:1.65;margin:0;color:#38342f}}
      .metrics {{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;margin-top:25px}}
      .metric {{padding:18px 0;border-top:1px solid #aaa094}}
      .metric b {{font-family:Georgia,serif;font-size:30px;font-weight:500;display:block}}
      .metric span {{font-size:13px;color:#6d665e;line-height:1.35}}
      .two {{display:grid;grid-template-columns:1fr 1fr;gap:46px}}
      .item {{margin-bottom:24px}}
      .item h3 {{font-size:17px;margin:0 0 4px}}
      .meta {{font-size:13px;color:#766f66;margin-bottom:8px}}
      .tags {{font-size:14px;line-height:1.7;color:#4c4741}}
      .cta {{padding-top:36px;display:flex;justify-content:space-between;gap:20px;align-items:end}}
      .cta strong {{font-family:Georgia,serif;font-size:28px;font-weight:500}}
      .links a {{color:#1c1c1c;text-decoration:none;border-bottom:1px solid #1c1c1c;margin-left:18px}}
      @media(max-width:800px){{.pp{{padding:28px 22px}}.hero,.two{{grid-template-columns:1fr}}.metrics{{grid-template-columns:1fr 1fr}}h1{{font-size:44px}}.lead{{font-size:20px}}.photo{{max-width:420px}}.cta{{display:block}}.links a{{display:block;margin:12px 0 0}}}}
    </style>
    <main class="pp">
      <section class="hero">
        <div>
          <div class="eyebrow">Recruiter Preview · 2026 · Cuiabá, Brazil</div>
          <h1>Gabriela<br>Michelotto</h1>
          <div class="role">Commercial Intelligence &amp; Sales Operations</div>
          <div class="lead">I turn commercial strategy into clear processes, data-informed decisions and sustainable growth.</div>
        </div>
        <img class="photo" src="{photo}" alt="Gabriela Michelotto">
      </section>

      <section class="section">
        <h2>Profile</h2>
        <p>8 years across B2B sales, commercial management and operations. My work evolved from client and distributor relationships to team leadership, portfolio ownership and targets, and now to pipeline, CRM, forecasting, BI and automation. I know what the numbers mean because I know the operation behind them.</p>
        <div class="metrics">
          <div class="metric"><b>8</b><span>years in B2B sales and commercial management</span></div>
          <div class="metric"><b>8</b><span>salespeople under commercial leadership</span></div>
          <div class="metric"><b>11</b><span>laboratory partners in portfolio management</span></div>
          <div class="metric"><b>12.8%</b><span>response rate in international outbound</span></div>
        </div>
      </section>

      <section class="section two">
        <div>
          <h2>Selected Experience</h2>
          <div class="item"><h3>Sales &amp; Pipeline Assistant · Rebecca Arnaud Design</h3><div class="meta">Jun 2026–Present · Freelance · Remote</div><p>International funnel ownership from sourcing through reporting: ICP qualification, tailored proposals in English, follow-up cadence, CRM hygiene in ClickUp/Notion, executive metrics and AI agents applied to prospecting.</p></div>
          <div class="item"><h3>Commercial Coordinator · SOMAPET Distribuição Pet</h3><div class="meta">Apr 2024–Aug 2026 · Cuiabá, Brazil</div><p>Led commercial performance, portfolio management, targets and forecasting. Structured pipeline routines and replaced recurring manual reporting with Python automation supported by Power BI and generative AI.</p></div>
        </div>
        <div>
          <h2>Core Focus</h2>
          <div class="tags">Pipeline · CRM · ICP · Forecasting · B2B Prospecting · Performance Analysis · Power BI · Python · AI Automation</div>
          <h2 style="margin-top:32px">Open To</h2>
          <div class="tags">Remote opportunities · International projects · Growth · Sales Ops · RevOps · Business Ops</div>
          <h2 style="margin-top:32px">Selected Projects</h2>
          <div class="item"><h3>SPB RevOps</h3><p>End-to-end commercial operation connecting revenue, funnel, win/loss and retention to a recommendation engine for stalled and lost opportunities.</p></div>
          <div class="item"><h3>B2B Executive Dashboard</h3><p>Executive view of sales, margin, delinquency, inventory and portfolio using Python, pandas, HTML/CSS and Chart.js.</p></div>
        </div>
      </section>

      <section class="cta">
        <strong>See the work behind the resume.</strong>
        <div class="links"><a href="/?lang=en">Full Portfolio</a><a href="mailto:gabrielamichelotto@gmail.com">Email</a><a href="https://www.linkedin.com/in/gabriela-michelotto" target="_blank">LinkedIn</a></div>
      </section>
    </main>
    """, unsafe_allow_html=True)
    st.stop()

template = "portfolio_en.html" if language == "en" else "portfolio.html"
html = (ROOT / template).read_text(encoding="utf-8")
html = html.replace('href="?lang=en"', 'href="/?lang=en"')
html = html.replace('href="?lang=pt"', 'href="/?lang=pt"')
for filename in ("foto-profissional-v2.png", "spb_preview.png", "painel_bi_preview.png"):
    html = html.replace(f'src="{filename}"', f'src="{data_uri(filename)}"')
st.markdown(html, unsafe_allow_html=True)
