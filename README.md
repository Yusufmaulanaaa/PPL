# SauceDemo Automation (Selenium + pytest + POM)

Otomasi pengujian UI untuk https://www.saucedemo.com/ dengan Page Object Model.

## Anggota Kelompok

| Nama | NIM |
|------|-----|
| Daffa Amri Hisbullah | 24090078 |
| Yusuf Maulana Syifa | 24090087 |
| Mustofa Achmad | 24090102 |

## Struktur

- `pages/`  : Page Object (locator Relative XPath + aksi)
  - `base_page.py` : class induk, explicit wait dan aksi dasar Selenium
  - `login_page.py` : halaman login
  - `inventory_page.py` : halaman inventory
- `tests/`  : Skrip uji + assertions
  - `test_login.py` : 3 test login
  - `test_inventory.py` : test add to cart dan logout
- `conftest.py` : fixture browser

## Cara menjalankan

Butuh Python 3.10+ dan Google Chrome.

```bash
python -m venv venv
# Windows: .\venv\Scripts\Activate.ps1   |   Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
pytest -v
```

## Catatan

- Tidak memakai absolute XPath dan tidak memakai `time.sleep()`, waktu tunggu pakai explicit wait di `BasePage`.
- Semua locator ada di folder `pages/`, tidak ada locator di file test.

## Hasil Test

Dijalankan dengan `py -m pytest -v`:

```
============================= test session starts =============================
platform win32 -- Python 3.12.6, pytest-9.2.0, pluggy-1.7.0 -- C:\Users\ADVAN\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: D:\semester-5\Capstone\PPL\PPL
configfile: pytest.ini
testpaths: tests
plugins: anyio-4.15.1
collecting ... collected 5 items

tests/test_inventory.py::TestInventory::test_add_backpack_to_cart PASSED [ 20%]
tests/test_inventory.py::TestInventory::test_logout PASSED               [ 40%]
tests/test_login.py::TestLogin::test_login_positive_valid_user PASSED    [ 60%]
tests/test_login.py::TestLogin::test_login_negative_locked_out_user PASSED [ 80%]
tests/test_login.py::TestLogin::test_login_negative_empty_password PASSED [100%]

============================= 5 passed in 19.41s ==============================
```

Hasil: **5 passed** — semua test case lolos.

## Diupload oleh

Yusufmaulanaa (yusufmaulanasyifa25@gmail.com) ke repositori GitHub.
