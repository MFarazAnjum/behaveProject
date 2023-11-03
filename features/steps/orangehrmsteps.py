from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def launch_browser(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)


@when('open orangehrm homepage')
def open_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



@then('verify that the logo present on page')
def verify_logo(context):
    status = context.driver.find_element(By.XPATH, '//h5[text() = "Login"]').is_displayed()
    assert status is True


@then('close browser')
def close_browser(context):
    context.driver.close()
