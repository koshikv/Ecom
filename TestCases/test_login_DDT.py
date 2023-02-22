import pytest

from PageObjects.LoginPage import Login
from Utilities.readProperties import readConfig
from Utilities.customloggers import Log
from Utilities import EXUtils
import time


class Test_002_DDT_Login:
    baseurl = readConfig.getapplicationurl()
    path = ".//TestData//LoginData.xlsx"

    logger = Log.generateLog()

    @pytest.mark.regression
    @pytest.mark.sanity
    def test_002_loginmainpage(self, setup):
        self.logger.info("***** Test_002_DDT *****")
        self.logger.info("***** test_002_DDT_loginmainpage started *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.rows = EXUtils.getRowCount(self.path, 'sheet1')

        lst_status = []

        for r in range(2, self.rows + 1):
            self.username = EXUtils.readData(self.path, 'sheet1', r, 1)
            self.password = EXUtils.readData(self.path, 'sheet1', r, 2)
            self.exp = EXUtils.readData(self.path, 'sheet1', r, 3)

            self.lp.SetUsername(self.username)
            self.lp.setPassword(self.password)
            self.lp.ClickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("************* test is passed *************")
                    self.lp.ClickLogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("************* test is failed *************")
                    self.lp.ClickLogout()
                    lst_status.append("failed")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("************* teat is failed *************")
                    lst_status.append("failed")
                elif self.exp == "fail":
                    self.logger.info("************* test is passed *************")
                    lst_status.append("pass")

        if "failed" not in lst_status:
            self.logger.info("*********** Test_002_DDT_Login is passed ***********")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********** Test_002_DDT_Login is failed ***********")
            self.driver.close()
            assert False
        print(lst_status)
