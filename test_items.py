import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_basket_button_present(browser):
    browser.get(link)
    # time.sleep(30)  # Закомментируйте эту строку при обычной работе
    button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert button is not None, "Add to basket button is not present"