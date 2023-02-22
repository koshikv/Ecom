import pytest

from PageObjects.LoginPage import Login
from Utilities.readProperties import readConfig
from Utilities.customloggers import Log


class Test_001:
    baseurl = readConfig.getapplicationurl()
    username = readConfig.getusename()
    password = readConfig.getpassword()

    logger = Log.generateLog()

    @pytest.mark.regression
    def test_001_homepagelogin(self, setup):
        self.logger.info("***** Test_001 *****")
        self.logger.info("***** test_001_homepagelogin started *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            self.logger.info("***** test_001_homepagelogin is passed *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_homepagelogin.png")
            self.logger.error("***** test_001_homepagelogin is failed *****")
            self.driver.close()
            assert False

    def test_002_loginmainpage(self, setup):
        self.logger.info("***** Test_001 *****")
        self.logger.info("***** test_002_loginmainpage started *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.SetUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.ClickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("***** test_002_loginmainpage is passed *****")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(".//Screenshots//" + "test_loginmainpage.png")
            self.logger.error("***** test_002_loginmainpage is failed *****")
            self.driver.close()
            assert False
