import pytest
from pages.login_page import LoginPage
from utils.data_login_loader import load_login_data

@pytest.mark.parametrize("username,password,debe_funcionar", load_login_data("data/data_login.csv"))
def test_login(driver, username, password, debe_funcionar):
    """
    Test parametrizado de login en SauceDemo.

    Este test utiliza datos desde un CSV (data_login.csv).
    Para cada caso:
    - Si 'debe_funcionar' es True, el login NO debe mostrar error.
    - Si 'debe_funcionar' es False, el login debe mostrar mensaje de error.

    La interacción está encapsulada en el Page Object LoginPage.
    El fixture 'driver' es provisto por conftest.py.
    """

    login_page = LoginPage(driver)

    # 1. Abrir la página
    login_page.open()

    # 2. Intentar login
    login_page.login(username, password)

    # 3. Validación
    if debe_funcionar:
        assert not login_page.has_error(), "El login DEBERÍA funcionar, pero mostró error."
    else:
        assert login_page.has_error(), "El login DEBERÍA fallar, pero NO mostró error."
