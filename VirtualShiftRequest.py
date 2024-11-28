from playwright.sync_api import sync_playwright
import re
from playwright.sync_api import Playwright, sync_playwright, expect

from playwright_stealth import stealth_sync

# data
sede = "Suba - Calle 145 #85-52 - DB01"
first_name = "Pedro"
last_name = "Pérezzz"
id_type = "Cédula"
id_number = "123456789"
phone = "1234567"
email = "a@b.com"
row = "Atención General"

# page
url = "https://qanty.com/portals/tickets?c=8lqYpCcK4GuXJKm7gKzr"


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Apply the stealth settings
        # stealth_sync(page) -- No sirvió

        page.goto(url)
        
        page.locator("[id=\"__BVID__26\"]").select_option(sede)
        
        page.locator("#name-input").click()
        page.locator("#name-input").fill(first_name)
        page.locator("#name-input").press("Tab")
        
        page.locator("#last-name-input").fill(last_name)
        
        page.locator("[id=\"__BVID__32\"]").get_by_role("combobox").locator("div").filter(has_text="Escriba algo").click()
        #page.get_by_role("option", name="Cédula", exact=True).locator("span").first.click()
        page.get_by_text("Cédula", exact=True).click()
        
        page.locator("#doc-number-input").click()
        page.locator("#doc-number-input").fill(id_number)
        
        page.locator("#phone-number-input").click()
        page.locator("#phone-number-input").fill(phone)
        
        page.locator("#email-input").click()
        page.locator("#email-input").fill(email)
        
        page.locator("[id=\"__BVID__43\"]").select_option("[object Object]")

        page.get_by_role("button", name="Pedir un turno").click()

        page.wait_for_timeout(10000)

        # ---------------------
        browser.close()

if __name__ == "__main__":
    run()