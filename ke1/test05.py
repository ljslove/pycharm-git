
from selenium import webdriver

import  time

driver=webdriver.Chrome()
driver.get("https://mail.126.com/")
time.sleep(6)
driver.switch_to.frame(0)

print(driver.find_elements_by_xpath("//*[@class='u-input box']")[0].text)

time.sleep(4)

driver.quit()