import time

from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pageactions.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

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

        }


def checkInputFieldOnSubscriptionGrid(self, search_field, input_id):
    self.wait_until_element_located(self.locators.get('in_subscription_ ' +input_id))
    assert self.find_element(self.locators.get('in_subscription_ ' +input_id)).text == search_field