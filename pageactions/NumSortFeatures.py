import time

from selenium.webdriver.common.action_chains import ActionChains
from pageactions.BasePage import BasePage
from selenium.webdriver.common.by import By


class NumSortFeatures(BasePage):

    def __init__(self, context):
        BasePage.__init__(
            self,
            context.driver
        )

        self.locators = {
            # Publication Grid Sorts --Start
            'sort_publication_grid_01': (By.XPATH, "//div[contains(text(),'Publication Code')]"),
            'sort_publication_grid_02': (By.XPATH, "//div[contains(text(),'Publication Name')]"),
            'sort_publication_grid_03': (By.XPATH, "//div[contains(text(),'Created On')]"),
            'sort_publication_grid_04': (By.XPATH, "//div[contains(text(),'Created By')]"),
            'sort_publication_grid_05': (By.XPATH, "//div[contains(text(),'Modified On')]"),
            'sort_publication_grid_06': (By.XPATH, "//div[contains(text(),'Modified By')]"),

            # Recipient Grid Sorts --End
            'sort_recipient_grid_01': (By.XPATH, "//div[contains(text(),'Recipient Name')]"),
            'sort_recipient_grid_02': (By.XPATH, "//div[contains(text(),'Address')]"),
            'sort_recipient_grid_03': (By.XPATH, "//div[contains(text(),'Primary Phone')]"),
            'sort_recipient_grid_04': (By.XPATH, "//div[contains(text(),'Backup Phone')]"),
            'sort_recipient_grid_05': (By.XPATH, "//div[contains(text(),'Email')]"),
            'sort_recipient_grid_06': (By.XPATH, "//div[contains(text(),'Monthly Cost')]"),
        }

    # Subscription Grid Sorts Methods --Start
    def sortByDoubleClickOnPublicationGrid(self, id):
        self.wait_until_element_clickable(self.locators.get('sort_publication_grid_'+id))
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(self.locators.get('sort_publication_grid_'+id)))
        action.double_click().perform()
        time.sleep(3)

    def sortByDoubleClickOnRecipientGrid(self, id):
        self.wait_until_element_clickable(self.locators.get('sort_recipient_grid_'+id))
        action = ActionChains(self.driver)
        action.move_to_element(self.find_element(self.locators.get('sort_recipient_grid_'+id)))
        action.double_click().perform()
        time.sleep(3)
