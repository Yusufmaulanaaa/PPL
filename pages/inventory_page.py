from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class InventoryPage(BasePage):
    """Page Object untuk halaman inventori SauceDemo."""

    # ELEMEN LOKATOR (Relative XPath)
    ADD_BACKPACK_BTN = (By.XPATH, "//button[contains(@data-test,'add-to-cart-sauce-labs-backpack')]")
    CART_BADGE = (By.XPATH, "//span[@data-test='shopping-cart-badge' or contains(@class,'shopping_cart_badge')]")
    BURGER_MENU_BTN = (By.XPATH, "//button[@id='react-burger-menu-btn']")
    LOGOUT_LINK = (By.XPATH, "//a[@id='logout_sidebar_link']")

    def add_backpack_to_cart(self):
        self.click(self.ADD_BACKPACK_BTN)

    def get_cart_badge_count(self) -> str:
        return self.get_text(self.CART_BADGE)

    def logout(self):
        self.click(self.BURGER_MENU_BTN)
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))
        self.click(self.LOGOUT_LINK)
        self.wait.until(EC.url_to_be("https://www.saucedemo.com/"))
