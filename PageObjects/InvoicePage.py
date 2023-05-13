from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class QuickBooksInvoice:
    #Locators
    Text_IncomeArrow="//div[@data-path='incomeoverview']//a//span[2]"


    #constructor
    def __init__(self,driver):
        self.driver=driver

    #Action Methods
