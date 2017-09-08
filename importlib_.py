# -*- coding: utf-8 -*-

from selenium import webdriver  # работа с браузером
from selenium.webdriver.common.keys import Keys  # имитация нажатий клавиатуры
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # ожидания различных событий
from selenium.webdriver.support import expected_conditions as EC #  ожидания различных событий
from selenium.webdriver.support.ui import Select # работа со списками
from selenium.webdriver.common.action_chains import ActionChains # различные действия
import unittest
import datetime # дата для лога
import time # время для лога


driver = webdriver.Chrome() #запуск в хроме
driver.maximize_window() #развернуть на весь экран

#логи
my_file = open('log.log', 'w')
def log(text):
   my_file.write(str(datetime.datetime.now()) + ' :   ')
   my_file.write(text + '\n')
   print(str(datetime.datetime.now()) + ' :   ')
   print(text + '\n')
#логи