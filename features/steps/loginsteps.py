from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'I launch Chrome Browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="/Users/vaku5928/Downloads/chromedriver")


@when(u'I open orange HRM Home Page')
def step_impl(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when(u'Enter username "{user}" and password "{pwd}"')
def step_impl(context, user, pwd):
    context.driver.find_element(By.ID, "txtUsername").send_keys(user)
    context.driver.find_element(By.ID, "txtPassword").send_keys(pwd)
    context.driver.find_element(By.ID, "btnLogin").click()


@then(u'User must successfully login to Dashboard page')
def step_impl(context):
    try:
        print(context)
        welcome_message_ele = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Dashboard')]").text
        # welcome_message = welcome_message_ele.text()

    except:
        assert False, "Unable to fetch Dashboard element"
    # assert welcome_message_ele == "Dashboard"
    if welcome_message_ele == "Dashboard":
        context.driver.close()
        assert True, "Test Passed"
