from importlib_ import *

#Поле, которое выезжает после нажатия на Наша Компания на странице Сотрудники

class OurCompanyField:
    def __init__(self):
        self.Our_comp_string = driver.find_element_by_css_selector('.OurOrgChoice-FirstLineNameBold')

    def Our_comp_cl(self): #Нажимает на строку "Наша компания"
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.OurOrgChoice-FirstLineNameBold')))
        finally:
             self.Our_comp_string.click()
