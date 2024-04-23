from playwright.sync_api import Page


def test_visit_home(client: Page):
    client.goto("/")
