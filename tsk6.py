import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = " http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()
browser.get(link)

valuable1 = int(browser.find_element(By.ID, 'num1').text)
valuable2 = int(browser.find_element(By.ID, 'num2').text)

sum = valuable1 + valuable2

select = Select(browser.find_element(By.ID, "dropdown"))
select.select_by_value(str(sum))

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()

time.sleep(5)
browser.quit()
