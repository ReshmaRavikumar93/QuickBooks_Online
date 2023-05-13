import os
from datetime import datetime
import pytest
from selenium import webdriver

#**********Fixtures*********
@pytest.fixture()
def setup(browser):
    if browser == "edge":
        from selenium.webdriver.edge.service import Service
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        print("Launching the Browser")
        s = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=s)
        print("Launching the Edge Browser")
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager
        print("Launching the Browser")
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)
        print("Launching the Firefox browser")
    else:
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        print("Launching the Browser")
        options = webdriver.ChromeOptions()
        options.add_argument("--disable notifications")
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s, options=options)
        print("Launching the Chrome browser")
    return driver

#This will get the value of CLI/ Hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

# This will return the Browser value to setup method
@pytest.fixture()
def browser(request):
     return request.config.getoption("--browser")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    #config.option.htmlpath = "C:\\Users\\rravikumar\\pythonProjectLastTry\\FrameWorkDevelopment\\Reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"
    config.option.htmlpath = os.path.abspath(os.curdir) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"