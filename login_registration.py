# 2 Account Registration
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
driver.find_element_by_link_text("My Account").click()  # Click "My Account"
time.sleep(2)
driver.find_element_by_id("reg_email").send_keys("random@random.com")  # Input email
time.sleep(1)
driver.find_element_by_id("reg_password").send_keys("RanD0MP@SSW0rD100500")  # Input password
time.sleep(1)
driver.find_element_by_name("register").click()  # Click "Register"
time.sleep(1)
driver.quit()

# 3 System authorization
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
driver.find_element_by_link_text("My Account").click()  # Click "My Account"
time.sleep(2)
driver.find_element_by_id("username").send_keys("random@random.com")  # Input email
time.sleep(1)
driver.find_element_by_id("password").send_keys("RanD0MP@SSW0rD100500")  # Input password
time.sleep(1)
driver.find_element_by_name("login").click()  # Click "Login"
time.sleep(1)
driver.quit()