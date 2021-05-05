from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait

class PageLogin:

    def __init__(self, my_driver):

        self.btn_google = (By.XPATH, '//button[@class="btn btn-block btn-secondary text-black label-black"]')                  
        self.driver = my_driver

    def ingresar_login_google(self):
        try:
            ingresar_google = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.btn_google))
            ingresar_google.click()
            print('pase btn_login ')
            
        except:
            print('No se encuentra el elemento')

