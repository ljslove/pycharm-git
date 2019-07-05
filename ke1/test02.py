
from selenium import  webdriver
import time

driver=webdriver.Chrome()


driver.get("http://www.baidu.com")
time.sleep(5)
driver.get("http://www.hao123.com")
#返回上一页
driver.back()



time.sleep(5)
#返回下一页
driver.forward()

time.sleep(5)
driver.refresh()

time.sleep(5)
driver.quit()

print("hoigjio")
print("jiorjiri")