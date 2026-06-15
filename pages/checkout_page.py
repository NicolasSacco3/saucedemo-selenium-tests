from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    # Paso 1 - datos personales
    _FIRST_NAME = (By.ID, "first-name")
    _LAST_NAME = (By.ID, "last-name")
    _POSTAL_CODE = (By.ID, "postal-code")
    _CONTINUE_BTN = (By.ID, "continue")
    _ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    # Paso 2 - resumen
    _SUMMARY_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    _FINISH_BTN = (By.ID, "finish")

    # Confirmación
    _COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    _COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # --- Paso 1: Información personal ---

    def fill_personal_info(self, first_name, last_name, postal_code):
        self.wait.until(
            EC.presence_of_element_located(self._FIRST_NAME)
        ).send_keys(first_name)

        self.driver.find_element(*self._LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self._POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        self.driver.find_element(*self._CONTINUE_BTN).click()

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._ERROR_MSG)
        ).text

    # --- Paso 2: Resumen de orden ---

    def get_summary_product_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self._ITEM_NAMES)
        )
        return [e.text for e in elements]

    def get_total(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._TOTAL_LABEL)
        ).text

    def click_finish(self):
        self.wait.until(
            EC.element_to_be_clickable(self._FINISH_BTN)
        ).click()

    # --- Confirmación ---

    def get_confirmation_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._COMPLETE_HEADER)
        ).text

    def get_confirmation_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._COMPLETE_TEXT)
        ).text
