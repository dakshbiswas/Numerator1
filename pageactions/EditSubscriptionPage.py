import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

from .BasePage import BasePage


class EditSubscriptionPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver,
        )

        self.locators = {
            'subscription_management_btn': (By.XPATH, "//div[@data-test-id='subscription-management']//div[@class='drawer-menu-item-icon']"),
            'subscription_btn': (By.XPATH, "//a[contains(text(),'Subscription')]"),
            'edit_subscription_title': (By.XPATH, "//span[contains(text(),'Edit Subscription')]"),
            'recordTest': (By.XPATH, "//span[@class ='grid-cell-text ' and text()='test ned']"),
            'recordTestCancel': (By.XPATH, "//span[@class ='grid-cell-text ' and text()='test nedu']"),
            # ------------------------------------------------------
            'providerName': (By.XPATH, "//input[@id='textInputprovider']"),
            'subscriptionName': (By.XPATH, "//input[@id='name']"),
            'recipientName': (By.XPATH, "//input[@id='textInputrecipient']"),
            'loginInfo': (By.XPATH, "//textarea[@id='login_info']"),
            'notes': (By.XPATH, "//textarea[@id='notes']"),
            'firstSubName': (By.XPATH, "//span[@class='grid-cell-text ' and text()='test ned']"),
            'firstSubNameAfterSave': (By.XPATH, "//span[@class='grid-cell-text ' and text()='test nedd']"),

            'transactionDateColumn': (By.XPATH, "//th[contains(text(),'Transaction Date')]"),
            'startDateColumn': (By.XPATH, "//th[contains(text(),'Start Date')]"),
            'endDateColumn': (By.XPATH, "//th[contains(text(),'End Date')]"),
            'amountColumn': (By.XPATH, "//th[contains(text(),'Amount')]"),
            'transactionTypeColumn': (By.XPATH, "//th[contains(text(),'Transaction Type')]"),
            'notesColumn': (By.XPATH, "//th[contains(text(),'Notes')]"),
            'recipientColumn': (By.XPATH, "//th[contains(text(),'Recipient')]"),
            # --------------------------------------------------------------
            'addTransactionButton': (By.XPATH, "//div[@class='top-tooltip']"),
            'deleteTransactionButton': (By.XPATH, "//div[@class='bottom-tooltip']"),
            'cancelButton': (By.XPATH, "//button[@id='Cancel']"),
            'saveButton': (By.XPATH, "//button[@id='Save']"),
            'duplicateText': (By.XPATH, "//div[contains(text(),'Duplicate Check: The record already exists.')]")
        }

    def click_on_subscription_management(self):
        self.wait_until_element_clickable(self.locators.get('subscription_management_btn'))
        self.find_element(self.locators.get('subscription_management_btn')).click()

    def click_on_subscription(self):
        self.wait_until_element_clickable(self.locators.get('subscription_btn'))
        self.find_element(self.locators.get('subscription_btn')).click()
        time.sleep(4)

    def click_on_record(self):
        self.wait_until_element_clickable(self.locators.get('recordTest'))
        source=self.find_element(self.locators.get('recordTest'))
        action = ActionChains(self.driver)
        action.double_click(source).perform()
        time.sleep(2)

    def verify_edit_page(self):
        self.wait_until_element_located(self.locators.get('edit_subscription_title'))
        res = self.find_element(self.locators.get('edit_subscription_title')).is_displayed()
        assert res is True

    def verify_filled_data(self, test):

        self.wait_until_element_located(self.locators.get('subscriptionName'))
        time.sleep(3)
        textResult = self.find_element(self.locators.get('subscriptionName')).text
        assert textResult in test

    def verify_all_fields(self):
        self.wait_until_element_located(self.locators.get('providerName'))
        first = self.find_element(self.locators.get('providerName')).is_displayed()
        assert first is True
        self.wait_until_element_located(self.locators.get('recipientName'))
        second = self.find_element(self.locators.get('recipientName')).is_displayed()
        assert second is True
        self.wait_until_element_located(self.locators.get('loginInfo'))
        third = self.find_element(self.locators.get('loginInfo')).is_displayed()
        assert third is True
        self.wait_until_element_located(self.locators.get('notes'))
        fourth = self.find_element(self.locators.get('notes')).is_displayed()
        assert fourth is True

    def verify_transaction_grid(self):
        self.wait_until_element_located(self.locators.get('transactionDateColumn'))
        first = self.find_element(self.locators.get('transactionDateColumn')).is_displayed()
        assert first is True
        self.wait_until_element_located(self.locators.get('startDateColumn'))
        second = self.find_element(self.locators.get('startDateColumn')).is_displayed()
        assert second is True
        self.wait_until_element_located(self.locators.get('endDateColumn'))
        third = self.find_element(self.locators.get('endDateColumn')).is_displayed()
        assert third is True
        self.wait_until_element_located(self.locators.get('amountColumn'))
        fourth = self.find_element(self.locators.get('amountColumn')).is_displayed()
        assert fourth is True
        self.wait_until_element_located(self.locators.get('transactionTypeColumn'))
        fifth = self.find_element(self.locators.get('transactionTypeColumn')).is_displayed()
        assert fifth is True
        self.wait_until_element_located(self.locators.get('notesColumn'))
        sixth = self.find_element(self.locators.get('notesColumn')).is_displayed()
        assert sixth is True
        self.wait_until_element_located(self.locators.get('recipientColumn'))
        seventh = self.find_element(self.locators.get('recipientColumn')).is_displayed()
        assert seventh is True

    def verify_saveCancel(self):
        self.wait_until_element_located(self.locators.get('cancelButton'))
        cancel = self.find_element(self.locators.get('cancelButton')).is_displayed()
        assert cancel is True
        self.wait_until_element_located(self.locators.get('saveButton'))
        save = self.find_element(self.locators.get('saveButton')).is_displayed()
        assert save is True

    def verify_edit(self, test):
        self.wait_until_element_located(self.locators.get('subscriptionName'))
        self.find_element(self.locators.get('subscriptionName')).send_keys(test)
        time.sleep(2)

    def verify_cancel(self):
        self.wait_until_element_located(self.locators.get('cancelButton'))
        self.find_element(self.locators.get('cancelButton')).click()
        time.sleep(2)

    def enter_duplicate_data(self, data):
        self.wait_until_element_located(self.locators.get('subscriptionName'))
        self.find_element(self.locators.get('subscriptionName')).clear()
        self.find_element(self.locators.get('subscriptionName')).send_keys(data)
        time.sleep(1)
        self.wait_until_element_located(self.locators.get('saveButton'))
        self.find_element(self.locators.get('saveButton')).click()
        time.sleep(2)

    def verify_duplicate_msg(self, msg):
        self.wait_until_element_located(self.locators.get('duplicateText'))
        dup = self.find_element(self.locators.get('duplicateText')).is_displayed()
        assert dup is True

    def enter_new_subName(self, data):
        self.wait_until_element_located(self.locators.get('subscriptionName'))
        self.find_element(self.locators.get('subscriptionName')).clear()
        self.find_element(self.locators.get('subscriptionName')).send_keys(data)

    def enter_new_proName(self, data):
        self.wait_until_element_located(self.locators.get('providerName'))
        self.find_element(self.locators.get('providerName')).clear()
        self.find_element(self.locators.get('providerName')).send_keys(data)

    def enter_new_recName(self, data):
        self.wait_until_element_located(self.locators.get('recipientName'))
        self.find_element(self.locators.get('recipientName')).clear()
        self.find_element(self.locators.get('recipientName')).send_keys(data)

    def enter_new_info(self, data):
        self.wait_until_element_located(self.locators.get('loginInfo'))
        self.find_element(self.locators.get('loginInfo')).clear()
        self.find_element(self.locators.get('loginInfo')).send_keys(data)

    def enter_new_notes(self, data):
        self.wait_until_element_located(self.locators.get('notes'))
        self.find_element(self.locators.get('notes')).clear()
        self.find_element(self.locators.get('notes')).send_keys(data)

    def save_and_verify(self, data):
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('saveButton'))
        self.find_element(self.locators.get('saveButton')).click()
        time.sleep(5)
        self.wait_until_element_located(self.locators.get('firstSubNameAfterSave'))
        textResult = self.find_element(self.locators.get('firstSubNameAfterSave')).text
        assert textResult in data


