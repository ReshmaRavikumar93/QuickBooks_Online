from selenium.webdriver.common.by import By



class QuickBooksDashBoard:
    #Loactors
    Text_DashBoard="//span[text()='Dashboard']"

    #Constructor
    def __init__(self,driver):
        self.driver=driver

    #Action Methods
    def dashboard(self):
        DashBoradtext=self.driver.find_element(By.XPATH,self.Text_DashBoard).text
        return DashBoradtext
