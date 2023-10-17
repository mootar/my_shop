# 1 Add a comment
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

path_to_extension = r'C:\Users\mikek\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\5.11.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/chromedriver.exe')
first_browser_tab = driver.window_handles[0]
time.sleep(3)
driver.switch_to.window(first_browser_tab)  # Switch to 1st tab
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://practice.automationtesting.in/")
first_tab = driver.current_window_handle
# Close Adblock extra tab
second_tab = driver.window_handles[1]
driver.switch_to.window(second_tab)
driver.close()
driver.switch_to.window(first_tab)
# # Start autotest
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(1)
driver.find_element_by_xpath("//a[@href='https://practice.automationtesting.in/product/selenium-ruby/']").click()  # Click "Selenium Ruby"
time.sleep(1)
driver.execute_script("window.scrollBy(0, 600);")
driver.find_element_by_xpath("//a[@href='#tab-reviews']").click()  # Click "Reviews"
time.sleep(1)
driver.find_element_by_css_selector(".star-5").click()  # Click "5 stars"
time.sleep(1)
driver.find_element_by_id("comment").send_keys("Nice book!")  # Input review text
time.sleep(1)
driver.find_element_by_id("author").send_keys("Random")  # Input name
time.sleep(1)
driver.find_element_by_id("email").send_keys("Random@random.com")  # Input email
time.sleep(1)
driver.find_element_by_id("submit").click()  # Click "Submit"
time.sleep(1)
driver.quit()