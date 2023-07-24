from playwright.sync_api import Page, expect


class FormPage:

    def __init__(self, page):
        self.page = page
        self.name = page.locator("#firstName")
        self.lastname = page.locator("#lastName")
        self.email = page.locator("#userEmail")
        self.gender = page.locator("label[for='gender-radio-1']")
        self.mobile = page.locator("#userNumber")
        self.date = page.locator("#dateOfBirthInput")
        self.subjects = page.locator("#subjectsInput")
        self.upload = page.locator("#uploadPicture")
        self.address = page.locator("#currentAddress")
        self.submit = page.locator("#submit")
        self.thanks = page.locator("#example-modal-sizes-title-lg")

    def Scroll_x(self, x, y):
        self.page.mouse.wheel(x, y)

    def enter_name(self, text, ruta):
        t = self.name
        expect(t).to_be_visible()
        t.highlight()
        t.fill(text)
        self.page.screenshot(path=ruta)

    def enter_lastname(self, text, ruta):
        t = self.lastname
        expect(t).to_be_visible()
        t.highlight()
        t.fill(text)
        self.page.screenshot(path=ruta)

    def enter_email(self, text, ruta):
        t = self.email
        expect(t).to_be_visible()
        t.highlight()
        t.fill(text)
        self.page.screenshot(path=ruta)

    def click_gender(self, ruta):
        t = self.gender
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.page.screenshot(path=ruta)

    def enter_mobile(self, text, ruta):
        t = self.mobile
        expect(t).to_be_visible()
        t.highlight()
        t.fill(text)
        self.page.screenshot(path=ruta)

    def enter_date(self, ruta):
        t = self.date
        expect(t).to_be_visible()
        t.highlight()
        t.click()
        self.page.keyboard.press('Enter')
        self.page.screenshot(path=ruta)

    def enter_subjects(self, subject1, subject2, subject3, ruta):
        t = self.subjects
        expect(t).to_be_visible()
        t.highlight()
        t.fill(subject1)
        self.page.keyboard.press('Enter')
        t.fill(subject2)
        self.page.keyboard.press('Enter')
        t.fill(subject3)
        self.page.keyboard.press('Enter')
        self.page.screenshot(path=ruta)

    def enter_hobbies(self, ruta):
        sports = self.page.locator("label[for='hobbies-checkbox-1']")
        music = self.page.locator("label[for='hobbies-checkbox-2']")
        sports.click()
        music.click()
        self.page.screenshot(path=ruta)

    def enter_upload(self, document, ruta):
        t = self.upload
        t.highlight()
        expect(t).to_be_visible()
        t.set_input_files(document)
        self.page.screenshot(path=ruta)

    def enter_address(self, text, ruta):
        t = self.address
        t.highlight()
        expect(t).to_be_visible()
        t.fill(text)
        self.page.screenshot(path=ruta)

    def enter_state_city(self, ruta):
        state = self.page.locator("#react-select-3-input")
        city = self.page.locator("#react-select-4-input")
        state.fill("Haryana")
        self.page.keyboard.press('Enter')
        city.fill("Panipat")
        self.page.keyboard.press('Enter')
        self.page.screenshot(path=ruta)

    def click_submit(self, ruta):
        t = self.submit
        expect(t).to_be_visible()
        expect(t).to_be_enabled()
        t.highlight()
        t.click()
        self.page.screenshot(path=ruta)

    def assert_text(self, text, ruta):
        t = self.thanks
        t.highlight()
        expect(t).to_contain_text(text)
        self.page.screenshot(path=ruta)
