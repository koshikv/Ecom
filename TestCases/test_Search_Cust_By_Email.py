import time

import pytest

from PageObjects.LoginPage import Login
from PageObjects.searchCustomers import searchCustomer
from PageObjects.addCustomers import addCutomers
from Utilities.readProperties import readConfig
from Utilities.customloggers import Log


class Test_004:
    baseurl = readConfig.getapplicationurl()
    username = readConfig.getusename()
    password = readConfig.getpassword()

    logger = Log.generateLog()

    @pytest.mark.regression
    def test_004_search_Customer_by_Email(self, setup):
        self.logger.info("***** Test_004 *****")
        self.logger.info("***** test_004_search_Customer_by_Email started *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("***** Login Successful *****")
        self.logger.info("***** Searching started *****")
        self.searchcust = searchCustomer(self.driver)
        self.cust = addCutomers(self.driver)
        self.cust.clickOn_mainLink_Cutomers()
        self.cust.clickOn_subLink_Customers()
        self.searchcust.set_Email_inputbox("victoria_victoria@nopCommerce.com")
        self.searchcust.click_Button_Search()
        time.sleep(5)
        status = self.searchcust.searchCustByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("***** test_004_search_Customer_by_Email finished *****")
