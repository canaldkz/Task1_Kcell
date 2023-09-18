import datetime

from selenium.webdriver import Keys, Chrome
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from models.Page import Page


class Locator:
    FIRST_NAME = '//input[@id="firstName"]'
    LAST_NAME = '//input[@id="lastName"]'
    USER_EMAIL = '//input[@id="userEmail"]'
    GENDER_INPUTS = '//input[contains(@id, "gender-radio")]'
    GENDER_LABELS = '//label[contains(@for, "gender-radio")]'
    USER_NUMBER = '//input[@id="userNumber"]'
    USER_DOB = '//input[@id="dateOfBirthInput"]'
    SUBJECT = '//input[@id="subjectsInput"]'
    HOBBIE_CHECKBOXES = '//input[contains(@id, "hobbies-checkbox")]'
    HOBBIE_LABELS = '//label[contains(@for, "hobbies-checkbox")]'
    FILE_INPUT = '//input[@id="uploadPicture"]'
    ADDRESS = '//textarea[@id="currentAddress"]'
    STATE = '//input[@id="react-select-3-input"]'
    CITY = '//input[@id="react-select-4-input"]'

    SUBMIT = '//button[@id="submit"]'

    MODAL = '//div[@id="example-modal-sizes-title-lg"]'
    MODAL_ROWS = '//div[@role="dialog"]//td[2]'


class FormPage(Page):
    def __init__(self, browser: Chrome):
        super().__init__(browser)
        self.browser = browser

    def complete_values(
        self,
        first_name: str,
        last_name: str,
        email: str,
        gender: str,
        number: str,
        date_of_birth: datetime.date,
        subject: str,
        hobbies: list,
        picture_path: str,
        address: str,
        state: str,
        city: str,
    ):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_email(email)
        self.set_gender(gender)
        self.set_number(number)
        self.set_dob(date_of_birth)
        self.set_subject(subject)
        self.set_hobbies(hobbies)
        self.set_picture(picture_path)
        self.set_address(address)
        self.set_state(state)
        self.set_city(city)

        self.submit()

        try:
            WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable(self.browser.find_element(By.XPATH, Locator.MODAL)))
            return self.collect_data()
        except:
            return False

    def set_first_name(self, first_name: str):
        self.browser.find_element(By.XPATH, Locator.FIRST_NAME).send_keys(first_name)

    def set_last_name(self, last_name: str):
        self.browser.find_element(By.XPATH, Locator.LAST_NAME).send_keys(last_name)

    def set_email(self, email: str):
        self.browser.find_element(By.XPATH, Locator.USER_EMAIL).send_keys(email)

    def set_gender(self, gender: str):
        gender_inputs = self.browser.find_elements(By.XPATH, Locator.GENDER_LABELS)
        for g in gender_inputs:
            if g.text == gender:
                self.scroll_to_elem(g)
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(g)).click()

    def set_number(self, number: str):
        self.browser.find_element(By.XPATH, Locator.USER_NUMBER).send_keys(number)

    def set_dob(self, date: datetime.date):
        dob_input = self.browser.find_element(By.XPATH, Locator.USER_DOB)
        dob_input.send_keys(Keys.CONTROL + "a")
        dob_input.send_keys(date.strftime("%m.%d.%Y"))
        dob_input.send_keys(Keys.ENTER)

    def set_subject(self, subject: str):
        subject_input = self.browser.find_element(By.XPATH, Locator.SUBJECT)
        subject_input.send_keys(subject)
        subject_input.send_keys(Keys.ENTER)


    def set_hobbies(self, hobbies: list[str]):
        hobbies_chechboxes = self.browser.find_elements(
            By.XPATH, Locator.HOBBIE_LABELS
        )
        for h in hobbies_chechboxes:
            if h.text in hobbies:
                self.scroll_to_elem(h)
                WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(h)).click()

    def set_picture(self, path: str):
        self.browser.find_element(By.XPATH, Locator.FILE_INPUT).send_keys(path)

    def set_address(self, address: str):
        self.browser.find_element(By.XPATH, Locator.ADDRESS).send_keys(address)

    def set_state(self, state: str):
        state_input = self.browser.find_element(By.XPATH, Locator.STATE)
        state_input.send_keys(state)
        state_input.send_keys(Keys.ENTER)

    def set_city(self, city: str):
        state_input = self.browser.find_element(By.XPATH, Locator.CITY)
        state_input.send_keys(city)
        state_input.send_keys(Keys.ENTER)

    def submit(self):
        submit_btn = self.browser.find_element(By.XPATH, Locator.SUBMIT)
        self.scroll_to_elem(submit_btn)
        WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable(submit_btn)).click()

    def collect_data(self):
        rows = self.browser.find_elements(By.XPATH, Locator.MODAL_ROWS)
        return rows