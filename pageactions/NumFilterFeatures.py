import time

from pageactions.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class NumFilterFeatures(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

        self.locators = {
            # Subscription Grid Filter --Start
            'publicatn_filter_01': (By.XPATH, "//button[@id='filter-icon-code']"),
            'publicatn_filter_02': (By.XPATH, "//button[@id='filter-icon-name']"),
            'publicatn_filter_03': (By.XPATH, "//button[@id='filter-icon-created_on']"),
            'publicatn_filter_04': (By.XPATH, "//button[@id='filter-icon-created_by__name']"),
            'publicatn_filter_05': (By.XPATH, "//button[@id='filter-icon-modified_on']"),
            'publicatn_filter_06': (By.XPATH, "//button[@id='filter-icon-modified_by__name']"),

            'publicatn_filter_input_02': (By.XPATH, "//input[@id='Publication Name']"),
            'publicatn_filter_input_01': (By.XPATH, "//input[@id='Publication Code']"),
            'publicatn_filter_input_03': (By.XPATH, "//input[@id='createdon_eq']"),
            'publicatn_filter_input_04': (By.XPATH, "//input[@id='Created By']"),
            'publicatn_filter_input_05': (By.XPATH, "//input[@id='modifiedon_eq']"),
            'publicatn_filter_input_06': (By.XPATH, "//input[@id='Modified By']"),

            # Subscription Grid Filter --End

            # ----------------------------------------------------
            'recipient_filter_01': (By.XPATH, "//button[@id='filter-icon-name']"),
            'recipient_filter_02': (By.XPATH, "//button[@id='filter-icon-address']"),
            'recipient_filter_03': (By.XPATH, "//button[@id='filter-icon-phone_no']"),
            'recipient_filter_04': (By.XPATH, "//button[@id='filter-icon-mobile_no']"),
            'recipient_filter_05': (By.XPATH, "//button[@id='filter-icon-email']"),
            'recipient_filter_06': (By.XPATH, "//button[@id='filter-icon-monthly_cost']"),
            # -----------------------------------------------------------------------------

            'recipient_filter_input_01': (By.XPATH, "//input[@id='Recipient Name']"),
            'recipient_filter_input_02': (By.XPATH, "//input[@id='Address']"),
            'recipient_filter_input_03': (By.XPATH, "//input[@id='Primary Phone']"),
            'recipient_filter_input_04': (By.XPATH, "//input[@id='Backup Phone']"),
            'recipient_filter_input_05': (By.XPATH, "//input[@id='Email']"),
            'recipient_filter_input_06': (By.XPATH, "//input[@id='monthlycost_eq']"),

            'filter_btn': (By.ID, "Filter"),
            'filter_clear_btn': (By.ID, "Clear"),
        }

    def clickFilterIconOnPublicationGrid(self, id, value):
        self.wait_until_element_clickable(self.locators.get('publicatn_filter_' + id)).click()
        self.wait_until_element_clickable(self.locators.get('publicatn_filter_input_' + id))
        self.find_element(self.locators.get('publicatn_filter_input_' + id)).clear()
        self.find_element(self.locators.get('publicatn_filter_input_' + id)).send_keys(value)

    def clickFilterButtonOnPublicationGrid(self):
        self.wait_until_element_clickable(self.locators.get('filter_btn'))
        self.find_element(self.locators.get('filter_btn')).click()
        self.is_loading_completed()

    def clearFilterOnPublicationGrid(self):
        self.wait_until_element_clickable(self.locators.get('filter_clear_btn'))
        self.find_element(self.locators.get('filter_clear_btn')).click()
        self.wait_until_element_is_invisible(self.locators.get('filter_clear_btn'))

    def clickFilterButtonOnColPublicationGrid(self, id):
        self.wait_until_element_clickable(self.locators.get('publicatn_filter_' + id)).click()

    def downEnter(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.DOWN).perform()
        time.sleep(1)
        actions.send_keys(Keys.RETURN).perform()

    def clickOnDateButton(self, id):
        self.wait_until_element_clickable(self.locators.get('publicatn_filter_input_'+id))
        self.find_element(self.locators.get('publicatn_filter_input_'+id)).click()

    # ==========================================================================

    def clickFilterIconOnRecipientGrid(self, id, value):
        self.wait_until_element_clickable(self.locators.get('recipient_filter_' + id)).click()
        self.wait_until_element_clickable(self.locators.get('recipient_filter_input_' + id))
        self.find_element(self.locators.get('recipient_filter_input_' + id)).clear()
        self.find_element(self.locators.get('recipient_filter_input_' + id)).send_keys(value)

    def clickFilterButtonOnColRecipientGrid(self, id):
        self.wait_until_element_clickable(self.locators.get('recipient_filter_' + id)).click()