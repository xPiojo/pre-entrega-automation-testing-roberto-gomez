import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
from utils.logger import logger  # <--- Usamos nuestro logger

@pytest.fixture
def driver():
    """
    Fixture que inicializa el driver de Chrome.
    Se ejecuta antes (yield) y después (teardown) de cada test.
    """
    options = Options()
    options.add_argument("--incognito")
    #options.add_argument("--headless=new") # Descomentar para no ver el navegador

    driver = webdriver.Chrome(options=options)
    
    yield driver  # El test se ejecuta aquí

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook que escucha el resultado de cada test.
    Si falla, toma una captura de pantalla.
    """
    outcome = yield
    report = outcome.get_result()

    if report.failed:
        # Intentamos obtener el driver del test que falló
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports", exist_ok=True)
            
            # Nombre del archivo con fecha y hora
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            # Limpiamos el nombre del test para evitar caracteres raros
            test_name = item.name.replace("[", "_").replace("]", "_")
            screenshot_path = f"reports/{test_name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path)
            
            # Usamos logger en lugar de print para consistencia
            logger.error(f"❌ Test Fallido: {item.name}")
            logger.info(f"📸 Captura de pantalla guardada en: {screenshot_path}")

# --- FIXTURE API (JSONPLACEHOLDER) ---
@pytest.fixture
def api_url():
    """
    Devuelve la URL base para las pruebas de API.
    """
    return "https://jsonplaceholder.typicode.com"
