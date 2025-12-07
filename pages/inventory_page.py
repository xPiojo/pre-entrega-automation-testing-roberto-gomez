from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.logger import logger

class InventoryPage:
    """
    Page Object para la página de inventario (Catálogo).
    Maneja la visualización de productos y la interacción básica con el carrito.
    """

    # --- Selectores ---
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")

    def __init__(self, driver):
        """
        Inicializa la página de inventario.

        Args:
            driver: Instancia de WebDriver de Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.info("InventoryPage inicializada")

    def obtain_all_products(self):
        """
        Obtiene la lista de todos los elementos de producto visibles.

        Returns:
            list: Lista de WebElements que representan los productos.
        """
        # Esperamos a que sean visibles antes de buscarlos
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        
        items = self.driver.find_elements(*self._INVENTORY_ITEMS)
        logger.info(f"Productos encontrados en catálogo: {len(items)}")
        return items

    def obtener_datos_catalogo(self):
        """
        Extrae la información (nombre y precio) de todos los productos.

        Returns:
            list[dict]: Lista de diccionarios con formato {'nombre': str, 'precio': float}.
        """
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        elementos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        
        datos_web = []
        for item in elementos:
            nombre = item.find_element(*self._ITEM_NAME).text
            texto_precio = item.find_element(*self._ITEM_PRICE).text
            # Limpiamos el precio: "$29.99" -> 29.99
            precio_limpio = float(texto_precio.replace('$', ''))
            
            datos_web.append({'nombre': nombre, 'precio': precio_limpio})
            
        logger.info(f"Datos extraídos del catálogo web: {len(datos_web)} productos.")
        return datos_web

    def get_cart_item_count(self):
        """
        Obtiene la cantidad de ítems mostrada en el badge del carrito.

        Returns:
            int: Cantidad de ítems (0 si el carrito está vacío).
        """
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            count = int(badge.text)
            logger.info(f"Badge del carrito encontrado. Cantidad: {count}")
            return count
        except NoSuchElementException:
            logger.info("No se encontró badge (Carrito vacío).")
            return 0

    def add_first_product_to_cart(self):
        """
        Hace clic en el botón 'Add to cart' del primer producto disponible.
        """
        self.wait.until(EC.element_to_be_clickable(self._ADD_TO_CART_BUTTON))
        
        botones = self.driver.find_elements(*self._ADD_TO_CART_BUTTON)
        
        if len(botones) > 0:
            botones[0].click()
            logger.info("Click realizado en el primer producto.")
        else:
            logger.error("Error: No se encontraron botones para agregar.")