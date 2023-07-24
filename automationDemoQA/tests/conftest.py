import random
import pytest
from playwright.sync_api import Page, expect, Playwright, sync_playwright

url = "https://demoqa.com/automation-practice-form"


@pytest.fixture(scope="function")
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, slow_mo=300)
    context = browser.new_context(
        viewport={'width': 1920, 'height': 1082},
        record_video_dir="recording/demoqa"
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto(url)
    expect(page).to_have_title("DEMOQA")
    yield page
    context.tracing.stop(path="trace.zip")
    context.close()
    browser.close()
