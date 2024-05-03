from playwright.sync_api import Page, expect


def test_add_offer(client: Page, logged_in_state):
    client.get_by_test_id("add-offer-button").click()
    client.get_by_placeholder("Title").fill("Test Title")
    client.get_by_placeholder("Company").fill("Test Company")
    client.get_by_placeholder("Location").fill("Test Location")
    client.get_by_placeholder("Type").select_option("Remote")
    client.get_by_placeholder("Salary").fill("20000")
    client.get_by_placeholder("Description").fill("Test Description")
    client.get_by_placeholder("Url").fill("https://www.example.com")
    client.get_by_role("button", name="Submit").click()

    expect(client.locator(".alert")).to_contain_text("Offer added")


def test_add_offer_not_logged(client: Page):
    expect(client.get_by_test_id("login-button")).not_to_be_visible()
    client.goto("/offers/form")
    client.wait_for_url("/account/login")
