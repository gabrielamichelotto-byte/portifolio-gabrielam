import streamlit as st
import base64, os

def _foto_b64():
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "foto.jpg")
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

_foto = _foto_b64()

st.set_page_config(
    page_title="Gabriela Michelotto · Portfólio",
    page_icon="💼",
    layout="wide"
)

# ── Idioma ──────────────────────────────────────
if "lang" not in st.session_state:
    st.session_state.lang = "PT"

# ── CSS ─────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
* { font-family: 'Inter', sans-serif; }
html, body, [data-testid="stAppViewContainer"], .main { background: #ffffff !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.hero { background: #0f0f0f; color: #ffffff; padding: 90px 80px 80px 80px; }
.hero-tag { font-size: 0.72rem; font-weight: 500; letter-spacing: 0.2em; text-transform: uppercase; color: #888; margin-bottom: 1.2rem; }
.hero-name { font-size: 3.8rem; font-weight: 800; line-height: 1.05; margin-bottom: 1rem; letter-spacing: -0.02em; }
.hero-title { font-size: 1.1rem; font-weight: 300; color: #aaa; margin-bottom: 2rem; max-width: 600px; line-height: 1.7; }
.hero-badge { display: inline-block; background: #ffffff15; border: 1px solid #333; color: #ccc; font-size: 0.75rem; font-weight: 400; padding: 0.35rem 0.9rem; border-radius: 20px; margin-right: 0.5rem; margin-bottom: 0.5rem; letter-spacing: 0.03em; }
.hero-stat { margin-top: 3rem; display: flex; gap: 3rem; }
.stat-num { font-size: 2.2rem; font-weight: 800; color: #fff; }
.stat-label { font-size: 0.72rem; font-weight: 400; color: #666; letter-spacing: 0.08em; text-transform: uppercase; }
.section { padding: 70px 80px; }
.section-alt { padding: 70px 80px; background: #f8f8f8; }
.section-label { font-size: 0.68rem; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: #999; margin-bottom: 0.5rem; }
.section-title { font-size: 2rem; font-weight: 800; color: #111; margin-bottom: 2.5rem; letter-spacing: -0.02em; }
.about-text { font-size: 1.05rem; font-weight: 300; color: #444; line-height: 1.9; max-width: 720px; }
.about-highlight { font-weight: 600; color: #111; }
.skill-group-title { font-size: 0.72rem; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: #999; margin-bottom: 0.8rem; }
.skill-pill { display: inline-block; background: #111; color: #fff; font-size: 0.8rem; font-weight: 400; padding: 0.4rem 1rem; border-radius: 4px; margin-right: 0.5rem; margin-bottom: 0.5rem; }
.skill-pill-light { display: inline-block; background: #f0f0f0; color: #333; font-size: 0.8rem; font-weight: 400; padding: 0.4rem 1rem; border-radius: 4px; margin-right: 0.5rem; margin-bottom: 0.5rem; }
.project-card { background: #fff; border: 1px solid #e8e8e8; border-radius: 8px; padding: 2rem; height: 100%; }
.project-card:hover { border-color: #111; }
.project-tag { font-size: 0.68rem; font-weight: 600; letter-spacing: 0.15em; text-transform: uppercase; color: #999; margin-bottom: 0.6rem; }
.project-name { font-size: 1.1rem; font-weight: 700; color: #111; margin-bottom: 0.6rem; }
.project-desc { font-size: 0.85rem; color: #666; font-weight: 300; line-height: 1.7; }
.project-link { display: inline-block; margin-top: 1.2rem; font-size: 0.78rem; font-weight: 600; color: #111; letter-spacing: 0.05em; text-decoration: none; border-bottom: 1px solid #111; padding-bottom: 1px; }
.contact-line { font-size: 1rem; font-weight: 300; color: #444; margin-bottom: 0.8rem; }
.contact-link { font-weight: 600; color: #111; text-decoration: none; }
.footer-bar { background: #0f0f0f; color: #555; text-align: center; font-size: 0.72rem; font-weight: 300; letter-spacing: 0.1em; padding: 1.5rem; }
.lang-bar { background: #0f0f0f; padding: 10px 80px; display: flex; justify-content: flex-end; }
.cta-btn { display: inline-block; background: #ffffff; color: #0f0f0f; font-size: 0.85rem; font-weight: 700; padding: 0.75rem 2rem; border-radius: 4px; text-decoration: none; letter-spacing: 0.04em; margin-right: 1rem; margin-top: 2rem; }
.cta-btn-outline { display: inline-block; background: transparent; color: #ffffff; font-size: 0.85rem; font-weight: 600; padding: 0.72rem 2rem; border-radius: 4px; border: 1px solid #555; text-decoration: none; letter-spacing: 0.04em; margin-top: 2rem; }
.cta-btn:hover { background: #e8e8e8; }
.cta-btn-outline:hover { border-color: #fff; color: #fff; }
.case-label { font-size: 0.65rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #bbb; margin-bottom: 0.4rem; }
.case-result { font-size: 0.78rem; font-weight: 600; color: #111; margin-top: 1rem; padding-top: 0.8rem; border-top: 1px solid #f0f0f0; }
#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
div[data-testid="stHorizontalBlock"] { gap: 0 !important; }
</style>
""", unsafe_allow_html=True)

# ── Seletor de idioma ────────────────────────────
st.markdown('<div style="background:#0f0f0f;padding:8px 80px;display:flex;justify-content:flex-end;">', unsafe_allow_html=True)
_, col_btn = st.columns([20, 1])
with col_btn:
    label = "🇺🇸 EN" if st.session_state.lang == "PT" else "🇧🇷 PT"
    if st.button(label, key="lang_toggle"):
        st.session_state.lang = "EN" if st.session_state.lang == "PT" else "PT"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

lang = st.session_state.lang

# ── Conteúdo bilíngue ────────────────────────────
T = {
    "hero_tag":        {"PT": "Portfólio Profissional",          "EN": "Professional Portfolio"},
    "hero_subtitle":   {"PT": "Coordenadora Comercial com 9 anos no mercado PET — unindo gestão de equipes, estratégia de dados e Inteligência Artificial para gerar resultados mensuráveis.",
                        "EN": "Sales Manager with 9 years in the pet industry — bridging team leadership, data strategy and AI to drive measurable business results."},
    "stat1":           {"PT": "Crescimento em 2025",             "EN": "Revenue Growth in 2025"},
    "stat2":           {"PT": "Profissionais liderados",         "EN": "Professionals Led"},
    "stat3":           {"PT": "Laboratórios parceiros",          "EN": "Partner Brands"},
    "stat4":           {"PT": "Anos de experiência",             "EN": "Years of Experience"},
    "about_label":     {"PT": "Sobre",                           "EN": "About"},
    "about_title":     {"PT": "Ciência, dados e estratégia<br>no mesmo lugar.", "EN": "Where science meets<br>data and strategy."},
    "about_body":      {
        "PT": 'Sou <span class="about-highlight">médica veterinária formada pela UFMT</span> e, ao longo de 9 anos no mercado, transformei minha base técnica em vantagem comercial. Hoje coordeno uma equipe de 14 profissionais na SOMAPET — distribuidora PET em Cuiabá — gerenciando campanhas, metas e estratégias com 11 laboratórios nacionais e multinacionais.<br><br>O que me diferencia é a capacidade de <span class="about-highlight">conectar dados a decisões</span>: uso Power BI para acompanhar indicadores em tempo real e aplico Inteligência Artificial com Claude para automatizar análises, otimizar processos e criar relatórios estratégicos.<br><br>Também desenvolvo <span class="about-highlight">manuais técnicos de treinamento</span> para vendedores e promotores iniciantes, aliados a acompanhamento a campo para acelerar o desenvolvimento individual da equipe.<br><br>Tenho pós-graduação em Gestão de Pessoas e acredito que <span class="about-highlight">liderança eficaz nasce da combinação entre técnica, empatia e visão de mercado.</span>',
        "EN": 'I am a <span class="about-highlight">Doctor of Veterinary Medicine (UFMT)</span> who has spent 9 years converting scientific expertise into commercial performance. As Sales Manager at SOMAPET — a leading pet products distributor in Cuiabá, Brazil — I oversee a team of 14 professionals across 11 national and multinational partner brands.<br><br>My differentiator is the ability to <span class="about-highlight">translate data into decisions</span>: I design real-time Power BI dashboards that give the team instant performance visibility, and I leverage AI (Claude) to automate reporting, surface insights and sharpen strategic focus.<br><br>I also create <span class="about-highlight">technical training manuals</span> for onboarding sales reps and promoters, paired with structured field coaching to accelerate each team member\'s professional growth.<br><br>I hold a Graduate Certificate in People Management and believe that <span class="about-highlight">high-impact leadership lives at the intersection of technical depth, emotional intelligence and market awareness.</span>',
    },
    "skills_label":    {"PT": "Competências",                    "EN": "Competencies"},
    "skills_title":    {"PT": "Ferramentas & habilidades.",      "EN": "Tools & expertise."},
    "sg_data":         {"PT": "Dados & Tecnologia",              "EN": "Data & Technology"},
    "sg_commercial":   {"PT": "Gestão Comercial",                "EN": "Sales & Commercial"},
    "sg_soft":         {"PT": "Comportamental",                  "EN": "Leadership & Soft Skills"},
    "sg_courses":      {"PT": "Cursos & Formação",               "EN": "Education & Certifications"},
    "skill_lead":      {"PT": "Liderança de equipes",            "EN": "Team Leadership"},
    "skill_goals":     {"PT": "Gestão de metas",                 "EN": "KPI & Target Management"},
    "skill_expansion": {"PT": "Expansão de mercado",             "EN": "Market Expansion"},
    "skill_portfolio": {"PT": "Gestão de carteira",              "EN": "Account Management"},
    "skill_comm":      {"PT": "Comunicação assertiva",           "EN": "Clear & Impactful Communication"},
    "skill_people":    {"PT": "Gestão de pessoas",               "EN": "People Development"},
    "skill_flex":      {"PT": "Flexibilidade",                   "EN": "Adaptability"},
    "skill_train":     {"PT": "Treinamento de equipes",          "EN": "Sales Team Coaching"},
    "skill_vision":    {"PT": "Visão estratégica",               "EN": "Strategic Thinking"},
    "course1":         {"PT": "Pós-graduação em Gestão de Pessoas", "EN": "Graduate Certificate — People & Leadership"},
    "course2":         {"PT": "Power BI do Básico ao Avançado",  "EN": "Power BI — Fundamentals to Advanced"},
    "course3":         {"PT": "Python para Análise de Dados",    "EN": "Python for Data Analysis"},
    "course4":         {"PT": "Inteligência Artificial Aplicada","EN": "Applied AI & Automation"},
    "course5":         {"PT": "Medicina Veterinária — UFMT",     "EN": "Doctor of Veterinary Medicine — UFMT"},
    "exp_label":       {"PT": "Trajetória",                      "EN": "Experience"},
    "exp_title":       {"PT": "Experiência profissional.",       "EN": "Professional background."},
    "proj_label":      {"PT": "Projetos",                        "EN": "Projects"},
    "proj_title":      {"PT": "O que já construí.",              "EN": "Selected work."},
    "proj1_desc":      {"PT": "Assistente de Inteligência Artificial com interface estilo diário, saudação dinâmica por horário e integração com Google Gemini. Construído do zero com Python.",
                        "EN": "Conversational AI assistant built from scratch in Python — featuring a handwritten diary aesthetic, time-aware dynamic greetings and Google Gemini integration."},
    "proj1_link":      {"PT": "Ver projeto →",                   "EN": "View project →"},
    "proj2_desc":      {"PT": "Dashboards em Power BI para acompanhamento em tempo real de performance por vendedor, laboratório e região. Suporte à tomada de decisão da liderança.",
                        "EN": "Real-time Power BI dashboards tracking commercial performance by sales rep, partner brand and region — designed to support data-driven decision-making at the leadership level."},
    "proj3_desc":      {"PT": "Geração automatizada de relatórios HTML a partir de planilhas Excel, com visualização de metas, resultados e acompanhamento de equipe.",
                        "EN": "Automated HTML report generation from Excel data sources, providing at-a-glance views of individual targets, results and overall team progress."},
    "proj4_name":      {"PT": "Manual de Vendas para Iniciantes",  "EN": "Sales Manual for Beginner Salespeople"},
    "proj4_tag":       {"PT": "Treinamento · RH",                  "EN": "Training · HR"},
    "proj4_desc":      {"PT": "Manual técnico desenvolvido para apoiar o RH no processo de onboarding de novos vendedores e promotores. Cobre técnicas de abordagem, conhecimento de produto, gestão de carteira e rotina de campo — acelerando a curva de aprendizado dos iniciantes.",
                        "EN": "Technical manual developed to support HR in the onboarding of new sales reps and promoters. Covers approach techniques, product knowledge, account management and field routines — shortening the learning curve for beginners."},
    "contact_label":   {"PT": "Contato",                         "EN": "Contact"},
    "contact_title":   {"PT": "Vamos conversar?",                "EN": "Let's connect."},
    "contact_loc":     {"PT": "Cuiabá, Mato Grosso — Brasil",    "EN": "Cuiabá, Mato Grosso — Brazil"},
    "footer":          {"PT": "GABRIELA BARROS MICHELOTTO &nbsp;·&nbsp; Cuiabá, MT &nbsp;·&nbsp; 2026",
                        "EN": "GABRIELA BARROS MICHELOTTO &nbsp;·&nbsp; Cuiabá, MT &nbsp;·&nbsp; 2026"},
    "cta_primary":     {"PT": "Falar Comigo",                     "EN": "Get in Touch"},
    "cta_secondary":   {"PT": "Ver LinkedIn",                     "EN": "View LinkedIn"},
    "case_challenge":  {"PT": "Contexto",                         "EN": "Challenge"},
    "case_action":     {"PT": "O que fiz",                        "EN": "What I did"},
    "case_result":     {"PT": "Resultado",                        "EN": "Result"},
    "proj1_challenge": {"PT": "Criar uma presença digital de IA sem experiência prévia em programação.",
                        "EN": "Build a production-ready AI showcase with zero prior programming experience."},
    "proj1_action":    {"PT": "Aprendi Python do zero e desenvolvi um assistente conversacional completo com Google Gemini.",
                        "EN": "Learned Python from scratch and built a full conversational assistant powered by Google Gemini."},
    "proj1_result":    {"PT": "App funcional publicado e no ar — acessível pelo link do portfólio.",
                        "EN": "Fully deployed app — live and accessible via portfolio link."},
    "proj2_challenge": {"PT": "Equipe de 14 pessoas sem visibilidade de performance em tempo real.",
                        "EN": "Team of 14 with no real-time visibility into individual or regional performance."},
    "proj2_action":    {"PT": "Construí dashboards em Power BI com indicadores por vendedor, laboratório e região.",
                        "EN": "Designed Power BI dashboards tracking KPIs by sales rep, partner brand and region."},
    "proj2_result":    {"PT": "Decisões de gestão passaram a ser orientadas por dados, com impacto direto no crescimento de 21%.",
                        "EN": "Management decisions became data-driven — directly contributing to 21% revenue growth."},
    "proj3_challenge": {"PT": "Relatórios manuais consumindo horas da liderança toda semana.",
                        "EN": "Manual reporting consuming hours of leadership time every week."},
    "proj3_action":    {"PT": "Automatizei a geração de relatórios HTML a partir de planilhas Excel.",
                        "EN": "Automated HTML report generation from Excel data sources."},
    "proj3_result":    {"PT": "Zero horas de trabalho manual — relatórios gerados em segundos.",
                        "EN": "Zero manual effort — reports generated in seconds."},
    "proj4_challenge": {"PT": "Alta rotatividade e curva longa de aprendizado para novos vendedores e promotores.",
                        "EN": "High turnover and long ramp-up time for new sales reps and promoters."},
    "proj4_action":    {"PT": "Criei manual técnico completo com rotas, abordagem, produto e gestão de carteira, em parceria com o RH.",
                        "EN": "Authored a complete technical manual covering field routes, sales approach, product knowledge and account management — in partnership with HR."},
    "proj4_result":    {"PT": "Onboarding mais rápido e padronizado, reduzindo dependência de treinamento individual.",
                        "EN": "Faster, standardized onboarding — reducing dependence on one-on-one training."},
}

def t(key):
    return T[key][lang]

# ── Experiências ─────────────────────────────────
experiencias = {
    "PT": [
        {
            "empresa": "SOMAPET",
            "cargo": "Coordenadora Comercial",
            "periodo": "ABRIL 2024 — PRESENTE · CUIABÁ, MT",
            "descricao": "Liderança de 14 profissionais (8 consultores + 6 promotores técnicos). Gestão de 11 laboratórios parceiros nacionais e multinacionais. Criação de manual técnico de vendas para apoiar o RH no onboarding de iniciantes, com acompanhamento a campo para desenvolvimento individual. Implementação de dashboards em Power BI e automação com IA (Claude). Crescimento de 21% no faturamento em 2025.",
            "sub_cargo": "Promotora Técnica · Virbac",
            "sub_periodo": "MAIO 2023 — ABRIL 2024",
            "sub_descricao": "Suporte técnico e promoção de produtos veterinários junto a clínicas, petshops e distribuidoras na região de Cuiabá.",
        },
        {
            "empresa": "ORGANNACT",
            "cargo": "Coordenadora Regional — MT/MS",
            "periodo": "AGOSTO 2019 — NOVEMBRO 2022 · MT/MS",
            "descricao": "Gestão comercial das equipes nos estados de MT e MS. Suporte técnico, treinamentos com médicos veterinários, desenvolvimento de carteira e elaboração de campanhas mensais junto às distribuidoras.",
        },
    ],
    "EN": [
        {
            "empresa": "SOMAPET",
            "cargo": "Sales Manager",
            "periodo": "APRIL 2024 — PRESENT · CUIABÁ, MT",
            "descricao": "Lead a team of 14 (8 sales consultants + 6 technical reps) across 11 national and multinational partner brands. Created a Sales Manual for Beginner Salespeople to support HR in onboarding, complemented by structured field coaching for individual development. Deployed Power BI dashboards for real-time KPI tracking and integrated AI automation (Claude) into reporting workflows. Delivered 21% revenue growth in 2025.",
            "sub_cargo": "Technical Sales Representative · Virbac",
            "sub_periodo": "MAY 2023 — APRIL 2024",
            "sub_descricao": "Provided field-level technical support and product promotion for Virbac across veterinary clinics, pet shops and distribution partners in the greater Cuiabá area.",
        },
        {
            "empresa": "ORGANNACT",
            "cargo": "Regional Sales Coordinator — MT/MS",
            "periodo": "AUGUST 2019 — NOVEMBER 2022 · MT/MS",
            "descricao": "Managed sales teams across two states (Mato Grosso and Mato Grosso do Sul). Delivered technical training to veterinary professionals, drove regional account growth and coordinated monthly promotional campaigns in partnership with local distributors.",
        },
    ],
}

# ════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════
_foto_html = f'<img src="data:image/jpeg;base64,{_foto}" style="width:320px;height:380px;object-fit:cover;object-position:top;border-radius:6px;display:block;">' if _foto else ""

st.markdown(f"""
<div class="hero" style="display:flex;align-items:flex-start;justify-content:space-between;gap:3rem;">
<div style="flex:1;min-width:0;">
<p class="hero-tag">{t("hero_tag")}</p>
<h1 class="hero-name">Gabriela Barros<br>Michelotto</h1>
<p class="hero-title">{t("hero_subtitle")}</p>
<div>
<span class="hero-badge">Power BI</span>
<span class="hero-badge">{'Inteligência Artificial' if lang=='PT' else 'Artificial Intelligence'}</span>
<span class="hero-badge">Python</span>
<span class="hero-badge">Excel</span>
<span class="hero-badge">{'Gestão Comercial' if lang=='PT' else 'Commercial Management'}</span>
<span class="hero-badge">{'Medicina Veterinária' if lang=='PT' else 'Veterinary Medicine'}</span>
</div>
<div>
<a class="cta-btn" href="mailto:gabrielamichelotto@gmail.com">{t("cta_primary")}</a>
<a class="cta-btn-outline" href="https://www.linkedin.com/in/gabrielamichelotto" target="_blank">{t("cta_secondary")}</a>
</div>
<div class="hero-stat">
<div><div class="stat-num">+21%</div><div class="stat-label">{t("stat1")}</div></div>
<div><div class="stat-num">14</div><div class="stat-label">{t("stat2")}</div></div>
<div><div class="stat-num">11</div><div class="stat-label">{t("stat3")}</div></div>
<div><div class="stat-num">9</div><div class="stat-label">{t("stat4")}</div></div>
</div>
</div>
<div style="flex-shrink:0;padding-top:0.5rem;">{_foto_html}</div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# SOBRE
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section">
<p class="section-label">{t("about_label")}</p>
<h2 class="section-title">{t("about_title")}</h2>
<p class="about-text">{t("about_body")}</p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# HABILIDADES
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section-alt">
<p class="section-label">{t("skills_label")}</p>
<h2 class="section-title">{t("skills_title")}</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""<div style="padding:0 80px 40px 80px;background:#f8f8f8;"><p class="skill-group-title">{t("sg_data")}</p><span class="skill-pill">Power BI</span><span class="skill-pill">Python</span><span class="skill-pill">Excel</span><span class="skill-pill">Claude AI</span><span class="skill-pill">Dashboards</span></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div style="padding:0 40px 40px 40px;background:#f8f8f8;"><p class="skill-group-title">{t("sg_commercial")}</p><span class="skill-pill-light">{t("skill_lead")}</span><span class="skill-pill-light">{t("skill_goals")}</span><span class="skill-pill-light">Sell out</span><span class="skill-pill-light">{t("skill_expansion")}</span><span class="skill-pill-light">{t("skill_portfolio")}</span></div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div style="padding:0 80px 40px 0;background:#f8f8f8;"><p class="skill-group-title">{t("sg_soft")}</p><span class="skill-pill-light">{t("skill_comm")}</span><span class="skill-pill-light">{t("skill_people")}</span><span class="skill-pill-light">{t("skill_flex")}</span><span class="skill-pill-light">{t("skill_train")}</span><span class="skill-pill-light">{t("skill_vision")}</span></div>""", unsafe_allow_html=True)

st.markdown(f"""<div style="padding:0 80px 50px 80px;background:#f8f8f8;"><p class="skill-group-title">{t("sg_courses")}</p><span class="skill-pill-light">{t("course1")}</span><span class="skill-pill-light">{t("course2")}</span><span class="skill-pill-light">{t("course3")}</span><span class="skill-pill-light">{t("course4")}</span><span class="skill-pill-light">{t("course5")}</span></div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# EXPERIÊNCIA
# ════════════════════════════════════════════════
st.markdown(f"""<div class="section"><p class="section-label">{t("exp_label")}</p><h2 class="section-title">{t("exp_title")}</h2></div>""", unsafe_allow_html=True)

exp_html = ""
for exp in experiencias[lang]:
    sub = ""
    if exp.get("sub_cargo"):
        sub = (
            '<div style="margin-top:1.2rem;padding-top:1rem;border-top:1px dashed #e8e8e8;">'
            f'<div style="font-size:0.78rem;font-weight:600;color:#888;">{exp["sub_cargo"]}</div>'
            f'<div style="font-size:0.68rem;color:#bbb;letter-spacing:0.05em;margin:0.2rem 0 0.5rem 0;">{exp["sub_periodo"]}</div>'
            f'<div style="font-size:0.8rem;color:#888;font-weight:300;line-height:1.7;">{exp["sub_descricao"]}</div>'
            '</div>'
        )
    exp_html += (
        '<div style="padding:0 80px;margin-bottom:2.5rem;">'
        '<div style="border-left:2px solid #e0e0e0;padding-left:1.5rem;">'
        f'<div style="font-size:1rem;font-weight:700;color:#111;">{exp["empresa"]}</div>'
        f'<div style="font-size:0.9rem;color:#555;margin-top:0.1rem;">{exp["cargo"]}</div>'
        f'<div style="font-size:0.7rem;color:#aaa;letter-spacing:0.06em;margin:0.4rem 0 0.8rem 0;">{exp["periodo"]}</div>'
        f'<div style="font-size:0.88rem;color:#555;font-weight:300;line-height:1.8;">{exp["descricao"]}</div>'
        f'{sub}'
        '</div></div>'
    )

st.markdown(exp_html, unsafe_allow_html=True)

# ════════════════════════════════════════════════
# PROJETOS
# ════════════════════════════════════════════════
st.markdown(f"""<div class="section-alt"><p class="section-label">{t("proj_label")}</p><h2 class="section-title">{t("proj_title")}</h2></div>""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""<div style="padding:0 20px 60px 80px;background:#f8f8f8;"><div class="project-card"><p class="project-tag">Python · Streamlit · AI</p><p class="project-name">{'Agente IA Pessoal' if lang=='PT' else 'Personal AI Agent'}</p><p class="case-label">{t("case_challenge")}</p><p class="project-desc">{t("proj1_challenge")}</p><p class="case-label" style="margin-top:0.7rem">{t("case_action")}</p><p class="project-desc">{t("proj1_action")}</p><p class="case-result">✦ {t("proj1_result")}</p><a class="project-link" href="https://github.com/gabrielamichelotto-byte/agente-gabriela" target="_blank" style="margin-top:1rem;display:inline-block">{t("proj1_link")}</a></div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div style="padding:0 20px 60px 20px;background:#f8f8f8;"><div class="project-card"><p class="project-tag">Power BI · {'Dados' if lang=='PT' else 'Data'}</p><p class="project-name">{'Dashboard Comercial' if lang=='PT' else 'Commercial Dashboard'}</p><p class="case-label">{t("case_challenge")}</p><p class="project-desc">{t("proj2_challenge")}</p><p class="case-label" style="margin-top:0.7rem">{t("case_action")}</p><p class="project-desc">{t("proj2_action")}</p><p class="case-result">✦ {t("proj2_result")}</p></div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div style="padding:0 80px 60px 20px;background:#f8f8f8;"><div class="project-card"><p class="project-tag">Python · Excel</p><p class="project-name">{'Dashboard BI de Vendedores' if lang=='PT' else 'Salesforce BI Dashboard'}</p><p class="case-label">{t("case_challenge")}</p><p class="project-desc">{t("proj3_challenge")}</p><p class="case-label" style="margin-top:0.7rem">{t("case_action")}</p><p class="project-desc">{t("proj3_action")}</p><p class="case-result">✦ {t("proj3_result")}</p></div></div>""", unsafe_allow_html=True)

c4, _, _ = st.columns(3)
with c4:
    st.markdown(f"""<div style="padding:0 20px 60px 80px;background:#f8f8f8;"><div class="project-card"><p class="project-tag">{t("proj4_tag")}</p><p class="project-name">{t("proj4_name")}</p><p class="case-label">{t("case_challenge")}</p><p class="project-desc">{t("proj4_challenge")}</p><p class="case-label" style="margin-top:0.7rem">{t("case_action")}</p><p class="project-desc">{t("proj4_action")}</p><p class="case-result">✦ {t("proj4_result")}</p></div></div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# CONTATO
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section">
<p class="section-label">{t("contact_label")}</p>
<h2 class="section-title">{t("contact_title")}</h2>
<p class="contact-line">📧 <a class="contact-link" href="mailto:gabrielamichelotto@gmail.com">gabrielamichelotto@gmail.com</a></p>
<p class="contact-line">💼 <a class="contact-link" href="https://www.linkedin.com/in/gabrielamichelotto" target="_blank">linkedin.com/in/gabrielamichelotto</a></p>
<p class="contact-line">📍 {t("contact_loc")}</p>
</div>
<div class="footer-bar">{t("footer")}</div>
""", unsafe_allow_html=True)
