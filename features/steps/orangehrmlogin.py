from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from orangehrmPOM import LoginPage
from selenium.webdriver.common.by import By


@given('I launch Chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()


@when('I open orangeHRM homepage')
def open_homepage(context):
    login_page = LoginPage(context.driver)
    login_page.open_page()
    context.driver.implicitly_wait(10)


@when('Enter username "{user}" and password "{pwd}"')
def enter_username_pass(context, user, pwd):
    login_page = LoginPage(context.driver)

    if user == "empty":
        login_page.enter_username("")
        login_page.enter_password("")
    else:
        login_page.enter_username(user)
        login_page.enter_password(pwd)


@when('click on login button')
def click_login_button(context):
    login_page = LoginPage(context.driver)
    login_page.click_login()


@then('User must successfully login to the Dashboard page with "{msg}"')
def check_dashboard(context, msg):
    login_page = LoginPage(context.driver)

    try:
        text = login_page.successfully_login()
        if msg == text:
            context.driver.close()
            assert True, "Test Passed"
    except:
        wait = WebDriverWait(context.driver, 10)
        element = context.driver.find_element(By.XPATH, '//p[text() ="Invalid credentials"] | //span[text() = '
                                                        '"Required"]')

        wait.until(lambda d: element.is_displayed())
        if msg == element:
            context.driver.close()
            assert True, "Test Failed"

# @then('Proper message should be displayed')
# def alert(context):
#     context.driver.implicitly_wait(10)
#     wait = WebDriverWait(context.driver, 10)  # Create a WebDriverWait instance
#     element = context.driver.find_element(By.XPATH, '//span[text() = "Required"]')
#     wait.until(lambda d: element.is_displayed())
#     print(element, element.text)
#     if element == "Required":
#         context.driver.close()
#         assert True, "Test Failed"
