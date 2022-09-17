import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

email = "test.user.05@inbox.ru"                                                       # тестовый юзер, могут быть любые валидные данные
                                                                                      # надо быть записанным на курс https://stepik.org/course/575/syllabus?auth=registration
password = "testpassword0505"
stepik_url = "https://stepik.org/catalog"
task_link = "https://stepik.org/lesson/236205/step/7?auth=registration&unit=208637"   # валидная сылка на задание
answer = "text_to_be_present_in_element"                                              # любая str, но лучше с правильным ответом))

browser = webdriver.Chrome()
browser.get(stepik_url)

browser.implicitly_wait(10)

button_login = browser.find_element(By.ID, "ember246").click()                        # авторизация и открытие задания
input_email = browser.find_element(By.ID, "id_login_email").send_keys(email)
input_password = browser.find_element(By.ID, "id_login_password").send_keys(password)
button_voity = browser.find_element(By.CSS_SELECTOR, "button.sign-form__btn.button_with-loader").click()

time.sleep(3)

browser.get(task_link)

def check_exists():                                                                   # функция проверяет наличие кнопки "решить снова
    try:                                                                              # т.е. было ли задание решено до этого
        browser.find_element(By.CSS_SELECTOR, "button.again-btn.white")
    except NoSuchElementException:
        return False
    return True

def send_answer():                                                                    # отправка ответа на степик
    input_answer = browser.find_element(By.CSS_SELECTOR,
                                        "textarea.ember-text-area.ember-view.textarea.string-quiz__textarea")
    input_answer.send_keys(answer)
    button_submit = browser.find_element(By.CSS_SELECTOR, "button.submit-submission")
    button_submit.click()


if browser.current_url == task_link:
    if check_exists():
        button_again = browser.find_element(By.CSS_SELECTOR, "button.again-btn.white")
        button_again.click()
        time.sleep(2)
        send_answer()
    else:
        send_answer()

else:
    if check_exists():
        button_unit = browser.find_element(By.ID, "ember936")
        button_unit.click()
        send_answer()
