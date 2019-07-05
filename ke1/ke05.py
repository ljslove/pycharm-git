#多窗口切换

from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://bj.ganji.com/");

time.sleep(5)
#打印当前页面的title

print(driver.title)
#打印当前页面的URL
print(driver.current_url)

driver.find_element_by_link_text("包吃包住").click()
time.sleep(3)
#切换到第二个页面
all_h=driver.window_handles
driver.switch_to.window(all_h[-1])
print(driver.title)
print(driver.current_url)

#切换到第一个页面
driver.switch_to.window(all_h[0])
print(driver.title)
print(driver.current_url)
driver.quit()
print("trgjigjoi")
print("rjgiogjoi")
