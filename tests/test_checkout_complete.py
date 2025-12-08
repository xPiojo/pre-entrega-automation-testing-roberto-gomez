import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from utils.logger import logger

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_end_to_end_purchase(driver, username, password):
    """
    TEST E2E: Login -> Agregar -> Carrito -> Checkout -> Datos -> Finish -> Validar -> Back Home
    """
    logger.info("--- INICIO TEST E2E: Compra Completa ---")

    # 1. Login
    logger.info("STEP 1: Login...")
    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    # 2. Agregar al Carrito
    logger.info("STEP 2: Agregando producto...")
    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.open_cart()

    # 3. Proceder al Checkout desde el Carrito
    logger.info("STEP 3: Iniciando Checkout...")
    cart = CartPage(driver)
    cart.click_checkout()

    # 4. Completar Formulario (Checkout Page)
    logger.info("STEP 4: Completando formulario de envío...")
    checkout = CheckoutPage(driver)
    checkout.enter_user_information("Carlos", "Martinez", "1375")
    checkout.click_continue()

    # 5. Finalizar Compra
    logger.info("STEP 5: Confirmando orden...")
    checkout.click_finish()

    # 6. Validar Mensaje de Éxito
    logger.info("STEP 6: Validando compra exitosa...")
    mensaje = checkout.get_complete_message()
    assert "Thank you for your order!" in mensaje, "Error: No se recibió el mensaje de agradecimiento."
    logger.info("✅ Mensaje 'Thank you' verificado correctamente.")

    # 7. Volver al Inicio (Lo que pediste)
    logger.info("STEP 7: Volviendo al inicio...")
    checkout.click_back_home()

    # Validación final: ¿Estamos de vuelta en productos?
    assert "inventory.html" in driver.current_url, "Error: El botón Back Home no llevó al inventario."
    logger.info("✅ Ciclo completo cerrado: Estamos de vuelta en el inventario.")

    logger.info("--- TEST E2E FINALIZADO CON ÉXITO ---")