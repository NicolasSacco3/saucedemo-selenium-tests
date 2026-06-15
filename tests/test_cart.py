import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login_page import Login_Page


@pytest.fixture(autouse=True)
def login_and_add_product(driver):
    """Realiza el login y agrega un producto al carrito antes de cada test."""
    login_page = Login_Page(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()


def test_producto_en_carrito(driver):
    """Verifica que el producto agregado aparece en el carrito."""
    cart = CartPage(driver)
    items = cart.get_cart_items()
    assert len(items) == 1


def test_nombre_producto_en_carrito(driver):
    """Verifica que el nombre del producto en el carrito es el correcto."""
    cart = CartPage(driver)
    names = cart.get_product_names()
    assert "Sauce Labs Backpack" in names


def test_eliminar_producto_del_carrito(driver):
    """Verifica que al eliminar un producto el carrito queda vacío."""
    cart = CartPage(driver)
    cart.remove_first_item()
    assert cart.is_cart_empty()


def test_boton_remove_visible(driver):
    """Verifica que el botón Remove es visible para el producto en el carrito."""
    from selenium.webdriver.common.by import By
    btn = driver.find_element(By.XPATH, "//button[contains(text(),'Remove')]")
    assert btn.is_displayed()


def test_continuar_comprando(driver):
    """Verifica que el botón 'Continue Shopping' redirige al inventario."""
    cart = CartPage(driver)
    cart.continue_shopping()
    assert "inventory.html" in driver.current_url
