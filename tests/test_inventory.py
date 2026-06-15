import pytest
from pages.inventory_page import InventoryPage
from pages.login_page import Login_Page


@pytest.fixture(autouse=True)
def login(driver):
    """Realiza el login antes de cada test de inventario."""
    login_page = Login_Page(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")


def test_titulo_inventario(driver):
    """Verifica que el título de la página de inventario es 'Products'."""
    inventory = InventoryPage(driver)
    assert inventory.get_title() == "Products"


def test_productos_visibles(driver):
    """Verifica que el catálogo carga al menos un producto."""
    inventory = InventoryPage(driver)
    products = inventory.get_products()
    assert len(products) > 0


def test_segundo_producto_correcto(driver):
    """Verifica que el segundo producto es 'Sauce Labs Bike Light'."""
    inventory = InventoryPage(driver)
    names = inventory.get_product_names()
    assert names[1] == "Sauce Labs Bike Light"


def test_agregar_producto_al_carrito(driver):
    """Verifica que al agregar un producto el badge del carrito muestra 1."""
    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    assert inventory.get_cart_badge_count() == "1"


def test_menu_lateral(driver):
    """Verifica que el menú lateral contiene las opciones esperadas."""
    inventory = InventoryPage(driver)
    inventory.open_menu()
    menu_text = inventory.get_menu_text()
    assert "All Items" in menu_text
    assert "Logout" in menu_text
    assert "About" in menu_text
    assert "Reset App State" in menu_text
