from selenium import webdriver
import unittest
from selenium.webdriver.chrome.options import Options
from pageHome import PageHome
from pageLogin import PageLogin
from pageCredential import PageCredential
import time


class TestCase(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_argument('start-maximized')        
        option.add_experimental_option("prefs", {
            "safebrowsing.enabled": 2,
        })

        self.driver = webdriver.Chrome('chromedriver.exe', chrome_options=option)
        self.driver.get('https://inkafarma.pe/')        
        self.driver.implicitly_wait(5)

        self.homePage = PageHome(self.driver)
        self.loginPage = PageLogin(self.driver)
        self.credentialPage = PageCredential(self.driver)

    
    def test_loguear(self):
        self.homePage.enlazar_login()
        self.loginPage.ingresar_login_google()
        self.credentialPage.ingresar_credential('test.automation.ta', 'prueba_ta01')
        time.sleep(5)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

        