"""
Mantém o portfólio Streamlit acordado simulando uma visita real.

Abre o app num navegador headless (Chromium), renderiza a página de verdade
(estabelecendo a sessão WebSocket que o Streamlit usa pra contar tráfego) e,
se o app estiver dormindo, clica no botão "get this app back up" pra acordá-lo.
"""

import os
import sys
from playwright.sync_api import sync_playwright

APP_URL = os.environ.get(
    "APP_URL", "https://portifolio-gabrielamichelotto.streamlit.app/"
)

# Textos do botão que o Streamlit mostra quando o app está dormindo
WAKE_BUTTON_TEXTS = [
    "Yes, get this app back up!",
    "get this app back up",
    "Yes, get this app back up",
]


def main() -> int:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        )
        page = context.new_page()

        print(f"Abrindo {APP_URL} ...")
        page.goto(APP_URL, wait_until="domcontentloaded", timeout=60_000)

        # Espera inicial pra página assentar
        page.wait_for_timeout(5_000)

        # Se o app estiver dormindo, procura e clica no botão de acordar
        woke_up = False
        for text in WAKE_BUTTON_TEXTS:
            try:
                btn = page.get_by_text(text, exact=False)
                if btn.count() > 0 and btn.first.is_visible():
                    print(f"App estava dormindo. Clicando: '{text}'")
                    btn.first.click(timeout=10_000)
                    woke_up = True
                    break
            except Exception:
                continue

        if woke_up:
            # Espera o app subir de novo (pode levar ~1 min)
            print("Aguardando o app acordar...")
            page.wait_for_timeout(60_000)
        else:
            print("App já estava acordado.")
            # Permanece um pouco na página pra firmar a sessão como visita real
            page.wait_for_timeout(15_000)

        title = page.title()
        print(f"Título da página: {title}")
        print("Visita concluída com sucesso.")

        context.close()
        browser.close()

    return 0


if __name__ == "__main__":
    sys.exit(main())
