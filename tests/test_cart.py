import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from utils.logger import logger

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_checkout_flow(driver, username, password):
    """
    TEST A: Agregar item -> Verificar en Carrito -> Ir a Checkout
    """
    logger.info("--- INICIO TEST: Flujo de Checkout (End-to-End) ---")
    
    # 1. Login
    logger.info("STEP 1: Iniciando sesión...")
    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    # 2. Agregar producto desde Inventario
    logger.info("STEP 2: Agregando producto desde el inventario...")
    inventory = InventoryPage(driver)
    
    # Capturamos el nombre para compararlo luego
    nombre_producto_agregado = inventory.add_first_product_to_cart() 
    
    # Navegar al carrito
    inventory.open_cart()

    # 3. Validar en el Carrito
    logger.info("STEP 3: Verificando contenido del carrito...")
    cart = CartPage(driver)
    nombres_en_carrito = cart.get_cart_items_names()
    
    assert nombre_producto_agregado in nombres_en_carrito, f"Error: '{nombre_producto_agregado}' no aparece en el carrito."
    logger.info(f"✅ Validación exitosa: El producto '{nombre_producto_agregado}' está en el carrito.")

    # 4. Ir a Checkout
    logger.info("STEP 4: Procediendo al Checkout...")
    cart.click_checkout()
    
    # Verificación final: ¿Cambiamos de URL?
    assert "checkout-step-one.html" in driver.current_url, "Error: No se redirigió a la página de checkout."
    logger.info("✅ Redirección a Checkout correcta.")
    logger.info("--- TEST FINALIZADO EXITOSAMENTE ---")


@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_remove_item_from_cart(driver, username, password):
    """
    TEST B: Agregar item -> Ir a Carrito -> Remover item -> Verificar vacío
    """
    logger.info("--- INICIO TEST: Remover Item del Carrito ---")
    
    # 1. Login y Agregar
    logger.info("STEP 1: Preparando entorno (Login + Agregar producto)...")
    login = LoginPage(driver)
    login.open()
    login.login(username, password)
    
    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.open_cart()

    # 2. Remover desde el Carrito
    logger.info("STEP 2: Removiendo el producto desde el carrito...")
    cart = CartPage(driver)
    cart.click_remove_first_item()

    # 3. Validar que esté vacío
    logger.info("STEP 3: Verificando que el carrito quedó vacío...")
    esta_vacio = cart.is_cart_empty()
    
    assert esta_vacio, "Error: El carrito debería estar vacío después de remover el item."
    logger.info("✅ Validación exitosa: El carrito está vacío.")
    logger.info("--- TEST FINALIZADO EXITOSAMENTE ---")
