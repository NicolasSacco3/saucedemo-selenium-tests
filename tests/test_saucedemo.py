import pytest
from pages.login_page import Login_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(autouse=True)
def login(driver):
    """Realiza el login antes de cada test de inventario."""
    login_page = Login_Page(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

def test_catalogo_productos( driver ):
  
     assert "inventory.html" in driver.current_url 
     
     title = driver.find_element(By.CLASS_NAME,"title").text
     assert title == "Products"

     productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
     assert len(productos) > 0

##Prueba si existe el segundo artículo
     nombre = productos[1].find_element(By.CLASS_NAME, "inventory_item_name ").text
     assert nombre == "Sauce Labs Bike Light"
## Prueba si existen los botónes Add To Cart
     btm = driver.find_elements(By.ID, "add-to-cart-sauce-labs-backpack")
     assert len(btm) > 0

def test_verificar_barra_menu ( driver ):
     wait = WebDriverWait (driver, 10)

     #Apreto el botón
     btn_menu = wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
     btn_menu.click()       

     #Dentro de la barra
     dentro = driver.find_element(By.CLASS_NAME,"bm-item-list").text
     assert dentro == "All Items" or "About" or "Logout" or "Reset App State"

def test_agregar_al_carrito( driver ):
     
     wait = WebDriverWait (driver, 10)

     #Agrego el producto 
     btn_add = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Add to cart')]"))
     )
     btn_add.click()

     #capturo el nombre del prducto clickeado
     #
     product_name = driver.find_element(By.CLASS_NAME,"inventory_item_name").text

     #contador
     badge = driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
     assert badge.text == "1"

     driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

     #productos en el carrito
     product_carrito = driver.find_element(By.CLASS_NAME,"inventory_item_name").text
     assert product_carrito == product_name

def test_verificar_boton_remove_de_un_producto( driver ):
     wait = WebDriverWait (driver, 10)   #Agrego el producto 
     btn_add = wait.until(EC.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light")))
     btn_add.click()
     btn_second = driver.find_element(By.ID,"remove-sauce-labs-bike-light").text
     assert btn_second == "Remove"
