"""
conftest.py
----------------------------
Se ejecuta antes de cada test y configura el driver de Selenium.
También toma capturas automáticas cuando un test falla.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime


@pytest.fixture
def driver():
    """
    Crea el navegador Chrome en modo incógnito.
    Se ejecuta antes del test y se cierra al terminar.
    """
    options = Options()
    options.add_argument("--incognito")
    # Para modo sin ventana (si lo querés), descomentá la siguiente línea:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    yield driver  # --> entrega el driver al test

    driver.quit()  # --> se ejecuta después del test


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Si un test falla, guarda una captura en /reports.
    Muy útil para debugging.
    """
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports", exist_ok=True)

            # Timestamp para que no se repitan nombres
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            screenshot_path = f"reports/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Captura guardada en: {screenshot_path}")
