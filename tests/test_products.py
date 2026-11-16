
from playwright.sync_api import Page, expect


def test_products_display(logged_in_page: Page):
    page = logged_in_page

    expect(page.get_by_text("Products")).to_be_visible()
    expect(page.locator(".inventory_item")).to_have_count(6)


def test_add_backpack_to_cart(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='add-to-cart-sauce-labs-backpack']"
    ).click()

    expect(page.locator(".shopping_cart_badge")).to_have_text("1")


def test_sort_products_low_to_high(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='product-sort-container']"
    ).select_option("lohi")

    prices = page.locator(".inventory_item_price").all_inner_texts()

    values = [float(p.replace("$", "")) for p in prices]

    assert values == sorted(values)


def test_sort_products_high_to_low(logged_in_page: Page):
    page = logged_in_page

    page.locator(
        "[data-test='product-sort-container']"
    ).select_option("hilo")

    prices = page.locator(".inventory_item_price").all_inner_texts()

    values = [float(p.replace("$", "")) for p in prices]

    assert values == sorted(values, reverse=True)



def test_product_details(logged_in_page: Page):

    page = logged_in_page

    page.get_by_text(
        "Sauce Labs Backpack", exact=True
    ).click()

    expect(
        page.locator("[data-test='inventory-item']")
    ).to_be_visible()
