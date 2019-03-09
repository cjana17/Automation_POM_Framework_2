from selenium import webdriver
import time
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
from pages.userpage import UserPage

@pytest.mark.usefixtures("test_launch_browser")
class TestLogin:
    def test_login(self,test_launch_browser):
        driver=self.driver
        lp=LoginPage(driver)
        lp.enter_user_name()
        lp.enter_password()
        lp.click_on_login_btn()

    def test_createuser(self,test_launch_browser):
        driver=self.driver
        up=UserPage(driver)
        time.sleep(5)
        up.click_on_user_btn()
        time.sleep(5)
        up.click_add_user_btn()
        time.sleep(5)

        driver.find_element_by_xpath("//*[@id='userDataLightBox_firstNameField']").send_keys("Test")
        driver.find_element_by_xpath("//*[@id='userDataLightBox_lastNameField']").send_keys("Test")
        driver.find_element_by_xpath("//*[@id='userDataLightBox_emailField']").send_keys("Test")
        driver.find_element_by_xpath("//*[@id='userDataLightBox_commitBtn']/div/span").click()
        time.sleep(5)


