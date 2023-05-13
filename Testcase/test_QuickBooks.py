import os
import time

import pytest

from PageObjects.QuickBooksLoginPage import QuickBooksLoginPage
from PageObjects.QuickBooksDashBoard import QuickBooksDashBoard
from Utilities.readproperties import Readconfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils



class Test_QuickBooksLogin:
    baseURL=Readconfig.getApplicationURL()
    path="C:\\Users\\rravikumar\\pythonProjectLastTry\\FrameWorkDevelopment\\TestData\\QuickBooksLoginData.xlsx"
    logger=LogGen.loggen()  #for logging

    @pytest.mark.sanity
    def test_QuickBooksLogin_001(self,setup):
        self.logger.info("*********test_QuickBooksLogin_001 started executing*********")
        self.driver=setup
        self.driver.implicitly_wait(300)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.QBLogin = QuickBooksLoginPage(self.driver)  #QuickBooks Login Page Object class
        self.QBdashboard = QuickBooksDashBoard(self.driver)#QuickBooks Dashboard Page Object class

        self.logger.info("*****Calling the Quickbooks Login Page****")
        self.Email=XLUtils.readData(self.path,"Sheet1",2,1)
        self.Password=XLUtils.readData(self.path,"Sheet1",2,2)
        self.logger.info("***Email is entered****")
        self.QBLogin.setEmail(self.Email)
        self.QBLogin.submitbutton()
        self.logger.info("****Password is entered****")
        self.QBLogin.setPassword(self.Password)
        self.QBLogin.submitbutton()
        self.QBLogin.ClickSkipForNow()
        self.logger.info("*****Selecting the Company File****")
        self.QBLogin.setSearch("TestCompanyNew")
        self.QBLogin.ChooseCompany()


        DashboradMessage=self.QBdashboard.dashboard()
        if DashboradMessage == "Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir)+"\\Screenshots\\"+"Test_QuickBooks_Login.png")
            self.driver.close()
            assert False




