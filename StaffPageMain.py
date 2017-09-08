from importlib_ import *

#Страница Сотрудники

class StaffPageMain:
    def __init__(self):
        self.Our_company_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[sbisname="OurComp"] span')))
#        self.Our_company_button = driver.find_element_by_css_selector('[sbisname="OurComp"] span')
        self.Find_name = driver.find_element_by_css_selector('.js-controls-TextBox__field.controls-TextBox__field')
        self.Exit_page_1 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="UserNameLinkButton"] span')))

    def Our_company_click(self):  #Нажимает на "Наша компания"
        self.Our_company_button.click()

    def EnterNameStaff(self):     #Вводит Имя
        self.Find_name.send_keys("Белова Олеся Александровна", Keys.ENTER)

    def ExitAccount(self):  # Выходит из аккаунта (нажатие на крестик)
        self.Exit_page_1.click()

class ClickNameStaff:
    def __init__(self):
        self.Click_name_stuff = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.controls-DataGridView__td.controls-DataGridView__firstContentCell')))
#       self.Click_name_stuff = driver.find_element_by_css_selector('.controls-DataGridView__td.controls-DataGridView__firstContentCell')

    def ClickNameStaf(self): #Клик на выбранного сотрудника
        self.Click_name_stuff.click()

class ExitAccount:
    def __init__(self):
        self.Exit_page_2 = driver.find_element_by_css_selector('.ws-hover-target.icon-16.icon-OutHotel.icon-primary')

    def ExitAccount2(self): #Выходит из аккаунта (нажатие на Выход)
        try:
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="UserNameLinkButton"] span')))
        finally:
            self.Exit_page_2.click()





