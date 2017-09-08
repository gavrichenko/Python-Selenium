from importlib_ import *

#Карточка сотрудника
class StaffCard:
    def __init__(self):
        self.close_card = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.sbisname-window-title-close.ws-button-classic.ws-component.ws-control-inactive.ws-enabled.ws-field-button.ws-float-close-right.ws-no-select')))

    def Close_staff_card(self): #Закрывает карточку партнера
        self.close_card.click()
        log('Закрываю карточку сотрудника')

