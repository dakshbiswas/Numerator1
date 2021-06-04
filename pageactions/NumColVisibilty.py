import time

from pageactions.BasePage import BasePage
from selenium.webdriver.common.by import By


class NumColVisibility(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

        self.locators = {
            # Publication Grid Column

            'publication_column_01': (By.XPATH, "//div[contains(text(),'Publication Code')]"),
            'publication_column_02': (By.XPATH, "//div[contains(text(),'Publication Name')]"),
            'publication_column_03': (By.XPATH, "//div[contains(text(),'Created On')]"),
            'publication_column_04': (By.XPATH, "//div[contains(text(),'Created By')]"),
            'publication_column_05': (By.XPATH, "//div[contains(text(),'Modified On')]"),
            'publication_column_06': (By.XPATH, "//div[contains(text(),'Modified By')]"),

            # Edit subscription transactions column
            'tran_col_01': (By.XPATH, "//th[contains(text(),'Transaction Date')]"),
            'tran_col_02': (By.XPATH, "//th[contains(text(),'Start Date')]"),
            'tran_col_03': (By.XPATH, "//th[contains(text(),'End Date')]"),
            'tran_col_04': (By.XPATH, "//th[contains(text(),'Amount')]"),
            'tran_col_05': (By.XPATH, "//th[contains(text(),'Transaction Type')]"),
            'tran_col_06': (By.XPATH, "//th[contains(text(),'Notes')]"),
            'tran_col_07': (By.XPATH, "//th[contains(text(),'Recipient')]"),

            # Recipient Grid Columns

            'recipient_column_01': (By.XPATH, "//div[contains(text(),'Recipient Name')]"),
            'recipient_column_02': (By.XPATH, "//div[contains(text(),'Address')]"),
            'recipient_column_03': (By.XPATH, "//div[contains(text(),'Primary Phone')]"),
            'recipient_column_04': (By.XPATH, "//div[contains(text(),'Backup Phone')]"),
            'recipient_column_05': (By.XPATH, "//div[contains(text(),'Email')]"),
            'recipient_column_06': (By.XPATH, "//div[contains(text(),'Monthly Cost')]"),
        }

    def check_columns_visibility(self, col, id):
        self.wait_until_element_clickable(self.locators.get('publication_column_' + id))
        check = self.find_element(self.locators.get('publication_column_' + id)).text
        check == col

    def check_columns_visibility_edit_sub(self, col, id):
        self.wait_until_element_clickable(self.locators.get('tran_col_' + id))
        check = self.find_element(self.locators.get('tran_col_' + id)).text
        check == col

    def check_columns_visibility_recipient(self, col, id):
        self.wait_until_element_clickable(self.locators.get('recipient_column_' + id))
        check = self.find_element(self.locators.get('recipient_column_' + id)).text
        check == col