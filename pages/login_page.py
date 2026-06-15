from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## Clases faltantes: Inventory - Carrito - Check Out 

class Login_Page:

    URL_SD = "https://www.saucedemo.com/"
    _USERNAME = (By.ID, "user-name")
    _PASS =  (By.ID, "password")
    _LOGINBUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open (self):
        self.driver.get(self.URL_SD)

    def login(self, username, password):

    
        self.wait.until(
            EC.presence_of_element_located(self._USERNAME)
        ).send_keys(username)
        
        self.driver.find_element(*self._PASS).send_keys(password)
        self.driver.find_element(*self._LOGINBUTTON).click() 