from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()

    # open a new page
    page = context.new_page()

    # go to the url
    page.goto("https://www.saucedemo.com/")

    #  Fill an input.
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    # Click a button
    page.locator("#login-button").click()

    ph = page.locator("span[text()='Products']")

    # Pause on the following line.
    page.pause()

    assert ph.is_visible(), "User is unable to login !!"

    burger_menu = page.locator("#react-burger-menu-btn")

    # Pause on the following line.
    page.pause()

    burger_menu.click()

    logout_btn = page.locator("//div[@class='bm-menu']//a[text()='logout']")

    page.pause()

    logout_btn.click()

    login_btn = page.locator("#login-button")
    
    # test
    assert login_btn.is_visible(), "Login is not successfull!"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
