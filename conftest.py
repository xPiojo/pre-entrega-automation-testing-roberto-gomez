import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import datetime
from utils.logger import logger
import pytest_html 

# Definir la ubicación para las capturas de pantalla
SCREENSHOTS_DIR = "reports/screenshots"

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
    Si falla, toma una captura de pantalla y la adjunta al reporte HTML.
    """
    outcome = yield
    report = outcome.get_result()
    
    # Inicializamos report.extra (necesario para agregar contenido al reporte HTML)
    report.extra = getattr(report, "extra", [])

    if report.failed:
        # Intentamos obtener el driver del test que falló
        driver = item.funcargs.get("driver")
        if driver:
            # CAMBIO 2: Crear el directorio anidado (reports/screenshots)
            os.makedirs(SCREENSHOTS_DIR, exist_ok=True)
            
            # Nombre del archivo con fecha y hora
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            # Limpiamos el nombre del test para evitar caracteres raros
            test_name = item.name.replace("[", "_").replace("]", "_")
            
            # La ruta donde se guarda el archivo (Ruta absoluta desde la raíz del proyecto)
            screenshot_path_save = f"{SCREENSHOTS_DIR}/{test_name}_{timestamp}.png"
            
            # La ruta que verá el reporte HTML (Ruta RELATIVA desde reports/report.html)
            screenshot_path_link = f"screenshots/{test_name}_{timestamp}.png"

            driver.save_screenshot(screenshot_path_save)
            
            logger.error(f"❌ Test Fallido: {item.name}")
            # Logear la ruta real de guardado
            logger.info(f"📸 Captura de pantalla guardada en: {screenshot_path_save}")

            # --- Adjuntar enlace navegable usando HTML puro ---
            # Creamos un enlace HTML como string.
            # Usamos la ruta RELATIVA para el enlace
            html_link_str = f'<a href="{screenshot_path_link}">Ver Captura de Pantalla</a>'
            
            # Inyectamos el enlace HTML en la metadata del test que falló
            report.extra.append(pytest_html.extras.html(html_link_str))


# --- FIXTURE API (JSONPLACEHOLDER) ---
@pytest.fixture
def api_url():
    """
    Devuelve la URL base para las pruebas de API.
    """
    return "https://jsonplaceholder.typicode.com"