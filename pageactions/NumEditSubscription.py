import time

from selenium.webdriver.common.by import By
from .BasePage import BasePage


class NumEditSubscription(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver,
        )

        self.locators = {
            # ------------------------------------------------------
            'input_col_02': (By.XPATH, "//input[@id='textInputprovider']"),
            'input_col_01': (By.XPATH, "//input[@id='name']"),
            'input_col_03': (By.XPATH, "//input[@id='textInputrecipient']"),
            'input_col_04': (By.XPATH, "//textarea[@id='login_info']"),
            'input_col_05': (By.XPATH, "//textarea[@id='notes']"),

            # --------------------------------------------------------------
            'addTransactionButton': (By.XPATH, "//div[@class='top-tooltip']"),
            'deleteTransactionButton': (By.XPATH, "//div[@class='bottom-tooltip']"),

            'cancelButton': (By.XPATH, "//button[@id='Cancel']"),
            'saveButton': (By.XPATH, "//button[@id='Save']"),
            'first_row_data_sub': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]"),
            'duplicateText': (By.XPATH, "//div[contains(text(),'Duplicate Check: The record already exists.')]"),
        }

    def check_if_already_filled(self, id):
        self.is_loading_completed()
        self.wait_until_element_clickable(self.locators.get('input_col_'+id))
        check = self.find_element(self.locators.get('input_col_'+id)).get_attribute('value')
        assert check is not ""

    def fill_data_in_field(self, id, data):
        self.wait_until_element_clickable(self.locators.get('input_col_'+id))
        self.find_element(self.locators.get('input_col_'+id)).click()
        self.find_element(self.locators.get('input_col_' + id)).clear()
        self.find_element(self.locators.get('input_col_' + id)).send_keys(data)
        self.is_loading_completed()

    def verify_save(self, data):
        self.wait_until_element_clickable(self.locators.get('saveButton'))
        self.find_element(self.locators.get('saveButton')).click()
        self.is_loading_completed()
        self.wait_until_element_clickable(self.locators.get('first_row_data_sub'))
        check = self.find_element(self.locators.get('first_row_data_sub')).text
        assert check == data

    def verify_cancel(self, data):
        self.wait_until_element_clickable(self.locators.get('cancelButton'))
        self.find_element(self.locators.get('cancelButton')).click()
        self.is_loading_completed()
        self.wait_until_element_clickable(self.locators.get('first_row_data_sub'))
        check = self.find_element(self.locators.get('first_row_data_sub')).text
        assert check != data

    def verify_duplicate_msg(self, msg):
        self.wait_until_element_located(self.locators.get('duplicateText'))
        dup = self.find_element(self.locators.get('duplicateText')).text
        assert dup == msg

    def click_save(self):
        self.wait_until_element_clickable(self.locators.get('saveButton'))
        self.find_element(self.locators.get('saveButton')).click()
        self.is_loading_completed()