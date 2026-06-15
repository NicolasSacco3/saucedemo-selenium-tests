from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:

    _TITLE = (By.CLASS_NAME, "title")
    _ITEMS = (By.CSS_SELECTOR, "[data-test='inventory-item']")
    _ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    _MENU_BTN = (By.ID, "react-burger-menu-btn")
    _MENU_ITEMS = (By.CLASS_NAME, "bm-item-list")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._TITLE)
        ).text

    def get_products(self):
        return self.wait.until(
            EC.presence_of_all_elements_located(self._ITEMS)
        )

    def get_product_names(self):
        elements = self.wait.until(
            EC.presence_of_all_elements_located(self._ITEM_NAMES)
        )
        return [e.text for e in elements]

    def add_first_product_to_cart(self):
        """Agrega el primer producto disponible al carrito y retorna su nombre."""
        product_name = self.wait.until(
            EC.presence_of_element_located(self._ITEM_NAMES)
        ).text
        self.wait.until(
            EC.element_to_be_clickable(self._ADD_TO_CART_BTN)
        ).click()
        return product_name

    def get_cart_badge_count(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._CART_BADGE)
        ).text

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self._CART_LINK)
        ).click()

    def open_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(self._MENU_BTN)
        ).click()

    def get_menu_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self._MENU_ITEMS)
        ).text
