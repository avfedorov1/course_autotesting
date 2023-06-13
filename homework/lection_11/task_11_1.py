# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()
# driver.maximize_window()  # Браузер будем открывать сразу в полном экране
sbis_site = 'https://sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    print('Переходим по url')
    driver.get(sbis_site)  # Переход по url
    print('Проверяем, что сайт открылся')
    assert driver.current_url == sbis_site  # Проверяем, что сайт открылся
    sleep(1)
    print('Проверяем, что заголовок сайта правильный')
    assert driver.title == sbis_title, 'Сайт не открылся'  # Проверка, что заголовок вкладки правильный
    sleep(1)
    tab_contacts = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu [href="/contacts"]')
    print('Проверяем, что кнопка "Контакты" отображается на странице')
    assert tab_contacts.is_displayed(), 'Кнопка не отображается'  # Проверка отображения кнопки на странице
    tab_contacts.click()
    sleep(1)
    baner_tensor = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor[target="_blank"]')
    print('Проверяем, что баннер отображается на странице')
    assert baner_tensor.is_displayed(), 'Баннер не отображается'
    baner_tensor.click()
    sleep(2)
    print('Переход на новую активную вкладку')
    driver.switch_to.window(driver.window_handles[1])  # Переход на новою вкладку
    news = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__card-title')
    print('Прокрутка до нужного элемента')
    news.location_once_scrolled_into_view  # Прокрутка до элемента
    sleep(1)
    news_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-bg .tensor_ru-Index__card-text a')
    sleep(1)
    print('Проверка отображения кнопки на новости')
    assert news_btn.is_displayed()  # Проверка отображения кнопки на странице
    news_btn.click()
    news_url = 'https://tensor.ru/about'
    print('Проверяем, что перешли именно на нужный адрес')
    assert driver.current_url == news_url  # Проверяем, что перешли именно на 'https://tensor.ru/about/'
    sleep(1)
    print('Закрываем активную вкладку')
    driver.close()  # Закрываем активную вкладку
    sleep(1)

finally:
    print('Закрываем браузер')
    driver.quit()  # Закрываем браузер
