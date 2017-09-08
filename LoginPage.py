from importlib_ import *

#Страница авторизации

class LoginPage:
    def __init__(self):
        self.login_inp = driver.find_element_by_css_selector('[name="loginName"] input')
        self.pass_inp = driver.find_element_by_css_selector('[name="loginPass"] input')
        self.login_but = driver.find_element_by_css_selector('.loginForm__sendButton')

    def set_login(self, login):       #Вводит логин
        self.login_inp.clear()
        self.login_inp.send_keys(login)

    def set_password(self, password): #Вводит пароль
        self.pass_inp.clear()
        self.pass_inp.send_keys(password)

    def enter(self):                  #Нажимает на кнопку Войти
        self.login_but.click()



