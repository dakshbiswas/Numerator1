import time

from selenium.webdriver.common.action_chains import ActionChains

from pageactions.BasePage import BasePage
from selenium.webdriver.common.by import By

class NumConfigs(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

        self.locators = {
            'subscription_mgmt': (By.XPATH, "//div[@data-test-id='subscription-management']//"
                                            "div[@class='drawer-menu-item-icon']//*[local-name()='svg']//"
                                            "*[name()='path' and contains(@fill,'currentCol')]"),
            'subscription_mgmt_01': (By.LINK_TEXT, "Publication"),
            'subscription_mgmt_02': (By.LINK_TEXT, "Source"),
            'subscription_mgmt_03': (By.LINK_TEXT, "Provider"),
            'subscription_mgmt_04': (By.LINK_TEXT, "Recipient"),
            'subscription_mgmt_05': (By.LINK_TEXT, "Subscription"),

            'in_subscription_01': (By.XPATH, "//div[contains(text(),'Publication Code')]"),
            'in_subscription_02': (By.XPATH, "//div[contains(text(),'Publication Name')]"),
            'in_subscription_03': (By.XPATH, "//div[contains(text(),'Created On')]"),
            'in_subscription_04': (By.XPATH, "//div[contains(text(),'Created By')]"),
            'in_subscription_05': (By.XPATH, "//div[contains(text(),'Modified On')]"),
            'in_subscription_06': (By.XPATH, "//div[contains(text(),'Modified By')]"),

            'publication_list_title': (By.XPATH, "//span[normalize-space()='Publication List']"),
            'first_record': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]"),
            'total_count': (By.XPATH, "//div[@class='total-count']"),
            'pageSize': (By.XPATH, '//button[@id="page_size"]'),
            'pagination': (By.ID, "page_no"),
            'pageSize_25': (By.XPATH, "//button[@id='25']"),
            'pageSize_50': (By.XPATH, "//button[@id='50']"),
            'pageSize_75': (By.XPATH, "//button[@id='75']"),
            'pageSize_100': (By.XPATH, "//button[@id='100']"),
            'page_size_len_05': (By.XPATH, "//div[@class='grid-row ']"),

            'addPublicationButton': (By.XPATH, '//button[@id="Add Publication"]'),
            'addPublicationTool': (By.XPATH, "//span[contains(text(),'Add Publication')]"),
            'publicatn_data_row_01': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]"),
            'publicatn_data_row_02': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]"),
            'publicatn_data_row_03': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[1]"),
            'publicatn_data_row_04': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/span[1]"),
            'publicatn_data_row_05': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/span[1]"),
            'publicatn_data_row_06': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]/span[1]"),

            # ===========================================================================
            # Edit subscription starts

            'first_row_data_sub': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]"),
            'edit_subscription_title': (By.XPATH, "//span[contains(text(),'Edit Subscription')]"),

            # Edit subscription ends
            # ===========================================================================

            # Recipient grid starts
            'recipient_list_title': (By.XPATH,"//span[contains(text(),'Recipient List')]"),
            'addRecipientButton': (By.XPATH, "//button[@id='Add Recipient']"),
            'addRecipientToolTip': (By.XPATH, "//span[contains(text(),'Add Recipient')]"),
            'recipient_data_row_01': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/span[1]"),
            'recipient_data_row_02': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/span[1]"),
            'recipient_data_row_03': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/span[1]"),
            'recipient_data_row_04': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[1]/span[1]"),
            'recipient_data_row_05': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/span[1]"),
            'recipient_data_row_06': (By.XPATH, "//body/div[@id='root']/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[6]/div[1]/span[1]"),
        }

    def click_on_subscription_management(self):
        self.wait_until_element_clickable(self.locators.get('subscription_mgmt'))
        self.find_element(self.locators.get('subscription_mgmt')).click()

    def subscription_mgmt_option(self, id):
        self.wait_until_element_clickable(self.locators.get('subscription_mgmt_' + id))
        self.find_element(self.locators.get('subscription_mgmt_' + id)).click()

    def check_subscription_list_page(self, sub_list):
        self.wait_until_element_clickable(self.locators.get('publicatn_data_row_01'))
        return self.find_element(self.locators.get('publicatn_data_row_01')).text

    def check_existing_record(self):
        self.wait_until_element_clickable(self.locators.get('publication_list_title'))
        check = self.find_element(self.locators.get('publication_list_title')).text
        assert check is not ""

    def check_total_count(self):
        self.wait_until_element_located(self.locators.get('total_count'))
        total_count = self.find_element(self.locators.get('total_count')).text
        total_count = total_count.replace('Total Count: ', '')
        assert int(total_count) >= 0

    def PaginationOnSubscriptionGrid(self, total_count, page_size):
        page_no = 1
        while total_count >= page_size:
            self.wait_until_element_clickable(self.locators.get('recipient_data_row_01'))
            check1 = self.find_element(self.locators.get('recipient_data_row_01')).text
            self.wait_until_element_clickable(self.locators.get('pagination'))
            self.find_element(self.locators.get('pagination')).click()
            # increment
            page_no += 1
            page_size = 1 + (page_no - 1) * page_size + page_size
            self.wait_until_element_clickable((By.ID, page_no))
            self.find_element((By.ID, page_no)).click()
            time.sleep(5)
            self.wait_until_element_clickable(self.locators.get('recipient_data_row_01'))
            check2 = self.find_element(self.locators.get('recipient_data_row_01')).text
            assert check1 != check2


    def get_total_count(self):
        self.wait_until_element_located(self.locators.get('total_count'))
        total_count = self.find_element(self.locators.get('total_count')).text
        total_count = total_count.replace('Total Count: ', '')
        return int(total_count)

    def get_page_size(self):
        self.wait_until_element_clickable(self.locators.get('pageSize'))
        page_size_value = self.find_element(self.locators.get('pageSize')).text
        return int(page_size_value)

    def click_page_size(self):
        self.wait_until_element_clickable(self.locators.get('pageSize'))
        self.find_element(self.locators.get('pageSize')).click()

    def click_page_size_value(self, value):
        self.wait_until_element_clickable(self.locators.get('pageSize_'+value))
        self.find_element(self.locators.get('pageSize_'+value)).click()
        self.is_loading_completed()

    def compare_page_length(self, value):
        global total_count
        try:
            total_count = self.find_element(self.locators.get('total_count')).text
            total_count = total_count.replace('Total Count: ', '')
            assert int(total_count) > int(value)
        except AssertionError:
            AssertionError('Total Count is ', total_count, ' which is less than Page Size')

    def check_page_length(self, id):
        try:
            total_entries = len(self.find_elements(self.locators.get('page_size_len_' + id)))
            page_size_value = self.find_element(self.locators.get('pageSize')).text
            assert int(total_entries) <= int(page_size_value)
        except AssertionError:
            AssertionError('Total entries are greater than Page Size Value')

    def check_add_publication(self):
        self.wait_until_element_located(self.locators.get('addPublicationButton'))
        add = self.find_element(self.locators.get('addPublicationButton')).is_displayed()
        assert add is True

    def add_hover(self):
        self.wait_until_element_clickable(self.locators.get('addPublicationButton'))
        element_to_hover_over = self.find_element(self.locators.get('addPublicationButton'))
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def add_tool_visibility(self):
        self.wait_until_element_located(self.locators.get('addPublicationTool'))
        addToolTip = self.find_element(self.locators.get('addPublicationTool')).is_displayed()
        assert addToolTip is True

    def getPublicationGridDataRowTextById(self, id):
        return self.find_element(self.locators.get('publicatn_data_row_' + id)).text

    # ===========================================================================
    # Edit subscription starts

    def check_edit_page(self, header):
        self.wait_until_element_clickable(self.locators.get('edit_subscription_title'))
        assert header == self.find_element(self.locators.get('edit_subscription_title')).text

    def doubleClickFirstRecordSub(self):
        self.wait_until_element_clickable(self.locators.get('first_row_data_sub'))
        source = self.find_element(self.locators.get('first_row_data_sub'))
        action = ActionChains(self.driver)
        action.double_click(source).perform()
        self.is_loading_completed()

    # ===========================================================================
    # Recipient grid starts

    def check_recipient_list_title(self, sub_list):
        self.wait_until_element_clickable(self.locators.get('recipient_list_title'))
        return self.find_element(self.locators.get('recipient_list_title')).text

    def check_existing_record_for_recipient(self):
        self.wait_until_element_clickable(self.locators.get('recipient_data_row_01'))
        check = self.find_element(self.locators.get('recipient_data_row_01')).text
        assert check is not ""

    def check_add_recipient(self):
        self.wait_until_element_located(self.locators.get('addRecipientButton'))
        add = self.find_element(self.locators.get('addRecipientButton')).is_displayed()
        assert add is True

    def add_hover_recipient(self):
        self.wait_until_element_clickable(self.locators.get('addRecipientButton'))
        element_to_hover_over = self.find_element(self.locators.get('addRecipientButton'))
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

    def add_tool_recipient_visibility(self):
        self.wait_until_element_located(self.locators.get('addRecipientToolTip'))
        addToolTip = self.find_element(self.locators.get('addRecipientToolTip')).is_displayed()
        assert addToolTip is True

    def getRecipientGridDataRowTextById(self, id):
        return self.find_element(self.locators.get('recipient_data_row_' + id)).text
