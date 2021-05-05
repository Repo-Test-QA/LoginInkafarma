from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys 


class PageCredential:

    def __init__(self, my_driver):
        
        self.modal_google = (By.XPATH, '//body/div/div[@id="initialView"]')
        self.input_user = (By.XPATH, '//input[@type="email"][@class="whsOnd zHQkBf"]')          
        self.input_password = (By.XPATH, '//input[@type="password"][@class="whsOnd zHQkBf"]')        
        self.driver = my_driver


    def ingresar_credential(self, input_user, input_password):

        try:

            self.driver.current_window_handle            
            windows = self.driver.window_handles
            for window in windows:
                self.driver.switch_to_window(window) 


            ingresar_user = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(self.input_user))
            ingresar_user.send_keys(input_user, Keys.ENTER) 
            print('pase input_user ')

            ingresar_password = WebDriverWait(self.driver, 8).until(EC.presence_of_element_located(self.input_password))
            ingresar_password.send_keys(input_password, Keys.ENTER)            
            print('pase input_password ')            
            
        except:
            print('No se encuentra el elemento')
        
        