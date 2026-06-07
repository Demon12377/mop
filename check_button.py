from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto('http://localhost:3000/mop/feral_druid/')

    # Wait for the page to load
    page.wait_for_selector('.bulk-tab-tab')
    page.click('.bulk-tab-tab')

    # Check for the Import Favorites button
    button = page.get_by_role("button", name="Import Favorites")
    if button.is_visible():
        print("Import Favorites button is visible")
        button.screenshot(path="import_favorites_button.png")
    else:
        print("Import Favorites button is NOT visible")
        page.screenshot(path="error_bulk_tab.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)
