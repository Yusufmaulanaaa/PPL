import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    """Inisialisasi browser Google Chrome untuk setiap fungsi pengujian."""
    options = Options()
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    # Hapus tanda # di bawah jika ingin menjalankan tanpa tampilan browser:
    # options.add_argument("--headless=new")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
