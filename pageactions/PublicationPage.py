import configparser
import time

from selenium.webdriver.common.by import By

from .BasePage import BasePage


class PublicationPage(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver,
        )

        self.locators = {
            'subscription_management_btn': (By.XPATH, "//div[@data-test-id='subscription-management']//div[@class='drawer-menu-item-icon']"),
            'publication_btn': (By.XPATH, "//a[normalize-space()='Publication']"),
            'publication_list_title': (By.XPATH,"//span[normalize-space()='Publication List']"),
            'record_count': (By.XPATH,"//div[@class='total-count']"),
            'firstColumn': (By.XPATH, "//div[contains(text(),'Publication Code')]"),
            'secondColumn': (By.XPATH, "//div[contains(text(),'Publication Name')]"),
            'thirdColumn': (By.XPATH, "//div[contains(text(),'Created On')]"),
            'fourthColumn': (By.XPATH, "//div[contains(text(),'Created By')]"),
            'fifthColumn': (By.XPATH, "//div[contains(text(),'Modified On')]"),
            'sixthColumn': (By.XPATH, "//div[contains(text(),'Modified By')]"),
            # ----------------------------------------------------
            'firstFilterButton': (By.XPATH, "//button[@id='filter-icon-code']"),
            'secondFilterButton': (By.XPATH, "//button[@id='filter-icon-name']"),
            'thirdFilterButton': (By.XPATH, "//button[@id='filter-icon-created_on']"),
            'fourthFilterButton': (By.XPATH, "//button[@id='filter-icon-created_by__name']"),
            'fifthFilterButton': (By.XPATH, "//button[@id='filter-icon-modified_on']"),
            'sixthFilterButton': (By.XPATH, "//button[@id='filter-icon-modified_by__name']"),
            # -----------------------------------------------------------------------------
            'pageNumber': (By.XPATH, '//button[@id="page_no"]'),
            'pageSize': (By.XPATH, '//button[@id="page_size"]'),
            'addPublicationButton': (By.XPATH, '//button[@id="Add Publication"]'),
            'addPublicationSidePanel': (By.XPATH, ' //div[@class="side-panel-header"]'),
            'publicationCodeInput': (By.XPATH, "//input[@id='Publication Code']"),
            'publicationNameInput': (By.XPATH, "//input[@id='Publication Name']"),
            'filterClear': (By.XPATH, "//button[@id='Clear']"),
            'createdOnInput': (By.XPATH, "//input[@id='createdon_eq']"),
            'createdByInput': (By.XPATH, "//input[@id='Created By']"),
            'modifiedByInput': (By.XPATH, " //input[@id='Modified By']"),
            'createdOnDate': (By.XPATH, "//span[@aria-label='April 26, 2021']"),
            'filterButton': (By.XPATH, "//button[@id='Filter']"),
            'modifiedOn': (By.XPATH, "//input[@id='modifiedon_eq']"),
            'modifiedDate': (By.XPATH, "//span[contains(text(),'26')]"),
            'nextPageButton': (By.XPATH, "//button[@id='Next']"),
            'pageSize25': (By.XPATH, "// button[ @ id = '25']")
        }

        # self.parser = configparser.RawConfigParser()
        # self.parser.read('properties/config.properties')
        # self.email = self.parser.get('config', 'config.EMAIL')
        # self.password = self.parser.get('config', 'config.PASSWORD')

    def click_on_subscription_management(self):
        self.wait_until_element_clickable(self.locators.get('subscription_management_btn'))
        self.find_element(self.locators.get('subscription_management_btn')).click()

    def click_on_publication(self):
        self.wait_until_element_clickable(self.locators.get('publication_btn'))
        self.find_element(self.locators.get('publication_btn')).click()
        time.sleep(3)

    def verify_publication_page(self):
        self.wait_until_element_located(self.locators.get('publication_list_title'))
        publication_list_page = self.find_element(self.locators.get('publication_list_title')).text
        assert "Publication List" in publication_list_page

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
        self.wait_until_element_located(self.locators.get('pageSize'))
        pages = self.find_element(self.locators.get('pageSize')).is_displayed()
        assert pages is True

    def add_visibility(self):
        self.wait_until_element_located(self.locators.get('addPublicationButton'))
        add = self.find_element(self.locators.get('addPublicationButton')).is_displayed()
        assert add is True

    def add_visibility_click(self):
        self.wait_until_element_clickable(self.locators.get('addPublicationButton'))
        add = self.find_element(self.locators.get('addPublicationButton')).click()
        time.sleep(1)

    def add_tool_visibility(self):
        self.wait_until_element_located(self.locators.get('addPublicationSidePanel'))
        addPanel = self.find_element(self.locators.get('addPublicationSidePanel')).is_displayed()
        assert addPanel is True

    def verify_filter_functionality(self):
        self.wait_until_element_clickable(self.locators.get('firstFilterButton'))
        self.find_element(self.locators.get('firstFilterButton')).click()
        self.find_element(self.locators.get('publicationCodeInput')).send_keys("Code")
        self.wait_until_element_clickable(self.locators.get('filterButton'))
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_clickable(self.locators.get('firstFilterButton'))
        self.find_element(self.locators.get('firstFilterButton')).click()
        self.wait_until_element_clickable(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()

        time.sleep(3)
        self.wait_until_element_clickable(self.locators.get('secondFilterButton'))
        self.find_element(self.locators.get('secondFilterButton')).click()
        self.find_element(self.locators.get('publicationNameInput')).send_keys("test")
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('secondFilterButton'))
        self.find_element(self.locators.get('secondFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('thirdFilterButton'))
        self.find_element(self.locators.get('thirdFilterButton')).click()
        self.find_element(self.locators.get('createdOnInput')).click()
        self.find_element(self.locators.get('createdOnDate')).click()
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('thirdFilterButton'))
        self.find_element(self.locators.get('thirdFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

        self.wait_until_element_clickable(self.locators.get('fourthFilterButton'))
        self.find_element(self.locators.get('fourthFilterButton')).click()
        self.find_element(self.locators.get('createdByInput')).send_keys("admin")
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('fourthFilterButton'))
        self.find_element(self.locators.get('fourthFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

        self.wait_until_element_located(self.locators.get('fifthFilterButton'))
        self.find_element(self.locators.get('fifthFilterButton')).click()
        self.find_element(self.locators.get('modifiedOn')).click()
        self.find_element(self.locators.get('modifiedDate')).click()
        self.find_element(self.locators.get('filterButton')).click()
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('fifthFilterButton'))
        self.find_element(self.locators.get('fifthFilterButton')).click()
        self.wait_until_element_located(self.locators.get('filterClear'))
        self.find_element(self.locators.get('filterClear')).click()
        time.sleep(3)

        self.wait_until_element_clickable(self.locators.get('sixthFilterButton'))
        self.find_element(self.locators.get('sixthFilterButton')).click()
        self.find_element(self.locators.get('modifiedByInput')).send_keys("admin")
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
        time.sleep(3)
        self.wait_until_element_located(self.locators.get('pageSize25'))
        self.find_element(self.locators.get('pageSize25')).click()
        time.sleep(3)


    def next_page_feature(self):
        self.wait_until_element_located(self.locators.get('nextPageButton'))
        self.find_element(self.locators.get('nextPageButton')).click()
