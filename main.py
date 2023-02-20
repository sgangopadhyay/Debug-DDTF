from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from Test_Data import data
from Test_Locators import locators
from Test_Codes import excel_function
from time import sleep

class Suman_DataDrivenTestingFramework:
    excel_file = 'D:\workspace\DDTF\Test_Data\login_data.xlsx'

    excel_data = excel_function.Suman_Excel_Function(excel_file)

    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(data.Suman_Data().url)
    
    def login(self):
        sleep(3)
        self.driver.find_element(by=By.NAME, value=locators.Suman_Locators().username_locator).send_keys(data.Suman_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Suman_Locators().password_locator).send_keys(data.Suman_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Suman_Locators().submitButton_locator).click()
        if(self.driver.current_url == data.Suman_Data().dashboard_url):
            print('SUCCESS : Login successfull')
            self.driver.quit()
        else:
            print('FAILURE : Login failure')
    
    def DDTF(self):
        sleep(3)
        for i in range(1, self.excel_data.row_count+1):
            self.__init__()
            for username, password in self.excel_data.dic().items():
                self.driver.find_element(by=By.NAME, value=locators.Suman_Locators().username_locator).send_keys(username)
                self.driver.find_element(by=By.NAME, value=locators.Suman_Locators().password_locator).send_keys(password)
                self.driver.find_element(by=By.XPATH, value=locators.Suman_Locators().submitButton_locator).click()
                if(self.driver.current_url == data.Suman_Data().dashboard_url):
                    print('SUCCESS : Login successfull')
                    self.driver.quit()                    
                else:
                    print('FAILURE : Login failure')
                    self.driver.quit()
                

s = Suman_DataDrivenTestingFramework()

s.DDTF()

