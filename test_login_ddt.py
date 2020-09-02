import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time


class Test_case_002_ddt_Login:
    base_url = Readconfig.get_application_url()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login(self, setup):
        self.logger.info("**** Test case 002 DDT Login ****")
        self.logger.info("**** verifying test login ****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)

        #must obtain data from .xlsx

        self.rows = XLUtils.get_row_count(self.path, "Hoja 1")
        print("Number of rows in the Excel: ", self.rows)

        list_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.read_data(self.path, 'Hoja 1', r, 1)
            self.password = XLUtils.read_data(self.path, 'Hoja 1', r, 2)
            self.exp = XLUtils.read_data(self.path, 'Hoja 1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            actual_title = self.driver.title
            expected_title = "Dashboard / nopCommerce administration"

            if actual_title == expected_title:
                if self.exp == "Pass":
                    self.logger.info("*** PASSED ***")
                    self.lp.clickLogout()
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** FAILED ***")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif actual_title != expected_title:
                if self.exp == "Pass":
                    self.logger.info("*** FAILED ***")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** PASSED ***")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("**** LOGIN DDT TEST PASSED")
            self.driver.close()
            assert True
        else:
            self.logger.info("**** LOGIN DDT TEST FAILED")
            self.driver.close()
            assert False

        self.logger.info("**** END OF Test case 002 DDT Login ****")
        self.logger.info("**** Test case 002 DDT Login COMPLETED ****")