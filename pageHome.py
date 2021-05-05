from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException 

class PageHome:
    def __init__(self, my_driver):                
                
        self.popup_promo = (By.XPATH, '//button[@id="onesignal-slidedown-cancel-button"]')        
        self.popup_register = (By.XPATH, '//div[@class="braindw_closepop"]')        
        self.link_icon_login = (By.XPATH, '//span[@class="icon icon-16-user"]')        
        self.driver = my_driver

    def enlazar_login(self):
        try:
            emergent_promo = WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.popup_promo))
            emergent_promo.click()
        except TimeoutException:
            print('popup promo not show')

        try:
            emergent_register = WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable(self.popup_register))
            emergent_register.click()            
        except TimeoutException:
            print('popup register not show')

        try:
            link_login = WebDriverWait(self.driver, 6).until(EC.presence_of_element_located(self.link_icon_login))
            link_login.click()
        except:
            print('No se encuentra el elemento')
            