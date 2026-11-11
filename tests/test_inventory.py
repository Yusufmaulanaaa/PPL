import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture
def logged_in(driver):
    """Precondition: login sebagai standard_user."""
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_dashboard_displayed() is True
    return login_page


class TestInventory:

    def test_add_backpack_to_cart(self, driver, logged_in):
        """TC-04: Badge keranjang menunjukkan '1' setelah Backpack ditambahkan."""
        inventory = InventoryPage(driver)
        inventory.add_backpack_to_cart()

        actual = inventory.get_cart_badge_count()
        assert actual == "1", f"Badge diharapkan '1', tetapi '{actual}'"

    def test_logout(self, driver, logged_in):
        """TC-05: Logout mengembalikan user ke halaman login."""
        inventory = InventoryPage(driver)
        inventory.logout()

        expected_url = "https://www.saucedemo.com/"
        actual_url = inventory.get_current_url()
        assert actual_url == expected_url, (
            f"URL diharapkan '{expected_url}', tetapi '{actual_url}'"
        )
        assert logged_in.is_login_button_displayed() is True, (
            "Tombol login tidak tampil setelah logout"
        )
