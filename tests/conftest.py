
import pytest
from pathlib import Path
from playwright.sync_api import Page, expect

BASE_URL = "https://www.saucedemo.com/"
AUTH_FILE = Path("auth/user.json")


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 900},
        "ignore_https_errors": True,
    }


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return {
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
        "args": ["--start-maximized"],
    }


@pytest.fixture(scope="session")
def storage_state(browser):
    AUTH_FILE.parent.mkdir(parents=True, exist_ok=True)

    context = browser.new_context()
    page = context.new_page()

    # SETUP: Login once per test session
    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(BASE_URL + "inventory.html")

    context.storage_state(path=str(AUTH_FILE))

    context.close()

    print("\nLOGIN SUCCESSFUL - AUTHENTICATION SAVED")

    yield str(AUTH_FILE)

    # TEARDOWN
    if AUTH_FILE.exists():
        AUTH_FILE.unlink()

    print("\nAUTHENTICATION STATE CLEANED")


@pytest.fixture
def logged_in_page(browser, storage_state):
    context = browser.new_context(storage_state=storage_state)

    page = context.new_page()
    page.goto(BASE_URL + "inventory.html")

    yield page

    context.close()
