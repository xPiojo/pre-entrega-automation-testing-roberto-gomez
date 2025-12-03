from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.logger import logger


class LoginPage:
    """
    Page Object para la página de login de SauceDemo.
    Encapsula la interacción con los elementos y la navegación.
    """

    URL = "https://www.saucedemo.com/"

    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        """
        Inicializa el Page Object con el driver de Selenium.
        
        Args:
            driver: instancia de WebDriver para controlar el navegador.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.info("LoginPage inicializada")

    def open(self):
        """
        Abre la URL de la página de login.
        """
        logger.info(f"Abrir URL: {self.URL}")
        self.driver.get(self.URL)

    def login(self, username, password):
        """
        Completa los campos de usuario y contraseña y hace click en login.
        
        Args:
            username (str): Nombre de usuario a ingresar.
            password (str): Contraseña a ingresar.
        """
        logger.info(f"Intentando login con username='{username}'")
        
        user_input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        pass_input = self.driver.find_element(*self._PASS_INPUT)
        login_button = self.driver.find_element(*self._LOGIN_BUTTON)

        user_input.clear()
        user_input.send_keys(username)

        pass_input.clear()
        pass_input.send_keys(password)

        login_button.click()
        logger.info("Click en botón de login")

    def has_error(self, timeout=3):
        """
        Verifica si aparece un mensaje de error en la página dentro del timeout dado.

        Args:
            timeout (int): Tiempo máximo en segundos para esperar el mensaje.

        Returns:
            bool: True si aparece mensaje de error, False si no.
        """
        logger.info("Verificando si hay mensaje de error...")
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(self._ERROR_MSG)
            )
            logger.info("Mensaje de error detectado.")
            return True
        except TimeoutException:
            logger.info("No se detectó mensaje de error.")
            return False
