from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:

    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _REMOVE_BTNS = (By.XPATH, "//button[contains(text(),'Remove')]")
    _CHECKOUT_BTN = (By.ID, "checkout")
    _CONTINUE_SHOPPING_BTN = (By.ID, "continue-shopping")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_items(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self._CART_ITEMS)
        )

    def get_product_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self._ITEM_NAMES)
        )
        return [e.text for e in elements]

    def remove_first_item(self):
        """Elimina el primer producto del carrito."""
        self.wait.until(
            EC.element_to_be_clickable(self._REMOVE_BTNS)
        ).click()

    def is_cart_empty(self):
        """Retorna True si no hay productos en el carrito."""
        items = self.driver.find_elements(*self._CART_ITEMS)
        return len(items) == 0

    def go_to_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self._CHECKOUT_BTN)
        ).click()

    def continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self._CONTINUE_SHOPPING_BTN)
        ).click()
