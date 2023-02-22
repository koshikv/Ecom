import pytest
from selenium.webdriver.common.by import By
from PageObjects.LoginPage import Login
from PageObjects.addCustomers import addCutomers
from Utilities.readProperties import readConfig
from Utilities.customloggers import Log


class Test_003_Add_Customers:
    baseurl = readConfig.getapplicationurl()
    username = readConfig.getusename()
    password = readConfig.getpassword()

    logger = Log.generateLog()

    @pytest.mark.regression
    def test_003_addCustomer(self, setup):
        self.logger.info("***** Test_003_Add_Customers *****")
        self.logger.info("***** Test_003_Add_Customers started *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("***** Login Successful *****")

        self.logger.info("***** Starting Add Customer Test *****")

        self.addCust = addCutomers(self.driver)
        self.addCust.clickOn_mainLink_Cutomers()
        self.addCust.clickOn_subLink_Customers()
        self.addCust.clickOn_link_AddNew()
        self.addCust.set_Email("rajuheraferi1@gmail.com")
        self.addCust.set_Password("rajubhai")
        self.addCust.set_inputbox_FirstName("Raju")
        self.addCust.set_inputbox_LastName("mallya")
        self.addCust.set_radioButton_Gender("Male")
        self.addCust.set_DOB_box("2/02/1985")
        self.addCust.set_inputbox_Company_name("Hera Feri Services")
        self.addCust.set_checkbox_is_tax_exempt("yes")
        self.addCust.set_link_NewsLetter("your store name")
        self.addCust.set_link_Customer_roles("Registered")
        self.addCust.set_Managerofvendor("Vendor 1")
        self.addCust.set_inputbox_AdminComment("Enjoy!....")

        self.addCust.set_button_save()

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        if "customer has added successfully." in self.msg:
            self.logger.info("********** Add Customer Test is Passed **********")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_add_cust.png")
            self.logger.error("********** Add Customer Test is failed **********")
            self.driver.close()

        self.logger.info("********** Add Customer Test is End **********")
