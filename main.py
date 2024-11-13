from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is in PATH
wait = WebDriverWait(driver, 10)

# Open Amazon India
driver.get("https://www.amazon.in")

try:
   
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("football")
    search_box.send_keys(Keys.RETURN)

   
    footballs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")))
    footballs[3].find_element(By.TAG_NAME, "a").click() 

   
    driver.switch_to.window(driver.window_handles[-1])

    add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    time.sleep(2)  

    cart_button = wait.until(EC.presence_of_element_located((By.ID, "nav-cart-count-container")))
    cart_button.click()


    quantity_dropdowns = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.a-dropdown-container .a-native-dropdown")))
    if quantity_dropdowns:
        driver.execute_script("arguments[0].scrollIntoView(true);", quantity_dropdowns[0])
        driver.execute_script("arguments[0].click();", quantity_dropdowns[0])
        quantity_option = wait.until(EC.presence_of_element_located((By.XPATH, "//li[@role='option']/a[text()='2']")))
        driver.execute_script("arguments[0].click();", quantity_option)
        time.sleep(2)


    driver.get("https://www.amazon.in")
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("MRF bat")
    search_box.send_keys(Keys.RETURN)

    bats = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")))
    bats[0].find_element(By.TAG_NAME, "a").click()  

    driver.switch_to.window(driver.window_handles[-1])

    add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    time.sleep(2)

    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    delete_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//input[@value='Delete']")))
    delete_buttons[0].click() 
    time.sleep(2)

    driver.get("https://www.amazon.in")
    search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))
    search_box.send_keys("Bhagavad Gita")
    search_box.send_keys(Keys.RETURN)

    books = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.s-main-slot div[data-component-type='s-search-result']")))
    books[0].find_element(By.TAG_NAME, "a").click() 

    driver.switch_to.window(driver.window_handles[-1])

    add_to_cart_button = wait.until(EC.presence_of_element_located((By.ID, "add-to-cart-button")))
    add_to_cart_button.click()
    time.sleep(2)


    driver.get("https://www.amazon.in/gp/cart/view.html?ref_=nav_cart")
    total_price_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span#sc-subtotal-amount-activecart .a-size-medium")))
    total_price = total_price_element.text
    print("Total Price in Cart:", total_price)

finally:
    time.sleep(20) 
    driver.quit()
