import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.logger import logger  # <--- 1. Importar el logger

@pytest.mark.parametrize("username,password", [
    ("standard_user", "secret_sauce")
])
def test_agregar_item_al_inventario(driver, username, password):
    """
    Test que valida agregar un item al carrito desde la página de inventario.
    """
    # Log de inicio del test
    logger.info("\n" + "="*60)
    logger.info("🚀 INICIO TEST: Agregar Item al Inventario") 
    logger.info("="*60)

    # 1. PRECONDICIÓN
    logger.info("STEP 1: Realizando Login...")
    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    # 2. INICIO DEL TEST DE INVENTARIO
    inventory = InventoryPage(driver)

    # 3. Validar que hay productos visibles
    logger.info("STEP 2: Verificando carga del catálogo...")
    productos = inventory.obtain_all_products()
    assert len(productos) > 0, "Error: No se cargaron los productos"

    # 4. Validar que el carrito empieza vacío
    logger.info("STEP 3: Verificando que el carrito esté vacío al inicio...")
    cantidad_inicial = inventory.get_cart_item_count()
    assert cantidad_inicial == 0, "Error: El carrito debería estar vacío al inicio"

    # 5. Acción: Agregar el primer producto
    logger.info("STEP 4: Agregando el primer producto al carrito...")
    inventory.add_first_product_to_cart()

    # 6. Validar que el contador subió a 1
    logger.info("STEP 5: Verificando que el contador del carrito aumentó...")
    cantidad_final = inventory.get_cart_item_count()
    assert cantidad_final == 1, f"Error: Esperaba 1 item, pero hay {cantidad_final}"

    logger.info("--- TEST FINALIZADO EXITOSAMENTE ---\n") # <--- Log de cierre con espacio