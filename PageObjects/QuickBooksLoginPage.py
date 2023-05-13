from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
class QuickBooksLoginPage:
    #Locators
    Email_xpath="//input[@name='Email']"
    Rememberme_xpath="//*[@type='checkbox']"
    submit_xpath="//*[@type='submit']"
    Password_xpath="//*[@name='Password']"
    Text_SkipNow = "//button[text()='Skip for now']"
    ID_Search="idsTxtField1"
    Text_CompanyName="//span[text()='TestCompanyNew']"
    #Constructors
    def __init__(self,driver):
        self.driver=driver

    #Action Methods
    def setEmail(self,susername):
        self.driver.find_element(By.XPATH,self.Email_xpath).send_keys(susername)

    def checkRememberMe(self):
        self.driver.find_element(By.XPATH,self.Rememberme_xpath).click()

    def submitbutton(self):
        self.driver.find_element(By.XPATH,self.submit_xpath).click()

    def setPassword(self,sPassword):
        self.driver.find_element(By.XPATH,self.Password_xpath).send_keys(sPassword)

    def ClickSkipForNow(self):
        self.driver.find_element(By.XPATH,self.Text_SkipNow).click()

    def setSearch(self,searchdata):
        Searching=self.driver.find_element(By.ID,self.ID_Search)
        Searching.send_keys(searchdata)
        Searching.send_keys(Keys.ENTER)

    def ChooseCompany(self):
        self.driver.find_element(By.XPATH,self.Text_CompanyName).click()



