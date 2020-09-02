import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_case_001_Login:
    base_url = Readconfig.get_application_url()
    username = Readconfig.get_user_email()
    password = Readconfig.get_password()
    logger = LogGen.loggen()

    def test_home_page_title(self, setup):
        self.logger.info("**** Test_case_001 ****")
        self.logger.info("**** verifying home page title ****")
        self.driver = setup
        self.driver.get(self.base_url)
        actual_title = self.driver.title

        if actual_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**** PASSED ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title.png")
            self.driver.close()
            self.logger.info("**** FAILED ****")
            assert False

    def test_login(self, setup):

        self.logger.info("**** verifying test login ****")
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        actual_title = self.driver.title

        if actual_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**** PASSED ****")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("**** FAILED ****")
            assert False
