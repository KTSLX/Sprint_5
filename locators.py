
#Логин
email_input_field = './/div/div/input[@type="text"]'  #поле ввода email на странице входа
password_input_field = './/div/div/input[@type="password"]'  #поле ввода пароля на странице входа
sign_in_button_on_login_page = './/form/button[text()="Войти"]'  #кнопка Входа на странице логина
sign_in_button_on_registration_page = './/div/div/p[text()="Уже зарегистрированы?"]/a[text()="Войти"]'  #кнопка входа на странице регистрации
sign_in_button_on_recovery_page = './/div/div/p[text()="Вспомнили пароль?"]/a[text()="Войти"]'  #кнопка входа на странице Восстановления пароля
sign_in_button = './/section/div/button[text()="Войти в аккаунт"]'  #кнопка Войти в аккаунт на главной странице
registration_button_on_login_page = './/div/div/p/a[text()="Зарегистрироваться"]'  #кнопка "Зарегистрироваться" на странице логина
recovery_button_on_login_page = './/div/div/p/a[text()="Восстановить пароль"]'  #кнопка "забыл пароль" на странице логина


#Шапка
account_button = './/div/header/nav/a/p'  #кнопка "Личный Кабинет" в шапке
constructor_button = './/header/nav/ul/li/a/p[text()="Конструктор"]'  #Кнопка "Конструктор" в шапке
stellar_burgers_button = './/header/nav/div/a'  #кнопа "Stellar Burgers" в шапке

#Регистрация
registration_name_input = './/label[text()="Имя"]/following-sibling::input'  #поле ввода "Имя" на странице регистрации
registration_email_input = './/label[text()="Email"]/following-sibling::input'  #поле ввода "Email" на странице регистрации
registration_password_input = './/label[text()="Пароль"]/following-sibling::input'  #поле ввода "Пароль" на странице регистрации
registration_in_form_button = './/form/button[text()="Зарегистрироваться"]'  #кнока "Зарегистрироваться" в форме регистрации
registration_form_error = './/fieldset/div/p[text()="Некорректный пароль"]'  #Error некорректный пароль


#Личный кабинет
logout_button = './/ul/li/button[text()="Выход"]'  #кнопка выхода из личного кабинета
account_info_header = './/nav/p[text()="В этом разделе вы можете изменить свои персональные данные"]'


#Конструктор
constuctor_header = './/main/section/h1[text()="Соберите бургер"]'  #заголовок над конструктором
fillings_button = './/div/span[text()="Начинки"]'  #Начинки кнопка
fillings_header = './/div/h2[text()="Начинки"]'  #Начинки заголовок
souces_button = './/div/span[text()="Соусы"]'  #Соусы
souces_header = './/div/h2[text()="Соусы"]'  #Соусы заголовок
buns_button = './/div/span[text()="Булки"]'  #Булки
buns_header = './/div/h2[text()="Булки"]'  #Булки заголовок
constructor_window = './/main/section/div[@class="BurgerIngredients_ingredients__menuContainer__Xu3Mo"]'  #окно конструктора для скролла вниз