from playwright.sync_api import sync_playwright
from pathlib import Path
from behave import given, when, then
from variables import LOGIN_VAR, PASSWORD_VAR, PATH_VAR

SESSION_FILE_PATH = Path(PATH_VAR)

def save_storage_state(context, path):
    context.context.storage_state(path=path)

def load_storage_state(context, path):
    context.context = context.browser.new_context(storage_state=path)

@given('the user navigates to GitHub login page')
def step_impl(context):
    context.context = context.browser.new_context()
    context.page = context.context.new_page()
    context.page.goto("https://github.com/login")

@when('the user enters valid credentials')
def step_impl(context):
    context.page.fill("input[name='login']", LOGIN_VAR)
    context.page.fill("input[name='password']", PASSWORD_VAR)
    context.page.click("input[value='Sign in']")
    save_storage_state(context, SESSION_FILE_PATH)

@then('the user should be logged in and session should be saved')
def step_impl(context):
    assert context.page.url == "https://github.com/"

@given('the user has a saved session')
def step_impl(context):
    load_storage_state(context, SESSION_FILE_PATH)
    context.page = context.context.new_page()

@when('the user opens GitHub with the saved session')
def step_impl(context):
    context.page.goto("https://github.com/")

@then('the user should see the dashboard content')
def step_impl(context):
    assert context.page.is_visible("#dashboard > div > feed-container > div.d-flex.flex-justify-between.flex-items-center > h2")