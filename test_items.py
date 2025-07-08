from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


class TestItems():
    def test_find_add_to_basket_button(self, browser):

        browser.get(link)
        print(f"Открытие страницы: {link}")

        url = browser.current_url
        print(f"Текущий URL: {url}")

        locale = browser.execute_script("return navigator.language")
        print(f"Текущая локаль: {locale}")

        sleep(10)

        try:
            btn = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")

        except NoSuchElementException:
            assert False, "Кнопка добавления в корзину не найдена."

        print(f"Кнопка добавления в корзину успешно найдена!")

        btn_text = btn.text
        print(f"Текст на кнопке: {btn_text}")

        sleep(2)