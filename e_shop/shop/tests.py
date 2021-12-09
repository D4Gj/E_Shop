import time
from decimal import Decimal

from django.test import LiveServerTestCase, TestCase
from selenium import webdriver
from django.contrib.auth.models import User

from selenium.webdriver.support.select import Select


class WebShopTest(LiveServerTestCase):

    def test_register_noteq_pass(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get(self.live_server_url)
        login_link = selenium.find_element(value="login")
        login_link.click()
        register_link = selenium.find_element(value="register")
        register_link.click()
        input_username = selenium.find_element(value="id_username")
        input_firstname = selenium.find_element(value="id_first_name")
        input_email = selenium.find_element(value="id_email")
        input_pass = selenium.find_element(value="id_password")
        input_pass2 = selenium.find_element(value="id_password2")
        submit = selenium.find_element(value="id_btn_register")

        input_username.send_keys("MyAwesomeLogin")
        input_firstname.send_keys("Vasya")
        input_email.send_keys("awesome@mail.com")
        input_pass.send_keys("!Qwerty12345")
        input_pass2.send_keys("!Qwerty123")

        submit.click()

        assert "Пароли не совпадают." in selenium.page_source

    def test_register_incorrect_email(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get(self.live_server_url)
        login_link = selenium.find_element(value="login")
        login_link.click()
        register_link = selenium.find_element(value="register")
        register_link.click()
        input_username = selenium.find_element(value="id_username")
        input_firstname = selenium.find_element(value="id_first_name")
        input_email = selenium.find_element(value="id_email")
        input_pass = selenium.find_element(value="id_password")
        input_pass2 = selenium.find_element(value="id_password2")
        submit = selenium.find_element(value="id_btn_register")

        input_username.send_keys("MyAwesomeLogin")
        input_firstname.send_keys("Vasya")
        input_email.send_keys("awesomemail.com")
        input_pass.send_keys("!Qwerty12345")
        input_pass2.send_keys("!Qwerty12345")

        submit.click()

        assert "Создать аккаунт" in selenium.title

    def test_register(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        login_link = selenium.find_element(value="login")
        login_link.click()
        register_link = selenium.find_element(value="register")
        register_link.click()
        input_username = selenium.find_element(value="id_username")
        input_firstname = selenium.find_element(value="id_first_name")
        input_email = selenium.find_element(value="id_email")
        input_pass = selenium.find_element(value="id_password")
        input_pass2 = selenium.find_element(value="id_password2")
        submit = selenium.find_element(value="id_btn_register")

        input_username.send_keys("MyAwesomeLogin")
        input_firstname.send_keys("Vasya")
        input_email.send_keys("awesome@mail.com")
        input_pass.send_keys("!Qwerty12345")
        input_pass2.send_keys("!Qwerty12345")

        submit.click()

        assert "Добро пожаловать" in selenium.page_source

    def test_login(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        login_link = selenium.find_element(value="login")
        login_link.click()
        input_login = selenium.find_element(value="id_username")
        input_password = selenium.find_element(value="id_password")
        submit = selenium.find_element("id","login_btn")

        input_login.send_keys("inzad")
        input_password.send_keys("1122Qwerty")
        submit.click()

        assert "Аккаунт" in selenium.page_source

    def test_login_no_acc(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        login_link = selenium.find_element(value="login")
        login_link.click()
        input_login = selenium.find_element(value="id_username")
        input_password = selenium.find_element(value="id_password")
        submit = selenium.find_element("id","login_btn")

        input_login.send_keys("RandomLogin")
        input_password.send_keys("!Qwerty12345")
        submit.click()

        assert "Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру." \
               in selenium.page_source

    def test_register_acc_exists(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        login_link = selenium.find_element(value="login")
        login_link.click()
        register_link = selenium.find_element(value="register")
        register_link.click()
        input_username = selenium.find_element(value="id_username")
        input_firstname = selenium.find_element(value="id_first_name")
        input_email = selenium.find_element(value="id_email")
        input_pass = selenium.find_element(value="id_password")
        input_pass2 = selenium.find_element(value="id_password2")
        submit = selenium.find_element(value="id_btn_register")

        input_username.send_keys("inzad")
        input_firstname.send_keys("Vasya")
        input_email.send_keys("awesome@mail.com")
        input_pass.send_keys("!Qwerty12345")
        input_pass2.send_keys("!Qwerty12345")

        submit.click()

        assert "Пользователь с таким именем уже существует." in selenium.page_source

    def test_add_product(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        selenium.find_element(value="login").click()

        input_login = selenium.find_element(value="id_username")
        input_password = selenium.find_element(value="id_password")

        input_login.send_keys("inzad")
        input_password.send_keys("1122Qwerty")
        selenium.find_element(value="login_btn").click()

        selenium.find_element(value="admin").click()
        selenium.find_element_by_xpath('//a[contains(@href,"admin/shop/product/add/")]').click()
        category = Select(selenium.find_element(value="id_category"))
        category.select_by_visible_text("Видеокарты")
        selenium.find_element(value="id_name").send_keys("Test-card")
        selenium.find_element(value="id_price").send_keys("999")
        selenium.find_element(by="name", value="_save").click()
        selenium.get("http://127.0.0.1:8000/")

        assert "Test-card" in selenium.page_source

    def test_add_cart(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        selenium.find_element(by="class name", value="item").click()
        selenium.find_element_by_xpath("//input[@type='submit']").click()
        assert "Ваша корзина" in selenium.page_source
        assert "Товары в корзине" in selenium.page_source

    def test_remove_cart(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        selenium.find_element(by="class name", value="item").click()
        selenium.find_element_by_xpath("//input[@type='submit']").click()
        selenium.find_element(by="id", value="8").click()
        assert "Корзина пуста." in selenium.page_source

    def test_update_cart(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        selenium = webdriver.Chrome('C://Users//1//PycharmProjects//E_Shop//e_shop//shop//static//chromedriver.exe',
                                    options=options)
        selenium.get("http://127.0.0.1:8000/")
        selenium.find_element(by="class name", value="item").click()
        price = selenium.find_element("class name", "price").text
        selenium.find_element_by_xpath("//input[@type='submit']").click()
        amount = Select(selenium.find_element(by="id", value="id_quantity"))
        amount.select_by_visible_text("2")
        selenium.find_element("id", "update8").click()
        sum_price = selenium.find_element_by_xpath("//td[@class='total']").text
        price = float(price[1:].replace(",", ".")) * 2
        sum_price = float(sum_price[1:].replace(",", "."))

        assert price == sum_price
