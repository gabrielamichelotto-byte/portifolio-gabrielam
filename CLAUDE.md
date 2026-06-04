# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Single-file Streamlit portfolio for Gabriela Barros Michelotto, deployed at https://portifolio-gabrielamichelotto.streamlit.app/. All application logic, content, and styling lives in `app.py`.

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
```

The app runs on port 8501. No build step, no test suite.

## Architecture

`app.py` is the entire application (~809 lines). It is organized in this order:

1. **Page config** — `st.set_page_config(layout="wide")`
2. **Session state** — `st.session_state.lang` holds `"PT"` or `"EN"`
3. **Asset loading** — profile photo and project screenshots loaded via `base64` with fallback paths
4. **CSS injection** — one large `st.markdown("""<style>...</style>""", unsafe_allow_html=True)` block that overrides Streamlit's native styling
5. **Translation dictionary** — `T` dict with nested `"PT"` / `"EN"` keys for all UI strings
6. **`t(key)` helper** — looks up `T[key][st.session_state.lang]`
7. **Content data** — `experiencias` dict (work history) and skill lists, each with PT/EN variants
8. **Section rendering** — sequential `st.markdown(...)` calls building: topbar → hero → value pillars → about → skills → experience → cases → contact → footer

## Bilingual System

All user-visible text must be added to the `T` dictionary with both `"PT"` and `"EN"` keys, then referenced via `t("key")`. Hardcoded strings not in `T` will only appear in one language.

## Styling Conventions

- No external CSS files — all styles are in the single `<style>` block inside `app.py`
- Color palette: gold `#c9a96e`, dark `#0a0a0a`/`#050505`, cream `#f7f3ee`, mid `#ede8e0`
- Font: Inter (loaded from Google Fonts in the style block)
- Mobile breakpoint: `768px` via `@media` queries
- Streamlit's own header, footer, and sidebar are hidden via CSS targeting `[data-testid]` selectors

## Images

Images are embedded as base64 strings directly in `app.py`. To update or add an image:
1. Place the image file in the repo root
2. Load it with `base64.b64encode(open("filename.ext", "rb").read()).decode()`
3. Use as `data:image/...;base64,{encoded}` in an `<img>` tag inside `st.markdown(..., unsafe_allow_html=True)`

## Deployment & Keep-Alive

Deployed to Streamlit Cloud. `.github/workflows/keep_alive.yml` pings the live URL every 6 days (cron `0 9 */6 * *`) to prevent the app from sleeping due to inactivity.

## Dev Container

`.devcontainer/devcontainer.json` configures a Python 3.11 environment that auto-starts the Streamlit server on attach. This matches the production runtime.
