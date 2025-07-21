from selenium import webdriver
from selenium.webdriver.safari.service import Service
from selenium.webdriver.safari.options import Options

# Enable Remote Automation in Safari once (in Terminal):
#    /usr/bin/safaridriver --enable

options = Options()
service = Service()  # No need to pass executable_path

driver = webdriver.Safari(options=options, service=service)
driver.get("https://www.google.com")

act_title = driver.title
exp_title = "Google"

if act_title == exp_title:
    print("Test passed ✅")
else:
    print("Test failed ❌ (got title: %r)" % act_title)

driver.quit()
