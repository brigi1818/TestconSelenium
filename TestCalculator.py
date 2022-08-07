import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class CalculatorTest(unittest.TestCase):
	def test_Calculator(self):
		self.driver = webdriver.Chrome(
		    executable_path="D:/DescargasD/MAIS/test/selen/drivers/chromedriver.exe")
		self.driver.get("https://www.calculator.net/percent-calculator.html")

		self.element1 = self.driver.find_element(By.XPATH, "//*[@id='cpar1']")
		self.element1.click()
		self.element1.send_keys("10")
		self.element2 = self.driver.find_element(By.XPATH, "//*[@id='cpar2']")
		self.element2.click()
		self.element2.send_keys("5")
		self.driver.find_element(By.XPATH, "//*[@id='content']/table[1]/tbody/tr[2]/td/input[2]").click();
		result = self.driver.find_element(By.XPATH, "//*[@id='content']/p[2]/font/b").text
		self.assertEqual("0.5", result)

    
     
if __name__ == "__main__":
	unittest.main()