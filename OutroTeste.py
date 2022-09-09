# import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# import Action chains
from selenium.webdriver.common.action_chains import ActionChains
servico = Service(ChromeDriverManager().install())
# create webdriver object
driver = webdriver.Chrome(service=servico)

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(By.LINK_TEXT,"Courses")

# create action chain object
action = ActionChains(driver)

# click the item
action.click(on_element = element)

# perform the operation
action.perform()
sleep(5)