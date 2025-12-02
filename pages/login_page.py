from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import logger


class LoginPage:
    URL = "https://www.saucedemo.com/"

    _USER_INPUT = (By.ID, "user-name")
    _PASS_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")
    _ERROR_MSG = (By.CSS_SELECTOR, "h3[data-test='error']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        logger.info("LoginPage inicializada")

    def open(self):
        logger.info(f"Abrir URL: {self.URL}")
        self.driver.get(self.URL)

    def login(self, username, password):
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

    def get_error_message(self):
        logger.info("Buscando mensaje de error...")
        error_element = self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MSG)
        )
        msg = error_element.text
        logger.info(f"Mensaje de error encontrado: '{msg}'")
        return msg