from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, '//button[text()= " Login "]')
        self.verify_success_text = (By.XPATH, '//span[text()="Dashboard"]')
        # self.verify_fail_text =

    def open_page(self):
        self.driver.get(self.url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def successfully_login(self):
        self.driver.find_element(*self.verify_success_text)

    # def fail_login(self):
    #     self.driver.find_element(By.XPATH, '//p[text() ="Invalid credentials"] | //span[text() = '
    #                                        '"Required"]')
