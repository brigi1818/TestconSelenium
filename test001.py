
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_url="https://www.calculator.net/percent-calculator.html"

driver=webdriver.Chrome(executable_path="D:/DescargasD/MAIS/test/selen/drivers/chromedriver.exe")

driver.maximize_window()

driver.implicitly_wait(10) #10 seg

driver.get(base_url)

element1 = driver.find_element(By.XPATH, "//*[@id='cpar1']")
element1.click()
element1.send_keys("10")

element2 = driver.find_element(By.XPATH, "//*[@id='cpar2']")
element2.click()
element2.send_keys("5")

driver.find_element(By.XPATH,"//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]").click();

print(driver.find_element(By.XPATH, "//*[@id='content']/p[2]/font/b").text)

