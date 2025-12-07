from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from utils.logger import logger

class InventoryPage:
    """
    Page Object para la página de inventario (Catálogo).
    """

    # --- Selectores ---
    _INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item")
    _ADD_TO_CART_BUTTON = (By.CLASS_NAME, "btn_inventory")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        # Agregamos la espera explícita
        self.wait = WebDriverWait(driver, 10)
        logger.info("InventoryPage inicializada")

    def obtain_all_products(self):
        """Devuelve la lista de todos los productos en pantalla"""
        # Esperamos a que sean visibles antes de buscarlos (Más robusto)
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        
        items = self.driver.find_elements(*self._INVENTORY_ITEMS)
        logger.info(f"Productos encontrados en catálogo: {len(items)}")
        return items

    def get_cart_item_count(self):
        """
        Devuelve el número del carrito. 
        Si no hay badge, asumimos 0.
        """
        try:
            # Intentamos buscar el badge
            badge = self.driver.find_element(*self._CART_BADGE)
            count = int(badge.text)
            logger.info(f"Badge del carrito encontrado. Cantidad: {count}")
            return count
        except NoSuchElementException:
            # Si no existe el elemento, es que el carrito está vacío
            logger.info("No se encontró badge (Carrito vacío).")
            return 0

    def add_first_product_to_cart(self):
        """Busca el primer botón 'Add to cart' y le hace click"""
        # Esperamos a que los botones sean clickeables
        self.wait.until(EC.element_to_be_clickable(self._ADD_TO_CART_BUTTON))
        
        botones = self.driver.find_elements(*self._ADD_TO_CART_BUTTON)
        
        if len(botones) > 0:
            botones[0].click()
            logger.info("Click realizado en el primer producto.")
        else:
            logger.error("Error: No se encontraron botones para agregar.")

    def obtener_datos_catalogo(self):
        """
        Recorre todos los productos en pantalla y devuelve una lista de diccionarios
        con el nombre y el precio (convertido a float) de cada uno.
        Estructura: [{'nombre': 'Sauce...', 'precio': 29.99}, ...]
        """
        # Esperamos a que todo cargue
        self.wait.until(EC.visibility_of_all_elements_located(self._INVENTORY_ITEMS))
        
        elementos = self.driver.find_elements(*self._INVENTORY_ITEMS)
        datos_web = []

        for item in elementos:
            # Extraemos nombre
            nombre = item.find_element(*self._ITEM_NAME).text
            
            # Extraemos precio (Ej: "$29.99")
            texto_precio = item.find_element(*self._ITEM_PRICE).text
            # Quitamos el '$' y convertimos a número (float)
            precio_limpio = float(texto_precio.replace('$', ''))

            datos_web.append({
                'nombre': nombre,
                'precio': precio_limpio
            })
        
        logger.info(f"Datos extraídos del catálogo web: {len(datos_web)} productos.")
        return datos_web