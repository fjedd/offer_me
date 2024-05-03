import pytest
from playwright.sync_api import (
    Browser,
    BrowserContext,
    Page,
    Playwright,
    sync_playwright,
)


@pytest.fixture(scope="session")
def playwright_setup() -> Browser:
    p: Playwright = sync_playwright().start()
    browser: Browser = p.firefox.launch()
    yield browser
    browser.close()
    p.stop()


@pytest.fixture()
def client(playwright_setup: Browser) -> Page:
    context: BrowserContext = playwright_setup.new_context(
        ignore_https_errors=True, base_url="http://app:8000"
    )
    page: Page = context.new_page()
    page.goto("/")
    yield page


@pytest.fixture
def logged_in_state(client: Page) -> None:
    client.goto("/account/login")
    client.get_by_label("Username").fill("testuser1")
    client.get_by_label("Password").fill("test_password")
    client.get_by_role("button", name="Login").click()
    client.context.storage_state(path=".auth/state.json")
