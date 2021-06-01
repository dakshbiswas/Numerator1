import configparser
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from .BasePage import BasePage


class RecipientPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver,
        )

        self.locators = {
            'subscription_management_btn': (By.XPATH, "//div[@data-test-id='subscription-management']//div[@class='drawer-menu-item-icon']"),
            'recipient_btn': (By.XPATH, "//a[contains(text(),'Recipient')]"),
            'recipient_list_title': (By.XPATH,"//span[contains(text(),'Recipient List')]"),
            'record_count': (By.XPATH,"//div[@class='total-count']"),

            'firstColumn': (By.XPATH, "//div[contains(text(),'Recipient Name')]"),
            'secondColumn': (By.XPATH, "//div[contains(text(),'Address')]"),
            'thirdColumn': (By.XPATH, "//div[contains(text(),'Primary Phone')]"),
            'fourthColumn':(By.XPATH, "//div[contains(text(),'Backup Phone')]"),
            'fifthColumn': (By.XPATH, "//div[contains(text(),'Email')]"),
            'sixthColumn': (By.XPATH, "//div[contains(text(),'Monthly Cost')]"),
            # ----------------------------------------------------
            'firstFilterButton': (By.XPATH, "//button[@id='filter-icon-name']"),
            'secondFilterButton': (By.XPATH, "//button[@id='filter-icon-address']"),
            'thirdFilterButton': (By.XPATH, "//button[@id='filter-icon-phone_no']"),
            'fourthFilterButton':(By.XPATH, "//button[@id='filter-icon-mobile_no']"),
            'fifthFilterButton': (By.XPATH, "//button[@id='filter-icon-email']"),
            'sixthFilterButton': (By.XPATH, "//button[@id='filter-icon-monthly_cost']"),
            # -----------------------------------------------------------------------------
            'pageNumber': (By.XPATH, '//button[@id="page_no"]'),
            'pageSize': (By.XPATH, '//button[@id="page_size"]'),
            'addRecipientButton': (By.XPATH, "//button[@id='Add Recipient']"),
            'addRecipientToolTip': (By.XPATH, "//span[contains(text(),'Add Recipient')]"),
            'filterClear': (By.XPATH, "//button[@id='Clear']"),
            'filterButton': (By.XPATH, "//button[@id='Filter']"),

            'recipientNameInput': (By.XPATH, "//input[@id='Recipient Name']"),
            'addressInput': (By.XPATH, "//input[@id='Address']"),
            'primaryPhoneInput': (By.XPATH, "//input[@id='Primary Phone']"),
            'backupPhoneInput': (By.XPATH, "//input[@id='Backup Phone']"),
            'emailInput': (By.XPATH, "//input[@id='Email']"),
            'costInput': (By.XPATH, "//input[@id='monthlycost_eq']"),

            'nextPageButton': (By.XPATH, "//button[@id='Next']"),
            'pageSize25': (By.XPATH, "// button[ @ id = '25']")
        }

    def click_on_subscription_management(self):
        self.wait_until_element_clickable(self.locators.get('subscription_management_btn'))
        self.find_element(self.locators.get('subscription_management_btn')).click()

    def click_on_recipient(self):
        self.wait_until_element_clickable(self.locators.get('recipient_btn'))
        self.find_element(self.locators.get('recipient_btn')).click()
        time.sleep(4)

    def verify_recipient_page(self):
        self.wait_until_element_located(self.locators.get('recipient_list_title'))
        recipient_list_page = self.find_element(self.locators.get('recipient_list_title')).text
        assert "Recipient List" in recipient_list_page

    def verify_record_count(self):
        self.wait_until_element_located(self.locators.get('record_count'))
        recordCount = self.find_element(self.locators.get('record_count')).text
        print(recordCount)

    def verify_columns(self):
        self.wait_until_element_located(self.locators.get('firstColumn'))
        first = self.find_element(self.locators.get('firstColumn')).is_displayed()
        assert first is True
        self.wait_until_element_located(self.locators.get('secondColumn'))
        second = self.find_element(self.locators.get('secondColumn')).is_displayed()
        assert second is True
        self.wait_until_element_located(self.locators.get('thirdColumn'))
        third = self.find_element(self.locators.get('thirdColumn')).is_displayed()
        assert third is True
        self.wait_until_element_located(self.locators.get('fourthColumn'))
        fourth = self.find_element(self.locators.get('fourthColumn')).is_displayed()
        assert fourth is True
        self.wait_until_element_located(self.locators.get('fifthColumn'))
        fifth = self.find_element(self.locators.get('fifthColumn')).is_displayed()
        assert fifth is True
        self.wait_until_element_located(self.locators.get('sixthColumn'))
        sixth = self.find_element(self.locators.get('sixthColumn')).is_displayed()
        assert sixth is True

    def verify_filter_display(self):
        self.wait_until_element_located(self.locators.get('firstFilterButton'))
        firstFilter = self.find_element(self.locators.get('firstFilterButton')).is_displayed()
        assert firstFilter is True
        self.wait_until_element_located(self.locators.get('secondFilterButton'))
        secondFilter = self.find_element(self.locators.get('secondFilterButton')).is_displayed()
        assert secondFilter is True
        self.wait_until_element_located(self.locators.get('thirdFilterButton'))
        thirdFilter = self.find_element(self.locators.get('thirdFilterButton')).is_displayed()
        assert thirdFilter is True
        self.wait_until_element_located(self.locators.get('fourthFilterButton'))
        fourthFilter = self.find_element(self.locators.get('fourthFilterButton')).is_displayed()
        assert fourthFilter is True
        self.wait_until_element_located(self.locators.get('fifthFilterButton'))
        fifthFilter = self.find_element(self.locators.get('fifthFilterButton')).is_displayed()
        assert fifthFilter is True
        self.wait_until_element_located(self.locators.get('sixthFilterButton'))
        sixthFilter = self.find_element(self.locators.get('sixthFilterButton')).is_displayed()
        assert sixthFilter is True

    def page_visibilty(self):
        self.wait_until_element_located(self.locators.get('pageNumber'))
        pagenum = self.find_element(self.locators.get('pageNumber')).is_displayed()
        assert pagenum is True
        self.wait_until_element_located(self.locators.get('pageSize'))
        pages = self.find_element(self.locators.get('pageSize')).is_displayed()
        assert pages is True

    def add_visibility(self):
        self.wait_until_element_located(self.locators.get('addRecipientButton'))
        add = self.find_element(self.locators.get('addRecipientButton')).is_displayed()
        assert add is True  

    def add_visibility_hover(self):
        self.wait_until_element_clickable(self.locators.get('addRecipientButton'))
        element_to_hover_over = self.find_element(self.locators.get('addRecipientButton'))
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()
        time.sleep(1)

    def add_visibility_hover_check(self):
        self.wait_until_element_located(self.locators.get('addRecipientToolTip'))
        addPanel = self.find_element(self.locators.get('addRecipientToolTip')).is_displayed()
        assert addPanel is True

    def verify_recipient_filter(self, data):
        self.wait_until_element_clickable(self.locators.get('firstFilterButton'))
        self.find_element(self.locators.get('firstFilterButton')).click()
        self.find_element(self.locators.get('recipientNameInput')).send_keys(data)
        self.wait_until_element_clickable(self.locators.get('filterButton'))
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_clickable(self.locators.get('firstFilterButton'))
        self.find_element(self.locators.get('firstFilterButton')).click()
        self.wait_until_element_clickable(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

    def verify_address_filter(self, data):

        self.wait_until_element_clickable(self.locators.get('secondFilterButton'))
        self.find_element(self.locators.get('secondFilterButton')).click()
        self.find_element(self.locators.get('addressInput')).send_keys(data)
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('secondFilterButton'))
        self.find_element(self.locators.get('secondFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

    def verify_primary_filter(self, data):

        self.wait_until_element_located(self.locators.get('thirdFilterButton'))
        self.find_element(self.locators.get('thirdFilterButton')).click()
        self.find_element(self.locators.get('primaryPhoneInput')).send_keys(data)
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('thirdFilterButton'))
        self.find_element(self.locators.get('thirdFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

    def verify_backup_filter(self, data):

        self.wait_until_element_clickable(self.locators.get('fourthFilterButton'))
        self.find_element(self.locators.get('fourthFilterButton')).click()
        self.find_element(self.locators.get('backupPhoneInput')).send_keys(data)
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('fourthFilterButton'))
        self.find_element(self.locators.get('fourthFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

    def verify_email_filter(self, data):

        self.wait_until_element_located(self.locators.get('fifthFilterButton'))
        self.find_element(self.locators.get('fifthFilterButton')).click()
        self.find_element(self.locators.get('emailInput')).send_keys(data)
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('fifthFilterButton'))
        self.find_element(self.locators.get('fifthFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

    def verify_cost_filter(self, data):

        self.wait_until_element_clickable(self.locators.get('sixthFilterButton'))
        self.find_element(self.locators.get('sixthFilterButton')).click()
        self.find_element(self.locators.get('costInput')).send_keys(data)
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('sixthFilterButton'))
        self.find_element(self.locators.get('sixthFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

    def verify_sorting(self):
        self.wait_until_element_located(self.locators.get('firstColumn'))
        self.find_element(self.locators.get('firstColumn')).click()
        time.sleep(3)
        self.find_element(self.locators.get('firstColumn')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('secondColumn'))
        self.find_element(self.locators.get('secondColumn')).click()
        time.sleep(3)
        self.find_element(self.locators.get('secondColumn')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('thirdColumn'))
        self.find_element(self.locators.get('thirdColumn')).click()
        time.sleep(3)
        self.find_element(self.locators.get('thirdColumn')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('fourthColumn'))
        self.find_element(self.locators.get('fourthColumn')).click()
        time.sleep(3)
        self.find_element(self.locators.get('fourthColumn')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('fifthColumn'))
        self.find_element(self.locators.get('fifthColumn')).click()
        time.sleep(3)
        self.find_element(self.locators.get('fifthColumn')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('sixthColumn'))
        self.find_element(self.locators.get('sixthColumn')).click()
        time.sleep(3)
        self.find_element(self.locators.get('sixthColumn')).click()
        time.sleep(3)

    def change_page_size(self):
        self.wait_until_element_located(self.locators.get('pageSize'))
        self.find_element(self.locators.get('pageSize')).click()
        time.sleep(1)
        self.wait_until_element_located(self.locators.get('pageSize25'))
        self.find_element(self.locators.get('pageSize25')).click()
        time.sleep(3)


    def next_page_feature(self):
        self.wait_until_element_located(self.locators.get('nextPageButton'))
        self.find_element(self.locators.get('nextPageButton')).click()
