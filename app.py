import streamlit as st
import base64, os

st.set_page_config(
    page_title="Gabriela Barros Michelotto",
    page_icon="◆",
    layout="wide"
)

# ── Idioma ───────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "PT"

# ── Foto via base64 ──────────────────────────────
def load_photo():
    for fname in ["foto.jpg.jpg", "foto.jpg", "foto.png"]:
        path = os.path.join(os.path.dirname(__file__) or ".", fname)
        if os.path.exists(path):
            with open(path, "rb") as f:
                return base64.b64encode(f.read()).decode()
    return None

photo_b64 = load_photo()
photo_src  = f"data:image/jpeg;base64,{photo_b64}" if photo_b64 else ""
photo_html = f'<img src="{photo_src}" alt="Gabriela Barros Michelotto" style="width:100%;max-width:440px;border-radius:6px;display:block;margin-left:auto;box-shadow:0 32px 80px rgba(0,0,0,0.5);">' if photo_src else ""

# ── CSS ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
*, *::before, *::after { font-family: 'Inter', sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
html, body, [data-testid="stAppViewContainer"], .main { background: #f7f3ee !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── TOPBAR ── */
.topbar {
  background: #0a0a0a;
  padding: 14px 80px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #1a1a1a;
}
.topbar-name { font-size: 0.7rem; font-weight: 600; color: #c9a96e; letter-spacing: 0.2em; text-transform: uppercase; }
.topbar-nav  { display: flex; gap: 2rem; }
.topbar-nav a { font-size: 0.7rem; font-weight: 400; color: #444; letter-spacing: 0.12em; text-transform: uppercase; text-decoration: none; }
.topbar-nav a:hover { color: #c9a96e; }

/* ── HERO ── */
.hero-wrap { background: #f7f3ee; }
.hero-grid {
  display: grid;
  grid-template-columns: 1fr 400px;
  gap: 5rem;
  padding: 90px 80px 80px 80px;
  align-items: center;
  max-width: 1400px;
}
.hero-eyebrow {
  font-size: 0.65rem;
  font-weight: 600;
  letter-spacing: 0.28em;
  text-transform: uppercase;
  color: #c9a96e;
  margin-bottom: 1.4rem;
}
.hero-name {
  font-size: 4.6rem;
  font-weight: 900;
  line-height: 1.0;
  letter-spacing: -0.03em;
  color: #0a0a0a !important;
  margin-bottom: 1.6rem;
}
.hero-subtitle {
  font-size: 1.05rem;
  font-weight: 300;
  color: #666;
  line-height: 1.8;
  max-width: 540px;
  margin-bottom: 0;
}
.hero-subtitle strong { color: #111; font-weight: 500; }

.hero-divider {
  width: 48px;
  height: 2px;
  background: #c9a96e;
  margin: 2.2rem 0;
}

.hero-stats { display: flex; gap: 3rem; align-items: flex-start; }
.stat-val {
  font-size: 2.2rem;
  font-weight: 800;
  color: #c9a96e;
  letter-spacing: -0.02em;
  line-height: 1;
}
.stat-lbl {
  font-size: 0.58rem;
  font-weight: 500;
  color: #999;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  margin-top: 0.35rem;
  line-height: 1.4;
}

.hero-cta { display: flex; gap: 1rem; margin-top: 2.4rem; align-items: center; }
.btn-primary {
  display: inline-block;
  width: fit-content;
  background: #c9a96e;
  color: #0a0a0a;
  font-size: 0.75rem;
  font-weight: 700;
  padding: 0.85rem 2.2rem;
  border-radius: 2px;
  text-decoration: none;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.btn-secondary {
  display: inline-block;
  width: fit-content;
  background: transparent;
  color: #555;
  font-size: 0.75rem;
  font-weight: 500;
  padding: 0.82rem 2.2rem;
  border-radius: 2px;
  border: 1px solid #bbb;
  text-decoration: none;
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.btn-primary:hover  { background: #b8975a; }
.btn-secondary:hover { border-color: #c9a96e; color: #c9a96e; }

/* ── SECTIONS ── */
.section      { padding: 88px 80px; background: #f7f3ee; }
.section-dark { padding: 88px 80px; background: #ede8e0; }
.section-mid  { padding: 88px 80px; background: #ede8e0; }

.eyebrow {
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.26em;
  text-transform: uppercase;
  color: #c9a96e;
  margin-bottom: 0.7rem;
  display: flex;
  align-items: center;
  gap: 0.6rem;
}
.eyebrow::before {
  content: '';
  display: inline-block;
  width: 20px;
  height: 1px;
  background: #c9a96e;
}
.section-heading {
  font-size: 2.4rem;
  font-weight: 800;
  color: #111;
  line-height: 1.12;
  letter-spacing: -0.025em;
  margin-bottom: 3rem;
}
.section-heading-white {
  font-size: 2.4rem;
  font-weight: 800;
  color: #111;
  line-height: 1.12;
  letter-spacing: -0.025em;
  margin-bottom: 3rem;
}

/* ── ABOUT ── */
.about-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 5rem;
  align-items: start;
}
.about-text {
  font-size: 1rem;
  font-weight: 300;
  color: #555;
  line-height: 2.0;
}
.about-text strong { color: #111; font-weight: 600; }
.about-text p { margin-bottom: 1.2rem; }

.pillar {
  border-top: 2px solid #c9a96e;
  padding-top: 1.2rem;
  margin-bottom: 1.8rem;
}
.pillar-title { font-size: 0.78rem; font-weight: 700; color: #111; margin-bottom: 0.4rem; letter-spacing: 0.02em; }
.pillar-text  { font-size: 0.85rem; font-weight: 300; color: #666; line-height: 1.7; }

/* ── SKILLS ── */
.skills-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2.5rem; margin-top: 0; }
.skill-group-name {
  font-size: 0.62rem;
  font-weight: 700;
  letter-spacing: 0.22em;
  text-transform: uppercase;
  color: #c9a96e;
  padding-bottom: 0.7rem;
  border-bottom: 1px solid #d8d0c5;
  margin-bottom: 1rem;
}
.skill-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.45rem 0;
  border-bottom: 1px solid #ede8e0;
  font-size: 0.85rem;
  font-weight: 400;
  color: #444;
}
.skill-row:last-child { border-bottom: none; }

/* ── EXPERIENCE ── */
.exp-item {
  border-left: 2px solid #c9a96e;
  padding-left: 2rem;
  margin-bottom: 3rem;
  position: relative;
}
.exp-item::before {
  content: '';
  width: 8px;
  height: 8px;
  background: #c9a96e;
  border-radius: 50%;
  position: absolute;
  left: -5px;
  top: 6px;
}
.exp-company { font-size: 1rem; font-weight: 800; color: #111; letter-spacing: -0.01em; }
.exp-role    { font-size: 0.92rem; font-weight: 300; color: #666; margin-top: 0.2rem; }
.exp-period  {
  font-size: 0.62rem;
  font-weight: 600;
  color: #c9a96e;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  margin: 0.6rem 0 1rem;
}
.exp-desc { font-size: 0.88rem; font-weight: 300; color: #555; line-height: 1.9; }
.exp-sub {
  margin-top: 1.4rem;
  padding-top: 1.2rem;
  border-top: 1px dashed #ccc;
}
.exp-sub-role   { font-size: 0.78rem; font-weight: 600; color: #444; }
.exp-sub-period { font-size: 0.6rem; color: #888; letter-spacing: 0.08em; margin: 0.25rem 0 0.6rem; }
.exp-sub-desc   { font-size: 0.82rem; color: #666; font-weight: 300; line-height: 1.75; }

/* ── CASES ── */
.cases-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-top: 0; }
.case-card {
  background: #fff;
  border: 1px solid #e8e2d9;
  border-top: 3px solid #c9a96e;
  border-radius: 4px;
  padding: 2rem;
  height: 100%;
}
.case-tag  {
  font-size: 0.6rem;
  font-weight: 700;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: #c9a96e;
  margin-bottom: 0.8rem;
}
.case-name {
  font-size: 0.98rem;
  font-weight: 700;
  color: #111;
  margin-bottom: 1.4rem;
  line-height: 1.35;
}
.case-lbl {
  font-size: 0.58rem;
  font-weight: 700;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: #bbb;
  margin: 0.9rem 0 0.35rem;
}
.case-lbl:first-of-type { margin-top: 0; }
.case-text { font-size: 0.82rem; color: #666; font-weight: 300; line-height: 1.7; }
.case-result {
  font-size: 0.78rem;
  font-weight: 600;
  color: #111;
  margin-top: 1.3rem;
  padding-top: 0.9rem;
  border-top: 1px solid #f0ebe3;
}
.case-link {
  display: inline-block;
  margin-top: 1rem;
  font-size: 0.7rem;
  font-weight: 700;
  color: #c9a96e;
  letter-spacing: 0.1em;
  text-decoration: none;
  text-transform: uppercase;
  border-bottom: 1px solid #c9a96e;
  padding-bottom: 1px;
}

/* ── CONTACT ── */
.contact-item { font-size: 0.95rem; font-weight: 300; color: #666; margin-bottom: 1.1rem; line-height: 1.6; }
.contact-item a { font-weight: 500; color: #c9a96e; text-decoration: none; }
.contact-item a:hover { color: #b8975a; }
.contact-label { font-size: 0.6rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: #999; display: block; margin-bottom: 0.25rem; }

/* ── FOOTER ── */
.footer-bar {
  background: #050505;
  color: #2a2a2a;
  text-align: center;
  font-size: 0.65rem;
  font-weight: 400;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 2rem;
}

/* ── STATS STRIP ── */
.stats-strip { background: #0a0a0a; padding: 0 80px 60px 80px; }
.stats-grid  { display: flex; gap: 3rem; }
.stat-card   { min-width: 90px; }
.stat-num    { font-size: 2.1rem; font-weight: 800; color: #c9a96e; letter-spacing: -0.02em; line-height: 1; }
.stat-label  { font-size: 0.62rem; font-weight: 400; color: #555; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 0.3rem; line-height: 1.5; }

/* ── VALUE PILLARS ── */
.pillars     { display: grid; grid-template-columns: repeat(3,1fr); gap: 2rem; padding: 48px 80px 56px; background: #ede8e0; border-top: 1px solid #ddd6ca; }
.pillar-icon { font-size: 1.2rem; margin-bottom: 0.8rem; }
.pillar-title { font-size: 0.78rem; font-weight: 700; color: #111; margin-bottom: 0.4rem; letter-spacing: 0.04em; text-transform: uppercase; }
.pillar-body { font-size: 0.85rem; font-weight: 300; color: #666; line-height: 1.7; }

/* ── HIDE STREAMLIT ── */
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
div[data-testid="stHorizontalBlock"] { gap: 0 !important; }
[data-testid="stButton"] > button {
  background: #0a0a0a !important;
  border: 1px solid #c9a96e !important;
  color: #c9a96e !important;
  font-size: 0.72rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.14em !important;
  text-transform: uppercase !important;
  padding: 0.5rem 1.4rem !important;
  border-radius: 2px !important;
}
[data-testid="stButton"] > button:hover { background: #c9a96e !important; color: #0a0a0a !important; }
</style>
""", unsafe_allow_html=True)

# ── Conteúdo bilíngue ────────────────────────────
lang = st.session_state.lang

T = {
  # HERO
  "eyebrow":       {"PT": "Gestora Comercial · Estratégia & Dados",
                    "EN": "Commercial Manager · Strategy & Data"},
  "subtitle":      {"PT": "9 anos no mercado PET transformando <strong>liderança de equipes</strong>, <strong>análise de dados</strong> e <strong>Inteligência Artificial</strong> em crescimento mensurável.",
                    "EN": "9 years in the pet industry translating <strong>team leadership</strong>, <strong>data analysis</strong> and <strong>AI</strong> into measurable commercial growth."},
  "stat1":         {"PT": "Crescimento<br>2025",           "EN": "Growth<br>2025"},
  "stat2":         {"PT": "Profissionais<br>liderados",   "EN": "Professionals<br>led"},
  "stat3":         {"PT": "Laboratórios<br>parceiros",    "EN": "Partner<br>brands"},
  "stat4":         {"PT": "Anos de<br>experiência",       "EN": "Years of<br>experience"},
  "cta1":          {"PT": "Entrar em Contato",            "EN": "Get in Touch"},
  "cta2":          {"PT": "Ver LinkedIn",                 "EN": "View LinkedIn"},
  # ABOUT
  "about_ey":      {"PT": "Sobre",                        "EN": "About"},
  "about_h":       {"PT": "Ciência, dados e<br>estratégia comercial.",
                    "EN": "Where science meets<br>commercial strategy."},
  "about_p1":      {"PT": "Médica Veterinária formada pela UFMT, construí minha carreira na intersecção entre <strong>conhecimento técnico e gestão comercial</strong>. Ao longo de 9 anos no mercado PET, desenvolvi a capacidade de traduzir dados em decisões — e decisões em resultados.",
                    "EN": "A Doctor of Veterinary Medicine from UFMT, I have built my career at the intersection of <strong>technical expertise and commercial leadership</strong>. Over 9 years in the pet industry, I have developed the ability to translate data into decisions — and decisions into results."},
  "about_p2":      {"PT": "Hoje coordeno uma equipe de <strong>14 profissionais na SOMAPET</strong> — distribuidora PET em Cuiabá — gerenciando estratégias com 11 laboratórios nacionais e multinacionais, implementando dashboards em Power BI e automação com IA.",
                    "EN": "Today I lead a team of <strong>14 professionals at SOMAPET</strong> — a PET distributor in Cuiabá — managing strategies with 11 national and multinational partner brands, implementing Power BI dashboards and AI-driven automation."},
  "p1_t":          {"PT": "Liderança",                   "EN": "Leadership"},
  "p1_d":          {"PT": "Gestão de equipes comerciais com foco em desenvolvimento individual, metas e alta performance.",
                    "EN": "Commercial team management focused on individual development, goal-setting and high performance."},
  "p2_t":          {"PT": "Dados & Tecnologia",          "EN": "Data & Technology"},
  "p2_d":          {"PT": "Power BI, Python e Inteligência Artificial aplicados à tomada de decisão estratégica e automação de processos.",
                    "EN": "Power BI, Python and AI applied to strategic decision-making and process automation."},
  "p3_t":          {"PT": "Visão de Negócio",            "EN": "Business Acumen"},
  "p3_d":          {"PT": "Gestão de carteira, sell-out, campanhas mensais e relacionamento B2B com laboratórios parceiros.",
                    "EN": "Account management, sell-out strategies, monthly campaigns and B2B relationships with partner brands."},
  # SKILLS
  "sk_ey":         {"PT": "Competências",                "EN": "Competencies"},
  "sk_h":          {"PT": "Ferramentas &<br>habilidades.", "EN": "Tools &<br>expertise."},
  "sk_data":       {"PT": "Dados & Tecnologia",          "EN": "Data & Technology"},
  "sk_comm":       {"PT": "Gestão Comercial",            "EN": "Sales & Commercial"},
  "sk_lead":       {"PT": "Liderança & Soft Skills",     "EN": "Leadership & Soft Skills"},
  "sk_edu":        {"PT": "Formação",                    "EN": "Education"},
  # EXP
  "exp_ey":        {"PT": "Trajetória",                  "EN": "Experience"},
  "exp_h":         {"PT": "Experiência<br>profissional.", "EN": "Professional<br>background."},
  # CASES
  "case_ey":       {"PT": "Realizações",                 "EN": "Selected Work"},
  "case_h":        {"PT": "O que já construí.",          "EN": "Cases & deliverables."},
  "ctx":           {"PT": "Contexto",                    "EN": "Challenge"},
  "act":           {"PT": "O que fiz",                   "EN": "What I did"},
  "res":           {"PT": "Resultado",                   "EN": "Result"},
  "see":           {"PT": "Ver projeto",                 "EN": "View project"},
  # CONTACT
  "ct_ey":         {"PT": "Contato",                     "EN": "Contact"},
  "ct_h":          {"PT": "Vamos conversar.",            "EN": "Let's connect."},
  "ct_loc":        {"PT": "Cuiabá, Mato Grosso — Brasil", "EN": "Cuiabá, Mato Grosso — Brazil"},
  # FOOTER
  "footer":        {"PT": "Gabriela Barros Michelotto &nbsp;·&nbsp; Cuiabá, MT &nbsp;·&nbsp; 2026",
                    "EN": "Gabriela Barros Michelotto &nbsp;·&nbsp; Cuiabá, MT &nbsp;·&nbsp; 2026"},
  # CASES content
  "c1_tag":  {"PT": "Python · Streamlit · IA",           "EN": "Python · Streamlit · AI"},
  "c1_name": {"PT": "Agente IA Pessoal",                 "EN": "Personal AI Agent"},
  "c1_ctx":  {"PT": "Construir presença digital em IA sem experiência prévia em programação.",
              "EN": "Build an AI-powered digital presence with no prior programming background."},
  "c1_act":  {"PT": "Aprendi Python do zero e desenvolvi assistente conversacional com Google Gemini.",
              "EN": "Learned Python from scratch and built a full conversational assistant powered by Google Gemini."},
  "c1_res":  {"PT": "App funcional publicado — acessível pelo portfólio.",
              "EN": "Fully deployed app — live and accessible via portfolio."},
  "c1_link": {"PT": "Ver projeto", "EN": "View project"},
  "c2_tag":  {"PT": "Power BI · Dados",                  "EN": "Power BI · Data"},
  "c2_name": {"PT": "Dashboard Comercial",               "EN": "Commercial Dashboard"},
  "c2_ctx":  {"PT": "Equipe de 14 sem visibilidade de performance em tempo real.",
              "EN": "Team of 14 with no real-time visibility into individual or regional performance."},
  "c2_act":  {"PT": "Dashboards em Power BI com KPIs por vendedor, laboratório e região.",
              "EN": "Designed Power BI dashboards tracking KPIs by sales rep, brand and region."},
  "c2_res":  {"PT": "Gestão orientada por dados — contribuição direta para crescimento de 21%.",
              "EN": "Data-driven management — direct contribution to 21% revenue growth."},
  "c3_tag":  {"PT": "Python · Excel",                    "EN": "Python · Excel"},
  "c3_name": {"PT": "Automação de Relatórios",           "EN": "Report Automation"},
  "c3_ctx":  {"PT": "Relatórios manuais consumindo horas da liderança toda semana.",
              "EN": "Manual reporting consuming hours of leadership time every week."},
  "c3_act":  {"PT": "Automatizei geração de relatórios HTML a partir de planilhas Excel.",
              "EN": "Automated HTML report generation from Excel data sources."},
  "c3_res":  {"PT": "Redução significativa de retrabalho — relatórios gerados em segundos.",
              "EN": "Significant reduction in manual effort — reports generated in seconds."},
  "c4_tag":  {"PT": "Treinamento · RH",                  "EN": "Training · HR"},
  "c4_name": {"PT": "Manual de Vendas para Iniciantes",  "EN": "Sales Manual for Beginners"},
  "c4_ctx":  {"PT": "Alta rotatividade e curva longa de aprendizado para novos vendedores.",
              "EN": "High turnover and slow onboarding for new sales reps and promoters."},
  "c4_act":  {"PT": "Manual completo para iniciantes: pipeline, abordagem comercial e técnicas de negociação.",
              "EN": "Complete beginner sales manual: pipeline management, commercial approach and negotiation techniques."},
  "c4_res":  {"PT": "Onboarding mais rápido e padronizado, menor dependência de treinamento individual.",
              "EN": "Faster, standardized onboarding — reducing dependence on one-on-one coaching."},
}

T["skill_lead"] = {"PT": "Liderança de equipes", "EN": "Team Leadership"}

def t(k): return T[k][lang]

experiencias = {
  "PT": [
    {"empresa": "SOMAPET", "cargo": "Coordenadora Comercial",
     "periodo": "ABRIL 2024 — PRESENTE · CUIABÁ, MT",
     "descricao": "Liderança de 14 profissionais — 8 consultores de vendas e 6 promotores técnicos. Gestão estratégica de 11 laboratórios parceiros nacionais e multinacionais. Implementação de dashboards em Power BI e automação com IA (Claude) para análises e relatórios. Crescimento de 21% no faturamento em 2025.",
     "sub_cargo": "Promotora Técnica · Virbac",
     "sub_periodo": "MAIO 2023 — ABRIL 2024",
     "sub_desc": "Suporte técnico e promoção de produtos veterinários junto a clínicas, petshops e distribuidoras em Cuiabá."},
    {"empresa": "ORGANNACT", "cargo": "Coordenadora Regional — MT/MS",
     "periodo": "AGOSTO 2019 — NOVEMBRO 2022 · MT/MS",
     "descricao": "Gestão comercial de equipes nos estados de MT e MS. Treinamentos técnicos com médicos veterinários, desenvolvimento de carteira e campanhas mensais junto às distribuidoras parceiras."},
  ],
  "EN": [
    {"empresa": "SOMAPET", "cargo": "Sales Manager",
     "periodo": "APRIL 2024 — PRESENT · CUIABÁ, MT",
     "descricao": "Lead a team of 14 — 8 sales consultants and 6 technical promoters — across 11 national and multinational partner brands. Deployed Power BI dashboards for real-time KPI visibility and integrated AI automation (Claude) into reporting workflows. Delivered 21% revenue growth in 2025.",
     "sub_cargo": "Technical Sales Rep · Virbac",
     "sub_periodo": "MAY 2023 — APRIL 2024",
     "sub_desc": "Field-level technical support and product promotion for Virbac across veterinary clinics, pet shops and distributors in the greater Cuiabá area."},
    {"empresa": "ORGANNACT", "cargo": "Regional Sales Coordinator — MT/MS",
     "periodo": "AUGUST 2019 — NOVEMBER 2022 · MT/MS",
     "descricao": "Managed sales teams across Mato Grosso and Mato Grosso do Sul. Delivered technical training to veterinary professionals, drove regional account growth and coordinated monthly promotional campaigns with local distributors."},
  ],
}

# ════════════════════════════════════════════════
# TOPBAR + IDIOMA
# ════════════════════════════════════════════════
st.markdown('<div class="topbar"><span class="topbar-name">Gabriela Barros Michelotto</span></div>', unsafe_allow_html=True)
_, col_lang = st.columns([20, 1])
with col_lang:
    label = "🇺🇸 EN" if lang == "PT" else "🇧🇷 PT"
    if st.button(label, key="lang_btn"):
        st.session_state.lang = "EN" if lang == "PT" else "PT"
        st.rerun()
# compensate button spacing
st.markdown('<style>div[data-testid="stHorizontalBlock"]{margin-top:-52px;padding-right:20px;justify-content:flex-end;background:#0a0a0a;}</style>', unsafe_allow_html=True)

# ════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════
badges_pt = ["Power BI", "Inteligência Artificial", "Python", "Excel", "Channel Sales", "Medicina Veterinária", "Gestão de Pessoas"]
badges_en = ["Power BI", "Artificial Intelligence", "Python", "Excel", "Channel Sales", "Veterinary Medicine", "People Management"]
badges = badges_pt if lang == "PT" else badges_en
badges_html = "".join(f'<span class="hero-badge">{b}</span>' for b in badges)

st.markdown(f"""
<div class="hero-wrap">
<div class="hero-grid">
  <div>
    <p class="hero-eyebrow">{t("eyebrow")}</p>
    <h1 class="hero-name" style="color:#0a0a0a !important;">Gabriela Barros<br>Michelotto</h1>
    <p class="hero-subtitle">{t("subtitle")}</p>
    <div class="hero-divider"></div>
    <div class="hero-stats">
      <div><div class="stat-val">+21%</div><div class="stat-lbl">{'Crescimento 2025' if lang=='PT' else 'Growth 2025'}</div></div>
      <div><div class="stat-val">14</div><div class="stat-lbl">{'Profissionais' if lang=='PT' else 'Professionals'}</div></div>
      <div><div class="stat-val">11</div><div class="stat-lbl">{'Laboratórios' if lang=='PT' else 'Partner brands'}</div></div>
      <div><div class="stat-val">9</div><div class="stat-lbl">{'Anos exp.' if lang=='PT' else 'Years exp.'}</div></div>
    </div>
    <div class="hero-cta">
      <a class="btn-primary" href="mailto:gabrielamichelotto@gmail.com" onclick="window.open('mailto:gabrielamichelotto@gmail.com');return false;" style="cursor:pointer;">{t("cta1")}</a>
      <a class="btn-secondary" href="https://www.linkedin.com/in/gabriela-michelotto/" target="_blank">{t("cta2")}</a>
    </div>
  </div>
  <div>{photo_html}</div>
</div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# VALUE PILLARS
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="pillars">
<div class="pillar"><div class="pillar-icon">🎯</div><div class="pillar-title">{t("p1_t")}</div><div class="pillar-body">{t("p1_d")}</div></div>
<div class="pillar"><div class="pillar-icon">📊</div><div class="pillar-title">{t("p2_t")}</div><div class="pillar-body">{t("p2_d")}</div></div>
<div class="pillar"><div class="pillar-icon">👥</div><div class="pillar-title">{t("p3_t")}</div><div class="pillar-body">{t("p3_d")}</div></div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# ABOUT
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section">
  <p class="eyebrow">{t("about_ey")}</p>
  <h2 class="section-heading">{t("about_h")}</h2>
  <div class="about-grid">
    <div class="about-text">
      <p>{t("about_p1")}</p>
      <p>{t("about_p2")}</p>
    </div>
    <div>
      <div class="pillar">
        <div class="pillar-title">{t("p1_t")}</div>
        <div class="pillar-text">{t("p1_d")}</div>
      </div>
      <div class="pillar">
        <div class="pillar-title">{t("p2_t")}</div>
        <div class="pillar-text">{t("p2_d")}</div>
      </div>
      <div class="pillar">
        <div class="pillar-title">{t("p3_t")}</div>
        <div class="pillar-text">{t("p3_d")}</div>
      </div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# SKILLS
# ════════════════════════════════════════════════
sk_data = ["Power BI", "Python", "Excel", "Claude AI", "Dashboards", "Automação"]
sk_comm = [t("skill_lead") if "skill_lead" in T else "Liderança de equipes",
           "Sell-out & Campanhas",
           "Gestão de carteira",
           "Expansão de mercado",
           "Relacionamento B2B"]
sk_lead = ["Comunicação assertiva", "Gestão de pessoas", "Visão estratégica",
           "Treinamento de equipes", "Adaptabilidade"]
sk_edu  = ["Pós-graduação em Gestão de Pessoas" if lang=="PT" else "Graduate Certificate — People & Leadership",
           "Power BI — Básico ao Avançado" if lang=="PT" else "Power BI — Fundamentals to Advanced",
           "Python para Análise de Dados" if lang=="PT" else "Python for Data Analysis",
           "Medicina Veterinária — UFMT" if lang=="PT" else "Doctor of Veterinary Medicine — UFMT",
           "Pós-grad. Perícia Criminal (cursando)" if lang=="PT" else "Graduate — Criminal Forensics (ongoing)"]

def skill_rows(items):
    return "".join(f'<div class="skill-row">{i}</div>' for i in items)

st.markdown(f"""
<div class="section-mid">
  <p class="eyebrow">{t("sk_ey")}</p>
  <h2 class="section-heading">{t("sk_h")}</h2>
  <div class="skills-grid">
    <div>
      <div class="skill-group-name">{t("sk_data")}</div>
      {skill_rows(sk_data)}
    </div>
    <div>
      <div class="skill-group-name">{t("sk_comm")}</div>
      {skill_rows(sk_comm)}
    </div>
    <div>
      <div class="skill-group-name">{t("sk_lead")}</div>
      {skill_rows(sk_lead)}
    </div>
  </div>
  <div style="margin-top:2.5rem;">
    <div class="skill-group-name">{t("sk_edu")}</div>
    <div style="display:flex;flex-wrap:wrap;gap:0.6rem;margin-top:0.8rem;">
      {"".join(f'<span style="background:#fff;border:1px solid #d8d0c5;border-radius:3px;padding:0.35rem 1rem;font-size:0.8rem;color:#555;font-weight:400;">{e}</span>' for e in sk_edu)}
    </div>
  </div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# EXPERIENCE
# ════════════════════════════════════════════════
exp_items = ""
for e in experiencias[lang]:
    sub = ""
    if e.get("sub_cargo"):
        sub = (
            '<div class="exp-sub">'
            f'<div class="exp-sub-role">{e["sub_cargo"]}</div>'
            f'<div class="exp-sub-period">{e["sub_periodo"]}</div>'
            f'<div class="exp-sub-desc">{e["sub_desc"]}</div>'
            '</div>'
        )
    exp_items += (
        '<div class="exp-item">'
        f'<div class="exp-company">{e["empresa"]}</div>'
        f'<div class="exp-role">{e["cargo"]}</div>'
        f'<div class="exp-period">{e["periodo"]}</div>'
        f'<div class="exp-desc">{e["descricao"]}</div>'
        f'{sub}'
        '</div>'
    )

st.markdown(f"""
<div class="section-dark">
  <p class="eyebrow">{t("exp_ey")}</p>
  <h2 class="section-heading-white">{t("exp_h")}</h2>
  {exp_items}
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# CASES
# ════════════════════════════════════════════════
def case_card(tag, name, ctx, act, res, link=None):
    link_html = f'<a class="case-link" href="{link}" target="_blank">{t("see")} →</a>' if link else ""
    return (
        '<div class="case-card">'
        f'<p class="case-tag">{tag}</p>'
        f'<p class="case-name">{name}</p>'
        f'<p class="case-lbl">{t("ctx")}</p><p class="case-text">{ctx}</p>'
        f'<p class="case-lbl">{t("act")}</p><p class="case-text">{act}</p>'
        f'<p class="case-result">◆ {res}</p>'
        f'{link_html}'
        '</div>'
    )

c1 = case_card(t("c1_tag"),t("c1_name"),t("c1_ctx"),t("c1_act"),t("c1_res"),"https://github.com/gabrielamichelotto-byte/agente-gabriela")
c2 = case_card(t("c2_tag"),t("c2_name"),t("c2_ctx"),t("c2_act"),t("c2_res"))
c3 = case_card(t("c3_tag"),t("c3_name"),t("c3_ctx"),t("c3_act"),t("c3_res"))
c4 = case_card(t("c4_tag"),t("c4_name"),t("c4_ctx"),t("c4_act"),t("c4_res"))

st.markdown(f'<div class="section"><p class="eyebrow">{t("case_ey")}</p><h2 class="section-heading">{t("case_h")}</h2><div class="cases-grid">{c1}{c2}{c3}{c4}</div></div>', unsafe_allow_html=True)

# ════════════════════════════════════════════════
# CONTACT
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section-dark">
  <p class="eyebrow">{t("ct_ey")}</p>
  <h2 class="section-heading-white">{t("ct_h")}</h2>
  <div class="contact-item">
    <span class="contact-label">E-mail</span>
    <a href="mailto:gabrielamichelotto@gmail.com" onclick="window.open('mailto:gabrielamichelotto@gmail.com');return false;">gabrielamichelotto@gmail.com</a>
  </div>
  <div class="contact-item">
    <span class="contact-label">LinkedIn</span>
    <a href="https://www.linkedin.com/in/gabriela-michelotto/" target="_blank">linkedin.com/in/gabriela-michelotto</a>
  </div>
  <div class="contact-item">
    <span class="contact-label">{'Localização' if lang=='PT' else 'Location'}</span>
    <span style="color:#888;">{t("ct_loc")}</span>
  </div>
  <div style="margin-top:2.5rem;">
    <a class="btn-primary" onclick="window.open('mailto:gabrielamichelotto@gmail.com');return false;" style="cursor:pointer;">{t("cta1")}</a>
  </div>
</div>
<div class="footer-bar">{t("footer")}</div>
""", unsafe_allow_html=True)

