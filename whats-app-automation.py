from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()

driver.get('http://web.whatsapp.com')

input('Scan QR code an press any key: ')
RK = driver.find_element_by_css_selector('span[title]="RK"]')
RK.click()

# Change this path to relevant information from What's app
testinput = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/..')

testinput.send_keys('Happy birthday')
testinput.send_keys(keys.RETURN)