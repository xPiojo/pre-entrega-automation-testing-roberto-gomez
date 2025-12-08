from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger

class CheckoutPage:
    """
    Page Object que maneja todo el flujo de checkout:
    1. Formulario de datos (Step One)
    2. Confirmación de compra (Step Two)
    3. Mensaje final de éxito (Checkout Complete)
    """

    # --- SELECTORES (STEP ONE) ---
    _FIRST_NAME_INPUT = (By.ID, "first-name") # Campo de Nombre
    _LAST_NAME_INPUT = (By.ID, "last-name")  # Campo de Apellido
    _POSTAL_CODE_INPUT = (By.ID, "postal-code") # Campo de Código Postal
    _CONTINUE_BUTTON = (By.ID, "continue") # Botón para continuar al Step Two
    
    
    # --- SELECTORES (STEP TWO - OVERVIEW) ---
    _FINISH_BUTTON = (By.ID, "finish")  # El botón para finalizar la compra
    
    # --- SELECTORES (COMPLETE) ---
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header") # El texto "Thank you for your order!"
    _BACK_HOME_BUTTON = (By.ID, "back-to-products")  # Botón para volver al inventario

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.info("CheckoutPage inicializada")
    
    # --- MÉTODOS DEL PASO 1 (Formulario) ---
    def enter_user_information(self, first_name, last_name, postal_code):
        """Ingresa la información del usuario en los campos correspondientes."""
        logger.info("Ingresando información del usuario en Checkout...")
        self.wait.until(EC.visibility_of_element_located(self._FIRST_NAME_INPUT)).send_keys(first_name)
        self.driver.find_element(*self._LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*self._POSTAL_CODE_INPUT).send_keys(postal_code)
        logger.info(f"Información ingresada: {first_name} {last_name}, {postal_code}")
    
    def click_continue(self):
        """Hace clic en el botón de Continuar (pasa al Step Two)."""
        logger.info("Haciendo click en Continuar...")
        self.wait.until(EC.element_to_be_clickable(self._CONTINUE_BUTTON)).click()

    # --- MÉTODOS DEL PASO 2 (Confirmación) ---
    def click_finish(self):
        """Hace clic en el botón Finish para completar la orden."""
        logger.info("Haciendo click en Finish...")
        # Esperamos a que el botón finish sea visible (estamos en la pag 2)
        self.wait.until(EC.element_to_be_clickable(self._FINISH_BUTTON)).click()

    # --- MÉTODOS PASO 3: VALIDACIÓN Y RETORNO ---
    def get_complete_message(self):
        """Devuelve el mensaje de éxito (Ej: 'Thank you for your order!')."""
        msg = self.wait.until(EC.visibility_of_element_located(self._COMPLETE_HEADER)).text
        logger.info(f"Mensaje final obtenido: '{msg}'")
        return msg

    def click_back_home(self):
        """Click en 'Back Home' para volver al inventario."""
        logger.info("Click en 'Back Home' (Volviendo a la tienda)...")
        self.wait.until(EC.element_to_be_clickable(self._BACK_HOME_BUTTON)).click()