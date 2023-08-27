from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    # LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, '[href="/ru/basket/"]')
    # BASKET_LINK = (By.CSS_SELECTOR, "//a[contains(text(), 'Посмотреть корзину')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    ALL_PRODUCT_LINK = (By.CSS_SELECTOR, '[href="/ru/catalogue/"]')

# class MainPageLocators():
    # LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_FIELD = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_FIELD1 = (By.ID, "id_registration-password1")
    REGISTER_PASSWORD_FIELD2 = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class CatalogPageLocators():
    FIRST_PRODUCT = (By.XPATH, "/html/body/div[2]/div/div/div/section/div/ol/li[1]/article/div[1]/a")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/h1")
    PRODUCT_PRICE = (By.XPATH, "/html/body/div[2]/div/div[2]/div[2]/article/div[1]/div[2]/p[1]")
    ADDED_TO_BASKET_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div/strong")
    PRICE_OF_BASKET_MESSAGE = (By.XPATH, "/html/body/div[2]/div/div[1]/div[3]/div/p[1]/strong")
    '''ПЕРВОЕ УСПЕШНОЕ СООБШЕНИЕ'''
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alert-success")

class BasketPageLocators():
    PRODUCT_LINK = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_MASSAGE = (By.CSS_SELECTOR), "[id='content_inner']>p"

