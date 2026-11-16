
from playwright.sync_api import Page, expect


BASE_URL = "https://www.saucedemo.com/"


# TC001 - Valid login
def test_TC001_valid_login(page: Page):

    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )


# TC002 - Invalid username
def test_TC002_invalid_username(page: Page):

    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill("wrong_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("Username and password do not match")


# TC003 - Invalid password
def test_TC003_invalid_password(page: Page):

    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("wrong_password")
    page.get_by_role("button", name="Login").click()

    expect(
        page.locator("[data-test='error']")
    ).to_be_visible()


# TC004 - Empty username
def test_TC004_empty_username(page: Page):

    page.goto(BASE_URL)

    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("Username is required")


# TC013 - Logout
def test_TC013_logout(logged_in_page: Page):

    page = logged_in_page

    page.locator("#react-burger-menu-btn").click()

    page.locator("#logout_sidebar_link").click()

    expect(
        page.get_by_placeholder("Username")
    ).to_be_visible()


# TC015 - Locked-out user
def test_TC015_locked_out_user(page: Page):

    page.goto(BASE_URL)

    page.get_by_placeholder("Username").fill("locked_out_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("locked out")
