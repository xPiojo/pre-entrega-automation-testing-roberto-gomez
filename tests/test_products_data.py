import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from utils.lector_json import leer_datos_productos
from utils.logger import logger  # <--- Import del logger

# Cargamos el JSON una sola vez al principio
DATOS_ESPERADOS = leer_datos_productos("data/productos.json")

@pytest.mark.parametrize("username,password", [("standard_user", "secret_sauce")])
def test_validar_precios_inventario(driver, username, password):
    """
    Test de Datos: Valida que los precios en la web coincidan
    con la base de datos oficial (JSON).
    """

    logger.info("--- INICIO TEST: Validación de Datos del Catálogo (JSON vs Web) ---")

    # 1. Login (Precondición)
    logger.info("STEP 1: Iniciando sesión en la aplicación...")
    login = LoginPage(driver)
    login.open()
    login.login(username, password)

    # 2. Obtener datos reales de la web
    logger.info("STEP 2: Extrayendo catálogo de productos desde el navegador...")
    inventory = InventoryPage(driver)
    productos_en_web = inventory.obtener_datos_catalogo()

    # 3. Convertir lista web a diccionario para buscar fácil
    logger.info("STEP 3: Procesando datos obtenidos para comparación...")
    # {'Sauce Labs Backpack': 29.99, ...}
    precios_web = {p['nombre']: p['precio'] for p in productos_en_web}

    logger.info("STEP 4: Iniciando validación cruzada (JSON vs Web)...")
    
    # 4. Validar cada producto del JSON
    for item in DATOS_ESPERADOS:
        nombre = item['nombre']
        precio_esperado = item['precio']

        # A) ¿Existe el producto?
        assert nombre in precios_web, f"Error: El producto '{nombre}' no aparece en la web"

        # B) ¿El precio es correcto?
        precio_real = precios_web[nombre]
        assert precio_real == precio_esperado, (
            f"Precio incorrecto en '{nombre}'. "
            f"Esperado: ${precio_esperado} | Encontrado: ${precio_real}"
        )

        # <--- Log de éxito por cada producto
        logger.info(f"   -> ✅ Producto validado: '{nombre}' | Precio: ${precio_real} (Correcto)")