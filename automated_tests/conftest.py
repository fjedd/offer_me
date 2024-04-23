import pytest
from playwright.sync_api import Page, sync_playwright


@pytest.fixture(scope="session")
def client() -> Page:
    p = sync_playwright().start()
    browser = p.firefox.launch()
    context = browser.new_context(ignore_https_errors=True, base_url="http://app:8000")
    page = context.new_page()
    yield page
    browser.close()
