
from playwright.sync_api import Page, expect


def test_add_backpack(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_remove_backpack(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    page.locator(".shopping_cart_link").click()

    page.locator(
        "[data-test='remove-sauce-labs-backpack']"
    ).click()

    expect(page.locator(".cart_item")).to_have_count(0)


def test_cart_badge(logged_in_page: Page):
    page = logged_in_page

    products = [
        "sauce-labs-backpack",
        "sauce-labs-bike-light"
    ]

    for product in products:
        page.locator(
            f"[data-test='add-to-cart-{product}']"
        ).click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("2")
