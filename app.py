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
    page_title="Gabriela Michelotto · Portfolio",
    page_icon="💼",
    layout="wide"
)

if "lang" not in st.session_state:
    st.session_state.lang = "PT"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');
:root {
    --navy:      #0D1B2A;
    --teal:      #2EC4B6;
    --teal-dark: #1DA89E;
    --teal-bg:   #F0FAFA;
    --white:     #FFFFFF;
    --ink:       #111827;
    --gray:      #6B7280;
    --light:     #F9FAFB;
    --border:    #E5E7EB;
}
* { font-family: 'Inter', sans-serif; box-sizing: border-box; margin: 0; padding: 0; }
html, body, [data-testid="stAppViewContainer"], .main { background: var(--white) !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ── TOPBAR ── */
.topbar { background: var(--navy); padding: 10px 80px; display: flex; justify-content: flex-end; align-items: center; }

/* ── HERO ── */
.hero { background: var(--navy); color: var(--white); padding: 80px 80px 70px; border-bottom: 3px solid var(--teal); }
.hero-inner { display: flex; align-items: flex-start; justify-content: space-between; gap: 3rem; }
.hero-text { flex: 1; min-width: 0; }
.hero-photo-wrap { flex-shrink: 0; padding-top: 0.5rem; }
.hero-eyebrow { font-size: 0.7rem; font-weight: 600; letter-spacing: 0.25em; text-transform: uppercase; color: var(--teal); margin-bottom: 1rem; }
.hero-name { font-size: 3.6rem; font-weight: 900; line-height: 1.03; margin-bottom: 0.9rem; letter-spacing: -0.03em; color: var(--white); }
.hero-title { font-size: 1.05rem; font-weight: 300; color: #94A3B8; margin-bottom: 1.8rem; max-width: 580px; line-height: 1.75; }
.hero-badge { display: inline-block; border: 1px solid #1E3A5F; color: #94A3B8; font-size: 0.72rem; font-weight: 500; padding: 0.3rem 0.85rem; border-radius: 20px; margin-right: 0.4rem; margin-bottom: 0.5rem; letter-spacing: 0.02em; transition: border-color 0.2s, color 0.2s; }
.hero-badge:hover { border-color: var(--teal); color: var(--teal); }
.hero-ctas { margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap; }
.cta-primary { display: inline-block; background: var(--teal); color: var(--navy); font-size: 0.85rem; font-weight: 700; padding: 0.8rem 2rem; border-radius: 4px; text-decoration: none; letter-spacing: 0.04em; transition: background 0.2s; }
.cta-primary:hover { background: var(--teal-dark); }
.cta-outline { display: inline-block; background: transparent; color: var(--white); font-size: 0.85rem; font-weight: 500; padding: 0.78rem 2rem; border-radius: 4px; border: 1px solid #2D4A6A; text-decoration: none; letter-spacing: 0.04em; transition: border-color 0.2s; }
.cta-outline:hover { border-color: var(--teal); color: var(--teal); }

/* ── STATS STRIP ── */
.stats-strip { background: var(--navy); padding: 0 80px 60px; }
.stats-grid { display: flex; gap: 0; border-top: 1px solid #1E3A5F; }
.stat-card { flex: 1; padding: 2rem 2rem 1.5rem; border-right: 1px solid #1E3A5F; }
.stat-card:last-child { border-right: none; }
.stat-num { font-size: 2.6rem; font-weight: 900; color: var(--teal); letter-spacing: -0.03em; line-height: 1; }
.stat-label { font-size: 0.68rem; font-weight: 500; color: #64748B; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 0.4rem; }

/* ── VALUE PROPS ── */
.pillars { background: var(--teal-bg); padding: 50px 80px; display: flex; gap: 2rem; }
.pillar { flex: 1; background: var(--white); border-radius: 8px; padding: 2rem; border-left: 3px solid var(--teal); }
.pillar-icon { font-size: 1.5rem; margin-bottom: 0.8rem; }
.pillar-title { font-size: 0.82rem; font-weight: 700; color: var(--ink); letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 0.5rem; }
.pillar-body { font-size: 0.85rem; color: var(--gray); line-height: 1.65; font-weight: 300; }

/* ── SECTIONS ── */
.section  { padding: 70px 80px; background: var(--white); }
.section-alt { padding: 70px 80px; background: var(--light); }
.eyebrow { font-size: 0.66rem; font-weight: 700; letter-spacing: 0.22em; text-transform: uppercase; color: var(--teal); margin-bottom: 0.4rem; }
.section-title { font-size: 2rem; font-weight: 800; color: var(--ink); margin-bottom: 2.5rem; letter-spacing: -0.02em; }
.about-text { font-size: 1.02rem; font-weight: 300; color: #374151; line-height: 1.95; max-width: 740px; }
.about-text b, .about-highlight { font-weight: 700; color: var(--ink); }

/* ── SKILLS ── */
.skill-group-title { font-size: 0.66rem; font-weight: 700; letter-spacing: 0.2em; text-transform: uppercase; color: var(--teal); margin-bottom: 0.9rem; }
.skill-pill { display: inline-block; background: var(--navy); color: var(--white); font-size: 0.78rem; font-weight: 500; padding: 0.38rem 1rem; border-radius: 4px; margin-right: 0.5rem; margin-bottom: 0.5rem; }
.skill-pill-light { display: inline-block; background: var(--white); color: var(--ink); font-size: 0.78rem; font-weight: 500; padding: 0.38rem 1rem; border-radius: 4px; margin-right: 0.5rem; margin-bottom: 0.5rem; border: 1px solid var(--border); }
.skill-col { padding: 0 40px 40px; background: var(--light); }
.skill-col-full { padding: 0 80px 50px; background: var(--light); }

/* ── EXPERIENCE ── */
.exp-item { padding: 0 80px; margin-bottom: 2.8rem; }
.exp-co { font-size: 1.05rem; font-weight: 800; color: var(--ink); letter-spacing: -0.01em; }
.exp-role { font-size: 0.95rem; color: var(--teal); font-weight: 600; margin-top: 0.15rem; }
.exp-period { font-size: 0.68rem; color: #9CA3AF; letter-spacing: 0.08em; text-transform: uppercase; margin: 0.35rem 0 0.8rem; }
.exp-desc { font-size: 0.88rem; color: #4B5563; font-weight: 300; line-height: 1.85; }
.exp-border { border-left: 3px solid var(--teal); padding-left: 1.5rem; }
.exp-sub { margin-top: 1.2rem; padding-top: 1rem; border-top: 1px dashed var(--border); }
.exp-sub-role { font-size: 0.8rem; font-weight: 600; color: var(--gray); }
.exp-sub-period { font-size: 0.67rem; color: #9CA3AF; letter-spacing: 0.06em; text-transform: uppercase; margin: 0.15rem 0 0.45rem; }
.exp-sub-desc { font-size: 0.8rem; color: #9CA3AF; font-weight: 300; line-height: 1.7; }

/* ── PROJECTS ── */
.proj-col { padding: 0 20px 60px; background: var(--light); }
.project-card { background: var(--white); border: 1px solid var(--border); border-radius: 8px; padding: 1.8rem; height: 100%; transition: border-color 0.2s, box-shadow 0.2s; }
.project-card:hover { border-color: var(--teal); box-shadow: 0 4px 20px rgba(46,196,182,0.1); }
.proj-tag { font-size: 0.64rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: var(--teal); margin-bottom: 0.5rem; }
.proj-name { font-size: 1.05rem; font-weight: 700; color: var(--ink); margin-bottom: 0.9rem; }
.case-label { font-size: 0.62rem; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase; color: #9CA3AF; margin-bottom: 0.35rem; margin-top: 0.6rem; }
.proj-desc { font-size: 0.83rem; color: var(--gray); font-weight: 300; line-height: 1.7; }
.case-result { font-size: 0.82rem; font-weight: 700; color: var(--teal-dark); margin-top: 1rem; padding-top: 0.8rem; border-top: 2px solid var(--teal-bg); }
.proj-link { display: inline-block; margin-top: 1rem; font-size: 0.76rem; font-weight: 600; color: var(--teal); letter-spacing: 0.04em; text-decoration: none; border-bottom: 1px solid var(--teal); padding-bottom: 1px; }
.proj-link:hover { color: var(--teal-dark); border-color: var(--teal-dark); }

/* ── CONTACT ── */
.contact-line { font-size: 1rem; font-weight: 300; color: #374151; margin-bottom: 0.9rem; }
.contact-link { font-weight: 600; color: var(--teal); text-decoration: none; }
.contact-link:hover { color: var(--teal-dark); }

/* ── FOOTER ── */
.footer-bar { background: var(--navy); border-top: 3px solid var(--teal); color: #475569; text-align: center; font-size: 0.7rem; font-weight: 400; letter-spacing: 0.12em; padding: 1.5rem; }

#MainMenu, footer, header { visibility: hidden; }
[data-testid="stSidebar"] { display: none; }
div[data-testid="stHorizontalBlock"] { gap: 0 !important; }

/* ── MOBILE ── */
@media (max-width: 768px) {
    .topbar { padding: 8px 20px !important; }
    .hero { padding: 50px 20px 40px !important; }
    .hero-inner { flex-direction: column !important; }
    .hero-photo-wrap { display: none !important; }
    .hero-name { font-size: 2.1rem !important; }
    .hero-title { font-size: 0.92rem !important; max-width: 100% !important; }
    .hero-badge { font-size: 0.68rem !important; }
    .hero-ctas { gap: 0.6rem !important; margin-top: 1.5rem !important; }
    .cta-primary, .cta-outline { font-size: 0.78rem !important; padding: 0.65rem 1.3rem !important; }
    .stats-strip { padding: 0 20px 40px !important; }
    .stats-grid { flex-wrap: wrap !important; }
    .stat-card { flex: 1 1 45% !important; border-right: none !important; border-bottom: 1px solid #1E3A5F; }
    .stat-num { font-size: 1.8rem !important; }
    .pillars { flex-direction: column !important; padding: 40px 20px !important; }
    .section { padding: 40px 20px !important; }
    .section-alt { padding: 40px 20px !important; }
    .section-title { font-size: 1.45rem !important; margin-bottom: 1.5rem !important; }
    .about-text { font-size: 0.93rem !important; }
    .skill-col { padding: 0 20px 25px !important; }
    .skill-col-full { padding: 0 20px 30px !important; }
    .exp-item { padding: 0 20px !important; }
    .proj-col { padding: 0 20px 30px !important; }
    .project-card { padding: 1.4rem !important; }
    div[data-testid="stHorizontalBlock"] { flex-wrap: wrap !important; }
    div[data-testid="stHorizontalBlock"] > div { width: 100% !important; min-width: 100% !important; flex: 1 1 100% !important; }
}
</style>
""", unsafe_allow_html=True)

# ── Language toggle ─────────────────────────────
st.markdown('<div class="topbar">', unsafe_allow_html=True)
_, col_btn = st.columns([20, 1])
with col_btn:
    label = "🇺🇸 EN" if st.session_state.lang == "PT" else "🇧🇷 PT"
    if st.button(label, key="lang_toggle"):
        st.session_state.lang = "EN" if st.session_state.lang == "PT" else "PT"
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

lang = st.session_state.lang

# ── Bilingual content ───────────────────────────
T = {
    "hero_eyebrow":  {"PT": "Portfólio Profissional",           "EN": "Professional Portfolio"},
    "hero_subtitle": {
        "PT": "Coordenadora Comercial que entregou <strong style='color:#2EC4B6'>+21% de crescimento em 2025</strong> — combinando liderança de equipes, Power BI e Inteligência Artificial para gerar resultados mensuráveis no mercado PET.",
        "EN": "Sales Manager who delivered <strong style='color:#2EC4B6'>+21% revenue growth in 2025</strong> — combining team leadership, Power BI and AI to drive measurable results in the pet distribution industry.",
    },
    "stat1":         {"PT": "Crescimento de Receita · 2025",    "EN": "Revenue Growth · 2025"},
    "stat2":         {"PT": "Profissionais Liderados",          "EN": "Professionals Led"},
    "stat3":         {"PT": "Laboratórios Parceiros",           "EN": "Partner Lab Brands"},
    "stat4":         {"PT": "Anos no Mercado PET",              "EN": "Years in Pet Industry"},
    "pillar1_title": {"PT": "Resultados Comerciais",            "EN": "Commercial Results"},
    "pillar1_body":  {"PT": "+21% de crescimento em 2025, expansão de PDVs ativos e gestão de 11 laboratórios nacionais e multinacionais.",
                      "EN": "+21% revenue growth in 2025, active POS expansion and management of 11 national and multinational lab brands."},
    "pillar2_title": {"PT": "Dados & Tecnologia",               "EN": "Data & Technology"},
    "pillar2_body":  {"PT": "Dashboards em Power BI para decisões em tempo real. IA com Claude para automação de relatórios e análises estratégicas.",
                      "EN": "Power BI dashboards for real-time decision-making. AI (Claude) for automated reporting and strategic analysis."},
    "pillar3_title": {"PT": "Liderança & Desenvolvimento",      "EN": "Leadership & Development"},
    "pillar3_body":  {"PT": "Equipe de 14 profissionais. Manuais técnicos de treinamento e acompanhamento a campo para acelerar o desenvolvimento individual.",
                      "EN": "14-person team. Technical training manuals and structured field coaching to accelerate individual development."},
    "about_label":   {"PT": "Sobre",                            "EN": "About"},
    "about_title":   {"PT": "Onde ciência veterinária<br>encontra estratégia comercial.", "EN": "Where veterinary science<br>meets commercial strategy."},
    "about_body":    {
        "PT": '<b>+21% de crescimento no faturamento em 2025.</b> Esse é o resultado mais recente de uma trajetória construída na interseção entre ciência veterinária, estratégia comercial e tecnologia.<br><br>Sou <b>médica veterinária formada pela UFMT</b> com 8 anos no mercado PET. Na <b>SOMAPET</b> — uma das principais distribuidoras PET de Cuiabá — lidero 14 profissionais e coordeno a relação estratégica com 11 laboratórios nacionais e multinacionais. Meu diferencial está em transformar dados em decisões: construí dashboards em Power BI que entregam visibilidade de performance em tempo real, e aplico IA com Claude para automatizar relatórios e afiar o foco estratégico da gestão.<br><br>Também desenvolvo <b>manuais técnicos de treinamento</b> e conduzo acompanhamento a campo — padronizando o onboarding de novos vendedores e promotores. Tenho pós-graduação em Gestão de Pessoas e acredito que <b>equipes de alta performance nascem da combinação entre profundidade técnica, inteligência de dados e investimento genuíno em pessoas.</b>',
        "EN": '<b>+21% revenue growth in 2025.</b> That is the most recent result of a career built at the intersection of veterinary science, commercial strategy and technology.<br><br>I am a <b>Doctor of Veterinary Medicine (UFMT)</b> with 8 years in the pet distribution industry. At <b>SOMAPET</b> — one of Cuiabá\'s leading pet distributors — I lead 14 professionals and manage strategic relationships across 11 national and multinational lab partners. My differentiator: I turn data into decisions — building real-time Power BI dashboards and deploying AI automation (Claude) that eliminate manual work and sharpen every strategic call my team makes.<br><br>I also author <b>technical training manuals</b> and lead structured field coaching to standardize onboarding and accelerate rep development. I hold a Graduate Certificate in People Management and believe that <b>elite commercial teams are built at the intersection of technical depth, data fluency and genuine investment in people.</b>',
    },
    "skills_label":   {"PT": "Competências",                    "EN": "Competencies"},
    "skills_title":   {"PT": "Ferramentas & habilidades.",      "EN": "Tools & expertise."},
    "sg_data":        {"PT": "Dados & Tecnologia",              "EN": "Data & Technology"},
    "sg_commercial":  {"PT": "Gestão Comercial",                "EN": "Sales & Commercial"},
    "sg_soft":        {"PT": "Liderança",                       "EN": "Leadership"},
    "sg_courses":     {"PT": "Formação & Certificações",        "EN": "Education & Certifications"},
    "skill_lead":     {"PT": "Liderança de Equipes",            "EN": "Team Leadership"},
    "skill_goals":    {"PT": "Gestão de Metas & KPIs",          "EN": "KPI & Target Management"},
    "skill_channel":  {"PT": "Channel Sales",                   "EN": "Channel Sales"},
    "skill_dist":     {"PT": "Gestão de Distribuidoras",        "EN": "Distributor Management"},
    "skill_portfolio":{"PT": "Gestão de Carteira",              "EN": "Account Management"},
    "skill_comm":     {"PT": "Comunicação Assertiva",           "EN": "Assertive Communication"},
    "skill_people":   {"PT": "Desenvolvimento de Pessoas",      "EN": "People Development"},
    "skill_coaching": {"PT": "Field Coaching",                  "EN": "Field Coaching"},
    "skill_train":    {"PT": "Treinamento de Equipes",          "EN": "Sales Team Training"},
    "skill_vision":   {"PT": "Visão Estratégica",               "EN": "Strategic Thinking"},
    "course1":        {"PT": "Pós-graduação em Gestão de Pessoas — Fac. Metropolitana",
                       "EN": "Graduate Certificate in People Management — Fac. Metropolitana"},
    "course2":        {"PT": "Medicina Veterinária — UFMT",     "EN": "Doctor of Veterinary Medicine — UFMT"},
    "course3":        {"PT": "Power BI do Básico ao Avançado",  "EN": "Power BI — Fundamentals to Advanced"},
    "course4":        {"PT": "Python para Análise de Dados",    "EN": "Python for Data Analysis"},
    "course5":        {"PT": "Inteligência Artificial Aplicada","EN": "Applied AI & Automation"},
    "course6":        {"PT": "Comunicação Assertiva — Fac. Líbano", "EN": "Assertive Communication — Fac. Líbano"},
    "exp_label":      {"PT": "Trajetória",                      "EN": "Experience"},
    "exp_title":      {"PT": "Experiência profissional.",       "EN": "Professional background."},
    "proj_label":     {"PT": "Projetos",                        "EN": "Projects"},
    "proj_title":     {"PT": "O que já construí.",              "EN": "Selected work."},
    "proj1_link":     {"PT": "Ver projeto →",                   "EN": "View project →"},
    "proj4_link":     {"PT": "Solicitar material →",            "EN": "Request material →"},
    "contact_label":  {"PT": "Contato",                         "EN": "Contact"},
    "open_to":        {"PT": "🟢 Aberta a Oportunidades · Disponível para entrevistas",
                       "EN": "🟢 Open to Opportunities · Available for interviews"},
    "contact_title":  {"PT": "Vamos conversar?",                "EN": "Let's connect."},
    "contact_loc":    {"PT": "Cuiabá, Mato Grosso — Brasil",   "EN": "Cuiabá, Mato Grosso — Brazil"},
    "footer":         {"PT": "GABRIELA BARROS MICHELOTTO &nbsp;·&nbsp; Cuiabá, MT &nbsp;·&nbsp; 2026",
                       "EN": "GABRIELA BARROS MICHELOTTO &nbsp;·&nbsp; Cuiabá, MT &nbsp;·&nbsp; 2026"},
    "cta_primary":    {"PT": "Falar Comigo",                    "EN": "Get in Touch"},
    "cta_secondary":  {"PT": "Ver LinkedIn",                    "EN": "View LinkedIn"},
    "case_ch":        {"PT": "Desafio",                         "EN": "Challenge"},
    "case_ac":        {"PT": "O que fiz",                       "EN": "What I did"},
    "case_re":        {"PT": "✦ Resultado",                     "EN": "✦ Result"},
    "p1_name":        {"PT": "Agente IA Pessoal",               "EN": "Personal AI Agent"},
    "p1_ch":          {"PT": "Criar uma presença digital de IA sem experiência prévia em programação.",
                       "EN": "Build a production-ready AI showcase with zero prior programming experience."},
    "p1_ac":          {"PT": "Aprendi Python do zero e desenvolvi um assistente conversacional completo integrado ao Google Gemini.",
                       "EN": "Learned Python from scratch and built a fully deployed conversational assistant powered by Google Gemini."},
    "p1_re":          {"PT": "App funcional publicado e no ar — acessível publicamente pelo portfólio.",
                       "EN": "Live, publicly accessible app — deployable as a portfolio asset for any professional."},
    "p2_name":        {"PT": "Dashboard Comercial em Power BI", "EN": "Commercial Power BI Dashboard"},
    "p2_ch":          {"PT": "Equipe de 14 profissionais sem visibilidade de performance em tempo real por vendedor, laboratório ou região.",
                       "EN": "14-person team with no real-time visibility into performance by rep, brand or territory."},
    "p2_ac":          {"PT": "Construí dashboards em Power BI com indicadores individuais, por laboratório e por região — integrado à rotina semanal de gestão.",
                       "EN": "Built Power BI dashboards tracking individual KPIs by rep, lab brand and territory — embedded into weekly management routines."},
    "p2_re":          {"PT": "Decisões orientadas por dados com impacto direto no crescimento de 21% em 2025.",
                       "EN": "Data-driven decisions directly contributing to 21% revenue growth in 2025."},
    "p3_name":        {"PT": "Automação de Relatórios com IA",  "EN": "AI-Powered Report Automation"},
    "p3_ch":          {"PT": "Relatórios manuais consumindo horas da liderança toda semana.",
                       "EN": "Manual reporting consuming hours of leadership time every week."},
    "p3_ac":          {"PT": "Automatizei a geração de relatórios HTML a partir de planilhas Excel usando Python.",
                       "EN": "Automated HTML report generation from Excel data sources using Python."},
    "p3_re":          {"PT": "Trabalho manual reduzido — relatórios estratégicos gerados em segundos.",
                       "EN": "Manual work eliminated — strategic reports now generated in seconds."},
    "p4_name":        {"PT": "Manual de Vendas para Iniciantes", "EN": "Sales Onboarding Manual"},
    "p4_tag":         {"PT": "Treinamento · RH · Field Operations", "EN": "Training · HR · Field Operations"},
    "p4_ch":          {"PT": "Alta rotatividade e curva longa de aprendizado para novos vendedores e promotores técnicos.",
                       "EN": "High turnover and long ramp-up time for new sales reps and technical promoters."},
    "p4_ac":          {"PT": "Desenvolvi manual técnico completo com rotas de campo, técnicas de abordagem, conhecimento de produto e gestão de carteira — em parceria com o RH.",
                       "EN": "Authored a complete technical manual covering field routes, sales methodology, product knowledge and account management — developed in partnership with HR."},
    "p4_re":          {"PT": "Onboarding mais rápido e padronizado, reduzindo dependência de treinamento individual ad hoc.",
                       "EN": "Faster, standardized onboarding — reducing dependence on ad hoc one-on-one training."},
}

def t(k): return T[k][lang]

# ── Experience data ─────────────────────────────
EXP = {
    "PT": [
        {
            "co": "SOMAPET",
            "role": "Coordenadora Comercial",
            "period": "ABRIL 2024 — PRESENTE · CUIABÁ, MT",
            "desc": "Liderou equipe de 14 profissionais (8 consultores de vendas + 6 promotores técnicos), entregando crescimento de 21% no faturamento em 2025. Gestão estratégica de 11 laboratórios parceiros nacionais e multinacionais — coordenando campanhas, channel sales, positivação de clientes e expansão de PDVs ativos. Implementou dashboards em Power BI para monitoramento de performance em tempo real e automatizou relatórios estratégicos com IA (Claude), eliminando trabalho manual da gestão. Criou manual técnico de vendas para padronizar o onboarding de novos profissionais e conduziu acompanhamento a campo para desenvolvimento individual da equipe.",
            "sub_role": "Promotora Técnica · Virbac",
            "sub_period": "MAIO 2023 — ABRIL 2024",
            "sub_desc": "Promotoria técnica e comercial do laboratório Virbac em MT. Acompanhamento da equipe comercial na rotina de campo, gestão de channel sales junto à gerência, treinamentos sobre suplementos e medicamentos da linha Pet e organização de eventos do setor.",
        },
        {
            "co": "ORGANNACT",
            "role": "Coordenadora Regional — MT/MS",
            "period": "AGOSTO 2019 — NOVEMBRO 2022 · MT/MS",
            "desc": "Dirigiu as operações comerciais em dois estados (MT e MS), gerenciando equipes junto às distribuidoras responsáveis. Forneceu suporte técnico a consultores e promotores do laboratório. Conduziu treinamentos e visitas técnicas a médicos veterinários para apresentação de novos produtos. Desenvolveu carteira de clientes e liderou o ciclo completo de campanhas mensais — da elaboração ao fechamento.",
        },
        {
            "co": "MC AGRO",
            "role": "Promotora Técnica",
            "period": "JANEIRO 2018 — JULHO 2019 · CUIABÁ, MT",
            "desc": "Representação técnica e comercial dos laboratórios Organnact, Syntec e Dechra em todo o estado do MT. Acompanhamento de equipes de campo da distribuidora, gestão de channel sales junto à gerência e treinamentos sobre suplementos e medicamentos da linha Pet. Organização e participação em eventos do setor com apresentação de produtos.",
        },
    ],
    "EN": [
        {
            "co": "SOMAPET",
            "role": "Sales Manager",
            "period": "APRIL 2024 — PRESENT · CUIABÁ, MT",
            "desc": "Delivered 21% revenue growth in 2025 while leading a 14-person team (8 sales consultants + 6 technical reps). Managed commercial and technical relationships across 11 national and multinational lab brands — overseeing channel sales strategy, monthly campaigns, client activation and active POS expansion. Built real-time Power BI dashboards and deployed AI automation (Claude) to eliminate manual reporting and sharpen strategic decision-making. Authored a Technical Sales Manual to standardize onboarding and conducted field coaching to accelerate individual rep development.",
            "sub_role": "Technical Sales Representative · Virbac",
            "sub_period": "MAY 2023 — APRIL 2024",
            "sub_desc": "Drove technical and commercial channel sales for Virbac across MT. Embedded with distributor field teams for daily sales support, managed channel sales performance with distributor leadership, delivered product training on pet supplements and medications, and organized industry events.",
        },
        {
            "co": "ORGANNACT",
            "role": "Regional Sales Coordinator — MT/MS",
            "period": "AUGUST 2019 — NOVEMBER 2022 · MT/MS",
            "desc": "Directed distributor channel operations across two states (Mato Grosso and Mato Grosso do Sul). Built and coached sales teams embedded in regional distribution networks. Delivered veterinary technical training, drove regional account portfolio growth and owned the full campaign cycle — from design through execution and monthly close.",
        },
        {
            "co": "MC AGRO",
            "role": "Technical Sales Representative",
            "period": "JANUARY 2018 — JULY 2019 · CUIABÁ, MT",
            "desc": "Drove technical and commercial channel sales for three lab brands (Organnact, Syntec and Dechra) across Mato Grosso state. Supported distributor field teams in daily sales execution, managed channel sales KPIs in partnership with distributor leadership, and delivered product training on pet supplements and medications. Organized and participated in industry trade events and product launch activations.",
        },
    ],
}

# ════════════════════════════════════════════════
# HERO
# ════════════════════════════════════════════════
_foto_html = f'<img src="data:image/jpeg;base64,{_foto}" style="width:270px;height:330px;object-fit:cover;object-position:top;border-radius:6px;display:block;border:3px solid #1E3A5F;">' if _foto else ""

badges_pt = ["Power BI", "Inteligência Artificial", "Python", "Excel", "Channel Sales", "Medicina Veterinária", "Gestão de Pessoas"]
badges_en = ["Power BI", "Artificial Intelligence", "Python", "Excel", "Channel Sales", "Veterinary Medicine", "People Management"]
badges = badges_pt if lang == "PT" else badges_en
badges_html = "".join(f'<span class="hero-badge">{b}</span>' for b in badges)

st.markdown(f"""
<div style="background:#1DA89E;padding:10px 80px;text-align:center;">
<span style="color:#0D1B2A;font-size:0.78rem;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;">{t("open_to")}</span>
</div>
<div class="hero">
<div class="hero-inner">
<div class="hero-text">
<p class="hero-eyebrow">{t("hero_eyebrow")}</p>
<h1 class="hero-name">Gabriela Barros<br>Michelotto</h1>
<p class="hero-title">{t("hero_subtitle")}</p>
<div>{badges_html}</div>
<div class="hero-ctas">
<a class="cta-primary" href="mailto:gabrielamichelotto@gmail.com">{t("cta_primary")}</a>
<a class="cta-outline" href="https://www.linkedin.com/in/gabriela-michelotto/" target="_blank">{t("cta_secondary")}</a>
</div>
</div>
<div class="hero-photo-wrap">{_foto_html}</div>
</div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# STATS STRIP
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="stats-strip">
<div class="stats-grid">
<div class="stat-card"><div class="stat-num">+21%</div><div class="stat-label">{t("stat1")}</div></div>
<div class="stat-card"><div class="stat-num">14</div><div class="stat-label">{t("stat2")}</div></div>
<div class="stat-card"><div class="stat-num">11</div><div class="stat-label">{t("stat3")}</div></div>
<div class="stat-card"><div class="stat-num">8</div><div class="stat-label">{t("stat4")}</div></div>
</div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# VALUE PILLARS
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="pillars">
<div class="pillar"><div class="pillar-icon">🎯</div><div class="pillar-title">{t("pillar1_title")}</div><div class="pillar-body">{t("pillar1_body")}</div></div>
<div class="pillar"><div class="pillar-icon">📊</div><div class="pillar-title">{t("pillar2_title")}</div><div class="pillar-body">{t("pillar2_body")}</div></div>
<div class="pillar"><div class="pillar-icon">👥</div><div class="pillar-title">{t("pillar3_title")}</div><div class="pillar-body">{t("pillar3_body")}</div></div>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# ABOUT
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section">
<p class="eyebrow">{t("about_label")}</p>
<h2 class="section-title">{t("about_title")}</h2>
<p class="about-text">{t("about_body")}</p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# SKILLS
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section-alt">
<p class="eyebrow">{t("skills_label")}</p>
<h2 class="section-title">{t("skills_title")}</h2>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""<div class="skill-col"><p class="skill-group-title">{t("sg_data")}</p><span class="skill-pill">Power BI</span><span class="skill-pill">Python</span><span class="skill-pill">Excel</span><span class="skill-pill">Claude AI</span><span class="skill-pill">Dashboards</span><span class="skill-pill">Automação</span></div>""", unsafe_allow_html=True)
with col2:
    st.markdown(f"""<div class="skill-col"><p class="skill-group-title">{t("sg_commercial")}</p><span class="skill-pill-light">{t("skill_lead")}</span><span class="skill-pill-light">{t("skill_goals")}</span><span class="skill-pill-light">{t("skill_channel")}</span><span class="skill-pill-light">{t("skill_dist")}</span><span class="skill-pill-light">{t("skill_portfolio")}</span></div>""", unsafe_allow_html=True)
with col3:
    st.markdown(f"""<div class="skill-col"><p class="skill-group-title">{t("sg_soft")}</p><span class="skill-pill-light">{t("skill_comm")}</span><span class="skill-pill-light">{t("skill_people")}</span><span class="skill-pill-light">{t("skill_coaching")}</span><span class="skill-pill-light">{t("skill_train")}</span><span class="skill-pill-light">{t("skill_vision")}</span></div>""", unsafe_allow_html=True)

st.markdown(f"""<div class="skill-col-full"><p class="skill-group-title">{t("sg_courses")}</p><span class="skill-pill-light">{t("course1")}</span><span class="skill-pill-light">{t("course2")}</span><span class="skill-pill-light">{t("course3")}</span><span class="skill-pill-light">{t("course4")}</span><span class="skill-pill-light">{t("course5")}</span><span class="skill-pill-light">{t("course6")}</span></div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# EXPERIENCE
# ════════════════════════════════════════════════
st.markdown(f"""<div class="section"><p class="eyebrow">{t("exp_label")}</p><h2 class="section-title">{t("exp_title")}</h2></div>""", unsafe_allow_html=True)

exp_html = ""
for exp in EXP[lang]:
    sub = ""
    if exp.get("sub_role"):
        sub = (
            '<div class="exp-sub">'
            f'<div class="exp-sub-role">{exp["sub_role"]}</div>'
            f'<div class="exp-sub-period">{exp["sub_period"]}</div>'
            f'<div class="exp-sub-desc">{exp["sub_desc"]}</div>'
            '</div>'
        )
    exp_html += (
        '<div class="exp-item">'
        '<div class="exp-border">'
        f'<div class="exp-co">{exp["co"]}</div>'
        f'<div class="exp-role">{exp["role"]}</div>'
        f'<div class="exp-period">{exp["period"]}</div>'
        f'<div class="exp-desc">{exp["desc"]}</div>'
        f'{sub}'
        '</div></div>'
    )

st.markdown(exp_html, unsafe_allow_html=True)

# ════════════════════════════════════════════════
# PROJECTS
# ════════════════════════════════════════════════
st.markdown(f"""<div class="section-alt"><p class="eyebrow">{t("proj_label")}</p><h2 class="section-title">{t("proj_title")}</h2></div>""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.markdown(f"""<div class="proj-col"><div class="project-card"><p class="proj-tag">Python · Streamlit · AI</p><p class="proj-name">{t("p1_name")}</p><p class="case-label">{t("case_ch")}</p><p class="proj-desc">{t("p1_ch")}</p><p class="case-label">{t("case_ac")}</p><p class="proj-desc">{t("p1_ac")}</p><p class="case-result">{t("case_re")} — {t("p1_re")}</p><a class="proj-link" href="https://github.com/gabrielamichelotto-byte/agente-gabriela" target="_blank">{t("proj1_link")}</a></div></div>""", unsafe_allow_html=True)
with c2:
    st.markdown(f"""<div class="proj-col"><div class="project-card"><p class="proj-tag">Power BI · Data Strategy</p><p class="proj-name">{t("p2_name")}</p><p class="case-label">{t("case_ch")}</p><p class="proj-desc">{t("p2_ch")}</p><p class="case-label">{t("case_ac")}</p><p class="proj-desc">{t("p2_ac")}</p><p class="case-result">{t("case_re")} — {t("p2_re")}</p></div></div>""", unsafe_allow_html=True)
with c3:
    st.markdown(f"""<div class="proj-col"><div class="project-card"><p class="proj-tag">Python · Excel · Automation</p><p class="proj-name">{t("p3_name")}</p><p class="case-label">{t("case_ch")}</p><p class="proj-desc">{t("p3_ch")}</p><p class="case-label">{t("case_ac")}</p><p class="proj-desc">{t("p3_ac")}</p><p class="case-result">{t("case_re")} — {t("p3_re")}</p></div></div>""", unsafe_allow_html=True)

c4, _, _ = st.columns(3)
with c4:
    st.markdown(f"""<div class="proj-col"><div class="project-card"><p class="proj-tag">{t("p4_tag")}</p><p class="proj-name">{t("p4_name")}</p><p class="case-label">{t("case_ch")}</p><p class="proj-desc">{t("p4_ch")}</p><p class="case-label">{t("case_ac")}</p><p class="proj-desc">{t("p4_ac")}</p><p class="case-result">{t("case_re")} — {t("p4_re")}</p><a class="proj-link" href="mailto:gabrielamichelotto@gmail.com">{t("proj4_link")}</a></div></div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════
# CONTACT
# ════════════════════════════════════════════════
st.markdown(f"""
<div class="section">
<p class="eyebrow">{t("contact_label")}</p>
<h2 class="section-title">{t("contact_title")}</h2>
<p class="contact-line">📧 <a class="contact-link" href="mailto:gabrielamichelotto@gmail.com">gabrielamichelotto@gmail.com</a></p>
<p class="contact-line">💼 <a class="contact-link" href="https://www.linkedin.com/in/gabriela-michelotto/" target="_blank">linkedin.com/in/gabriela-michelotto</a></p>
<p class="contact-line">📍 {t("contact_loc")}</p>
</div>
<div class="footer-bar">{t("footer")}</div>
""", unsafe_allow_html=True)
