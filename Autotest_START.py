from importlib_ import *
from LoginPage import LoginPage
from Accordion import *
from StaffPageMain import *
from OurCompanyField import OurCompanyField
from StaffCard import StaffCard
starttest = datetime.datetime.now()

#Данные для авторизации
LOGIN = 'check_rigth_user'
PASS = 'qwerty123'
URL = 'https://fix-inside.tensor.ru/'      #для быстрой замены тестового стенда

driver.get(URL)
log('START!')

#Проверка: перешли на стартовую страницу сайта
_title = driver.title
class TestStart(unittest.TestCase):
    def test_Authorize(self):
        self.assertEqual(_title, "Вход в систему/СБИС", msg="Не зашел на страницу авторизации")
log('***Проверка прошла успешно: перешли на стартовую страницу сайта')

#ввожу логин
login_page = LoginPage()
login_page.set_login(LOGIN)
log('Ввожу логин: ' + LOGIN)

#ввожу пароль
login_page.set_password(PASS)
log('Ввожу пароль: ' + PASS)

#нажимаю Зайти
login_page.enter()
log('Жду 10 секунд. Не успел разобраться как sid из куки передавать')
time.sleep(10) # ожидание загрузки разводящей инсайда
log('Захожу')

#нажимаю Сотрудники первый раз в аккордеоне
accordion = Accordion1()
accordion.Staff_click_one()
log('нажимаю Сотрудники первый раз в аккордеоне')

#нажимаю Сотрудники второй раз в аккордеоне
accord = Accordion2()
accord.Staff_click_two()
log('нажимаю Сотрудники второй раз в аккордеоне')
time.sleep(1)

#Проверка: перешли в раздел сотрудники
_title_staff = driver.title
class TestStaffPage(unittest.TestCase):
    def test_Stuff(self):
        self.assertEqual(_title_staff, "Сотрудники/СБИС", msg="Не зашел в раздел СОТРУДНИКИ")
log('***Проверка прошла успешно: перешли в раздел сотрудники')

#Клик на наша компания на странице сотрудников
Staff_main_page = StaffPageMain()
Staff_main_page.Our_company_click()
log('Клик на наша компания на странице сотрудников')
time.sleep(3) # ожидание лайтбокса

#Проверка: открылась форма с подразделениями
Our_Comp_Assert = driver.find_element_by_css_selector('.ws-float-area-title').text
class TestCompPage(unittest.TestCase):
    def test_our_comp_1(self):
        self.assertEqual(Our_Comp_Assert, "Выберите организацию", msg="Не открылась форма с подразделениями")
log('***Проверка прошла успешно: открылась форма с подразделениями')

#Клик на строку "Наша комания"
Our_comp_string = OurCompanyField()
Our_comp_string.Our_comp_cl()
log('Клик на строку "Наша комания"')
#time.sleep(1) # ожидание

#Проверка: Выбрана НАША КОМПАНИЯ
Our_Comp_Assert2 = driver.find_element_by_css_selector('[sbisname="OurComp"] span').text
class TestCompPage2(unittest.TestCase):
    def test_our_comp_2(self):
        self.assertEqual(Our_Comp_Assert2, "Наша компания", msg="Выбрана не НАША КОМПАНИЯ")
log('***Проверка прошла успешно: выбрана НАША КОМПАНИЯ')

#В поиске исчу фамилию имя
Staff_main_page.EnterNameStaff()
log('Ищу в поле поиска: Белова Олеся Александровна')
time.sleep(1) # ожидание

#Проверка: Поиск заданного имени
Find_Name_Stuff = driver.find_element_by_css_selector('.controls-HtmlDecorators-highlight').text
class FindNameStuff(unittest.TestCase):
    def test_find_name_staff(self):
        self.assertEqual(Find_Name_Stuff, "Белова Олеся Александровна", msg="На странице нет сотрудника с таким ФИО")
log('***Проверка прошла успешно: Поиск заданного имени в разделе Сотрудники')

#Клик на фамилию имя
Click_name_staff = ClickNameStaff()
Click_name_staff.ClickNameStaf()
log('Захожу в карточку сотрудника')
time.sleep(1)

#Проверка: Открытие карточки сотрудника
Find_Name_Stuff_Card = driver.find_element_by_css_selector('.controls-EditAtPlace__textField.controls-TextBox__field').text
class FindNameStuffCard(unittest.TestCase):
    def test_open_card_staff(self):
        self.assertEqual(Find_Name_Stuff_Card, "Белова", msg="Карточка не открылась")
log('***Проверка прошла успешно: Открытие карточки сотрудника')

#Закрываю карточку
Staff_card = StaffCard()
Staff_card.Close_staff_card()
log('Закрываю карточку сотрудника')
time.sleep(2)

#Разлогиниваюсь. Клик на Имя аккаунта
Staff_main_page.ExitAccount()
log ('Разлогиниваюсь. Клик на Имя аккаунта')
time.sleep(1)

#Закрываю два
Exit_account = ExitAccount()
Exit_account.ExitAccount2()
log('EXIT')
#time.sleep(2)

#Проверка: перешли на стартовую страницу сайта
class TestEnd(unittest.TestCase):
    def test_end(self):
        self.assertEqual(_title, "Вход в систему/СБИС", msg="Не зашел на страницу авторизации")
log('***Проверка прошла успешно: перешли на стартовую страницу сайта')
if __name__ == '__main__':
    unittest.main()

endtest = datetime.datetime.now()
my_file.write(str(endtest - starttest) + ' Время теста')
print(str(endtest - starttest) + ' Время теста')

driver.close()

