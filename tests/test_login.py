import pytest
from pages.login_page import LoginPage
from utils.data_login_loader import load_login_data
from utils.logger import logger  # <--- Faltaba importar el logger

@pytest.mark.parametrize("username,password,debe_funcionar", load_login_data("data/data_login.csv"))
def test_login(driver, username, password, debe_funcionar):
    """
    Test parametrizado para verificar el login en SauceDemo.
    """
    
    # Log de inicio diferenciado por usuario
    logger.info(f"--- INICIO TEST LOGIN: Usuario '{username}' ---")

    login_page = LoginPage(driver)

    # 1. Abrir la página
    logger.info("STEP 1: Abriendo página de login...")
    login_page.open()

    # 2. Realizar login
    logger.info(f"STEP 2: Intentando ingresar con credenciales: {username} / *****")
    login_page.login(username, password)

    # 3. Validar resultado
    logger.info("STEP 3: Verificando resultado esperado...")
    
    if debe_funcionar:
        es_exitoso = not login_page.has_error()
        assert es_exitoso, f"Error: El login con '{username}' debería funcionar, pero mostró error."
        logger.info(f"✅ Login exitoso confirmado para '{username}'.")
    else:
        tiene_error = login_page.has_error()
        assert tiene_error, f"Error: El login con '{username}' debería fallar, pero NO mostró error."
        logger.info(f"✅ Bloqueo correcto confirmado para '{username}' (Mensaje de error visible).")
    
    logger.info("--- FIN DE ITERACIÓN ---")