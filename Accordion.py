from importlib_ import *

class Accordion1:
    def __init__(self):
        self.staff_mini = driver.find_element_by_css_selector('[data-id="staff"] a')

    def Staff_click_one(self): #Клик на Сотрудники в аккордеоне
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-id="staff"] a')))
        finally:
            self.staff_mini.click()

class Accordion2:
    def __init__(self):
        self.staff_max = driver.find_element_by_css_selector('.navigation-LeftNavigation__HeadTitle')

    def Staff_click_two(self):  #Второй клик на Сотрудники в аккордеоне
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.navigation-LeftNavigation__HeadTitle')))
        finally:
            self.staff_max.click()