from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


PATH = './chromedriver'
driver = webdriver.Chrome(PATH)

#URL = 'https://www.techwithtim.net/'
#URL = 'https://www.youtube.com'
#URL = 'https://nairaland.com'
URL = 'https://orteil.dashnet.org/cookieclicker/'

driver.get(URL)

driver.implicitly_wait(5)
print(driver.title)
# #search = driver.find_element_by_name("q")
# search = driver.find_element(By.XPATH, '//input[@id="search"]')
# search.send_keys("vevo")
# search.send_keys(Keys.ENTER)

# try:
#     div = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//div[@id="contents" and @class="style-scope ytd-item-section-renderer"]'))
#     )
#     print(div.text)
#     driver.find_e
# except:
#     driver.quit()


english = driver.find_element(By.ID, 'langSelect-EN')
english.click()

cookie = driver.find_element(By.ID, 'bigCookie')
cookies_count = driver.find_element(By.ID, 'cookies')
items = [driver.find_element(By.ID, 'productPrice' + str(i)) for i in range(1, -1, -1)]




actions = ActionChains(driver)
actions.click(cookie)
 

print('checking')

for i in range(5000):
    actions.perform()
    count = int(cookies_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
