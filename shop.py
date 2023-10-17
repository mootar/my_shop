# 4 Goods page display
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(2)
driver.find_element_by_xpath("//img[@src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Mastering-HTML5-Forms-300x300.jpg']").click()  # Click "HTML 5 Forms"
time.sleep(1)
book_title = WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".summary.entry-summary"), "HTML5 Forms"))
driver.quit()

# 5 Goods amount in a category
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
# Start autotest
driver.find_element_by_link_text("My Account").click()  # Click "My Account"
time.sleep(2)
driver.find_element_by_id("username").send_keys("random@random.com")  # Input email
time.sleep(1)
driver.find_element_by_id("password").send_keys("RanD0MP@SSW0rD100500")  # Input password
time.sleep(1)
driver.find_element_by_name("login").click()  # Click "Login"
time.sleep(1)
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(1)
driver.find_element_by_xpath("//a[@href='https://practice.automationtesting.in/product-category/html/']").click()  # Click "HTML" category
time.sleep(1)
''' All of the method+locator combination below don't bear the correct result.
# goods_amount = driver.find_elements_by_css_selector("li a.add_to_cart_button")
# goods_amount = driver.find_elements_by_xpath("//a[@class='add_to_cart_button']")
# goods_amount = driver.find_elements_by_xpath("//li[@class='type-product']")
# goods_amount = driver.find_elements_by_css_selector("div li.type-product")
# goods_amount = driver.find_elements_by_css_selector("ul.products.masonry-done li.type-product")
# goods_amount = driver.find_elements_by_xpath("//*[@class='type-product']")
'''
goods_amount = driver.find_elements_by_css_selector("a > h3")  # This locator malfunctions as well.
if goods_amount == 3:
    print("Quantity of goods listed is ", len(goods_amount))
else:
    print("Quantity of goods listed is not 3.")
driver.quit()

# 6 Goods sorting
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

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
# Start autotest
driver.find_element_by_link_text("My Account").click()  # Click "My Account"
time.sleep(2)
driver.find_element_by_id("username").send_keys("random@random.com")  # Input email
time.sleep(1)
driver.find_element_by_id("password").send_keys("RanD0MP@SSW0rD100500")  # Input password
time.sleep(1)
driver.find_element_by_name("login").click()  # Click "Login"
time.sleep(1)
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(1)
sorting_type = WebDriverWait(driver, 2).until(
    EC.text_to_be_present_in_element((By.NAME, "orderby"), "Default sorting"))
time.sleep(1)
sorting = driver.find_element_by_class_name("orderby")
select = Select(sorting)
select.select_by_visible_text("Sort by price: high to low")  # Select "Sort by price: high to low"
time.sleep(1)
sorting_type = WebDriverWait(driver, 2).until(
    EC.text_to_be_present_in_element((By.NAME, "orderby"), "Sort by price: high to low"))
time.sleep(1)
driver.quit()

# 7 Goods display, price discount
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# Start autotest
driver.find_element_by_link_text("My Account").click()  # Click "My Account"
time.sleep(2)
driver.find_element_by_id("username").send_keys("random@random.com")  # Input email
time.sleep(1)
driver.find_element_by_id("password").send_keys("RanD0MP@SSW0rD100500")  # Input password
time.sleep(1)
driver.find_element_by_name("login").click()  # Click "Login"
time.sleep(1)
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(1)
driver.find_element_by_xpath("//img[@src='https://practice.automationtesting.in/wp-content/uploads/2017/01/Android-Quick-Start-Guide-300x300.png']").click()  # Click "Android Quick Start Guide"
time.sleep(1)
old_price = driver.find_element_by_css_selector(".price > del > span")
new_price = driver.find_element_by_css_selector(".price > ins > span")
old_price_text = old_price.text
new_price_text = new_price.text
assert old_price_text == "₹600.00"
assert new_price_text == "₹450.00"
preview = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//img[@title='Android Quick Start Guide']")))
preview.click()
preview_close = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
preview_close.click()
time.sleep(1)
driver.quit()

# 8 Price check in the cart
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# Start autotest
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(1)
driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']").click()  # Click "Add to basket"
time.sleep(1)
item_count = driver.find_element_by_css_selector("span.cartcontents")
total_price = driver.find_element_by_css_selector("ul:nth-child(1)  span.amount")
item_count_text = item_count.text
total_price_text = total_price.text
assert item_count_text == "1 Item"
assert total_price_text == "₹180.00"
driver.find_element_by_css_selector(".wpmenucart-contents").click()  # Open Cart
time.sleep(1)
# subtotal = driver.find_element_by_css_selector("table tbody span")
subtotal_check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, "//td[@data-title='Subtotal']"), total_price_text))
total_check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.cart_totals strong"), "₹183.60"))
driver.quit()

# 9 Working in cart
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
# Start autotest
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']").click()  # Click "Add to basket"
time.sleep(1)
driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=180']").click()  # Click "Add to basket"
time.sleep(1)
driver.find_element_by_css_selector(".wpmenucart-contents").click()  # Open Cart
time.sleep(1)
driver.find_element_by_css_selector(".cart tbody a").click()  # Delete 1st book
time.sleep(1)
driver.find_element_by_css_selector(".woocommerce-message a").click()  # Undo
time.sleep(1)
driver.find_element_by_css_selector(".cart_item:nth-child(2) input").clear()
time.sleep(1)
driver.find_element_by_css_selector(".cart_item:nth-child(2) input").send_keys(3)
time.sleep(1)
driver.find_element_by_name("update_cart").click()  # Update cart
time.sleep(2)
second_book_count = driver.find_element_by_css_selector(".cart_item:nth-child(2) input")
second_book_count_value = second_book_count.get_attribute("value")
assert second_book_count_value == "3", "Not 3!?"
driver.find_element_by_name("apply_coupon").click()  # Apply coupon
msg_check = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-error li"), "Please enter a coupon code."))
time.sleep(1)
driver.quit()

# 10 Buy goods
# Load website
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

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
# Start autotest
driver.find_element_by_link_text("Shop").click()  # Click "Shop"
time.sleep(1)
driver.execute_script("window.scrollBy(0, 300);")
driver.find_element_by_xpath("//a[@href='/shop/?add-to-cart=182']").click()  # Click "Add to basket"
time.sleep(1)
driver.find_element_by_css_selector(".wpmenucart-contents").click()  # Open Cart
time.sleep(1)
checkout = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "a.checkout-button")))
checkout.click()
driver.find_element_by_id("billing_first_name").send_keys("Random1")  # Input first name
driver.find_element_by_id("billing_last_name").send_keys("Random2")  # Input last name
driver.find_element_by_id("billing_email").send_keys("Random@random.com")  # Input email
driver.find_element_by_id("billing_phone").send_keys("9876543210")  # Input phone
driver.find_element_by_css_selector(".country_to_state a").click()
driver.find_element_by_xpath("//input[@id='s2id_autogen1_search']").send_keys("Kaza")
driver.find_element_by_css_selector("div.select2-result-label").click()
driver.find_element_by_id("billing_address_1").send_keys("Random place")  # Input address
driver.find_element_by_id("billing_city").send_keys("Random city")  # Input city
driver.find_element_by_id("billing_state").send_keys("Random state")  # Input state
driver.find_element_by_id("billing_postcode").send_keys("100500")  # Input postcode
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
payment_check = driver.find_element_by_css_selector("li.payment_method_cheque input")
payment_check.click()  # Pick "Check payments" radiobutton
place_order_button = driver.find_element_by_id("place_order")
place_order_button.click()  # Click "Place order"
notification = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
payment_type = WebDriverWait(driver, 5).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot tr:nth-child(3) td"), "Check Payments"))
time.sleep(1)
driver.quit()