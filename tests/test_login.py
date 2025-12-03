import pytest
from pages.login_page import LoginPage
from utils.data_login_loader import load_login_data


@pytest.mark.parametrize("username,password,debe_funcionar", load_login_data("data/data_login.csv"))
def test_login(driver, username, password, debe_funcionar):
    """
    Test parametrizado para verificar el login en SauceDemo.

    Parámetros:
        username (str): Nombre de usuario a probar.
        password (str): Contraseña asociada al usuario.
        debe_funcionar (bool): Indica si el login debe ser exitoso.

    Comportamiento:
        - Si 'debe_funcionar' es True, el login NO debe mostrar mensaje de error.
        - Si 'debe_funcionar' es False, el login DEBE mostrar mensaje de error.

    Se utiliza el patrón Page Object (LoginPage) para encapsular la interacción.
    El fixture 'driver' provee la instancia del navegador.
    """

    login_page = LoginPage(driver)

    # 1. Abrir la página de login
    login_page.open()

    # 2. Realizar el intento de login con las credenciales
    login_page.login(username, password)

    # 3. Validar según el resultado esperado
    if debe_funcionar:
        assert not login_page.has_error(), "El login DEBERÍA funcionar, pero mostró error."
    else:
        assert login_page.has_error(), "El login DEBERÍA fallar, pero NO mostró error."
