
from playwright.sync_api import Page, expect


def test_complete_checkout(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    page.locator(".shopping_cart_link").click()

    page.get_by_role("button", name="Checkout").click()

    page.get_by_placeholder("First Name").fill("Jag")
    page.get_by_placeholder("Last Name").fill("Dhakshinamoorthy")
    page.get_by_placeholder("Zip/Postal Code").fill("600001")

    page.get_by_role("button", name="Continue").click()

    page.get_by_role("button", name="Finish").click()

    expect(
        page.get_by_text("Thank you for your order!")
    ).to_be_visible()


def test_checkout_missing_details(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    page.locator(".shopping_cart_link").click()

    page.get_by_role("button", name="Checkout").click()

    page.get_by_role("button", name="Continue").click()

    expect(
        page.locator("[data-test='error']")
    ).to_contain_text("First Name is required")
