# encoding: UTF-8

from playwright.sync_api import Page, expect
import time
import names


class Actionwords:
    def __init__(self, page):
        self.page = page
        self.region = None
        self.password = None
        self.user = None

    def set_user_details(self, username, password):
        self.user = username
        self.password = password

    def i_login_to_salesloft(self):
        page = self.page

        page.goto('https://app.salesloft.com/app/dashboard')

        next_button = page.locator("text=Next")
        expect(next_button).to_be_visible()

        page.screenshot(path=f'salesloft.png')
        page.locator("[placeholder=\"Email Address\"]").click()
        page.locator("[placeholder=\"Email Address\"]").fill(self.user)
        page.locator("text=Next").click()
        page.locator("[placeholder=\"Password\"]").fill(self.password)
        page.locator("text=Sign In").click()

    def create_a_new_person(self):
        page = self.page

        name = names.get_first_name()
        surname = names.get_last_name()

        page.locator("[aria-label=\"Navigate to People\"] path").click()
        page.locator("button:has-text(\"Create People\")").click()
        page.locator("text=Create Person").click()

        page.locator("[aria-label=\"Person email address\"]").fill(f"{name}.{surname}@salesloft.com")
        page.locator("[aria-label=\"first name\"]").click()
        page.locator("[aria-label=\"first name\"]").fill(name)
        # Press Tab
        page.locator("[aria-label=\"first name\"]").press("Tab")
        # Fill [aria-label="last name"]
        page.locator("[aria-label=\"last name\"]").fill(surname)
        # Click button:has-text("Create Person")
        page.locator("button:has-text(\"Create Person\")").click()

        time.sleep(3)
        print('see me')
