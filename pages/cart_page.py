from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import logger

class CartPage:
    """
    Page Object para la página del Carrito (/cart.html).
    Maneja la verificación de items, eliminación y paso al checkout.
    """

    # --- SELECTORES ---
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name") # Nombres de productos en el carrito
    _CHECKOUT_BUTTON = (By.ID, "checkout") # Botón de Checkout
    _REMOVE_BUTTON = (By.CLASS_NAME, "cart_button") # Botones de Remove

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.info("CartPage inicializada")

    def get_cart_items_names(self):
        """Devuelve una lista con los textos de los productos en el carrito."""
        try:
            self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEM_NAME))
            items = self.driver.find_elements(*self._CART_ITEM_NAME)
            nombres = [item.text for item in items]
            logger.info(f"Productos encontrados en carrito: {nombres}")
            return nombres
        except TimeoutException:
            logger.warning("No se encontraron items en el carrito (o lista vacía).")
            return []

    def click_checkout(self):
        """Hace clic en el botón de Checkout."""
        logger.info("Haciendo click en Checkout...")
        self.wait.until(EC.element_to_be_clickable(self._CHECKOUT_BUTTON)).click()
        
    def click_remove_first_item(self):
        """Remueve el primer item de la lista (si existe)."""
        logger.info("Intentando remover el primer producto...")
        # Buscamos todos los botones de remover
        botones = self.driver.find_elements(*self._REMOVE_BUTTON)
        
        if len(botones) > 0:
            botones[0].click()
            logger.info("Click realizado en botón 'Remove'.")
        else:
            logger.error("No se encontraron botones para remover.")
            
    def is_cart_empty(self):
        """Devuelve True si no hay items en el carrito."""
        items = self.driver.find_elements(*self._CART_ITEM_NAME)
        return len(items) == 0