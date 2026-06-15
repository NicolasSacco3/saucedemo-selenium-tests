import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import Login_Page


@pytest.fixture(autouse=True)
def login_and_go_to_checkout(driver):
    """Login, agrega producto y navega hasta el checkout antes de cada test."""
    login_page = Login_Page(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_first_product_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.go_to_checkout()


def test_checkout_campos_vacios(driver):
    """Verifica que se muestra error si se intenta continuar sin completar datos."""
    checkout = CheckoutPage(driver)
    checkout.click_continue()
    error = checkout.get_error_message()
    assert "First Name is required" in error


def test_checkout_sin_apellido(driver):
    """Verifica que se muestra error si falta el apellido."""
    checkout = CheckoutPage(driver)
    checkout.fill_personal_info("Nicolas", "", "1832")
    checkout.click_continue()
    error = checkout.get_error_message()
    assert "Last Name is required" in error


def test_checkout_sin_codigo_postal(driver):
    """Verifica que se muestra error si falta el código postal."""
    checkout = CheckoutPage(driver)
    checkout.fill_personal_info("Nicolas", "Sacco", "")
    checkout.click_continue()
    error = checkout.get_error_message()
    assert "Postal Code is required" in error


def test_checkout_resumen_producto(driver):
    """Verifica que el producto aparece en el resumen de la orden."""
    checkout = CheckoutPage(driver)
    checkout.fill_personal_info("Nicolas", "Sacco", "1832")
    checkout.click_continue()
    names = checkout.get_summary_product_names()
    assert len(names) > 0


def test_checkout_flujo_completo(driver):
    """Verifica el flujo completo de compra hasta la confirmación."""
    checkout = CheckoutPage(driver)
    checkout.fill_personal_info("Nicolas", "Sacco", "1832")
    checkout.click_continue()
    checkout.click_finish()
    assert checkout.get_confirmation_header() == "Thank you for your order!"
