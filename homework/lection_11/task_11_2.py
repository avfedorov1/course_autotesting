# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

driver = webdriver.Chrome()
# driver.maximize_window()  # Браузер будем открывать сразу в полном экране
sbis_site_fix = 'https://fix-online.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
my_login, my_password = 'testoootest', 'Qwerty123'
action_chains = ActionChains(driver)

try:
    # Авторизовываемся на сайте
    print('Переходим на сайт')
    driver.get(sbis_site_fix)  # Переходим на сайт
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    print('Вводим в поле логина данные и кликаем Enter')
    login.send_keys(my_login, Keys.ENTER)  # Вводим в поле логина данные и кликаем Enter
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    print('Вводим в поле пароль данные и кликаем Enter')
    password.send_keys(my_password, Keys.ENTER)  # Вводим в поле пароль данные и кликаем Enter
    sleep(3)
    print('Проверяем, что сайт открылся')
    assert driver.current_url == sbis_site_fix, 'Сайт не открылся'  # Проверяем, что сайт открылся
    print('Проверяем, что заголовок вкладки правильный')
    assert driver.title == 'СБИС', 'Неправильное название вкладки'  # Проверяем, что заголовок вкладки правильный
    sleep(3)  # Для стабильности

    # Переходим в реестр Контакты
    contacts = driver.find_element(By.CSS_SELECTOR, '[data-qa="Контакты"]')
    print('Кликаем меню аккордеона Контакты')
    contacts.click()
    print('Ждем чуток для стабильности')
    sleep(2)  # Для стабильности
    contacts2 = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle')
    print('Кликаем меню аккордеона Контакты еще раз')
    contacts2.click()
    sleep(3)  # Для стабильности
    print('Проверяем, что адрес страницы правильный')
    assert driver.current_url == 'https://fix-online.sbis.ru/page/dialogs', 'url раздела неверный'
    new_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="sabyPage-addButton"]')
    print('Кликаем на "+" для создания нового смс')
    new_message.click()
    sleep(3)

    # Отправляем сообщение самому себе
    message_search = driver.find_element(By.CSS_SELECTOR, '[data-qa="addressee-selector-root"] [data-qa="controls-Render__field"] input')
    print('В строке поиска вводим получателя смс')
    action_chains.click(message_search).perform()
    message_search.send_keys('Ярославский')
    sleep(1)
    print('Выбираем получателя из списка')
    person = driver.find_element(By.CSS_SELECTOR, '.person-BaseInfo')
    assert person.is_displayed(), 'Получатель не отображается в результате поиска'
    person.click()
    sleep(1)
    massage = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    print('Вводим текст нового смс')
    massage.send_keys('Новое сообщение я пишу')
    sleep(3)
    massage_send = driver.find_element(By.CSS_SELECTOR, '[title="Отправить"]')
    print('Отправляем сообщение')
    action_chains.key_down(Keys.CONTROL).send_keys(Keys.ENTER).perform()
    sleep(3)

    # Убеждаемся, что сообщение появилось в реестре
    print('Проверяем, что сообщение появилось в реестре')
    list_massage = driver.find_elements(By.CSS_SELECTOR, '.controls-MasterDetail_details .controls-ListViewV')
    assert list_massage[0].text.find('Новое сообщение я пишу') != -1, 'Смс нужное отсутствует'
    sleep(2)

    # Удаляем сообщение и убеждаемся, что удалили
    print('Открываем контекстное меню для удаления сообщения')
    action_chains.context_click(list_massage[0]).perform()
    sleep(1)
    context_menu = driver.find_element(By.CSS_SELECTOR, '.controls-Popup')
    assert context_menu.is_displayed(), 'Контекстное меню не отображается'
    delete_massage_btn = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    assert delete_massage_btn.is_displayed(), 'В контекстном меню отсутствует пункт удаления'
    print('Кликаем на пункт удаления')
    delete_massage_btn.click()
    assert list_massage[0].text.find('Новое сообщение я пишу') == -1, 'Сообщение не удалено'
    print('Сообщение удалено')
    sleep(2)


finally:
    print('Закрываем браузер')
    driver.quit()
