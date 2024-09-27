from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def find_element_by_xpath(driver, xpath, timeout=10, wait_after=0):
    """
    Find a web element using XPath in the given WebDriver instance.
    Wait for loading the element on the page
    
    Args:
    - driver (webdriver): The WebDriver instance (e.g., ChromeDriver).
    - xpath (str): XPath expression to locate the element.
    - timeout (int): Maximum time to wait for the element to be found (default: 10 seconds).
    
    Returns:
    - WebElement: The found WebElement object if found, else None.
    """
    try:
        # Wait until the element identified by XPath appears
        wait = WebDriverWait(driver, timeout)
        element = wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        
        # Wait for 1 second to ensure the element is fully loaded
        if(wait_after):
            time.sleep(wait_after)  

        return element
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return None


def cookie_closer(driver):
    try:
        cookie_class_name = 'home full-animation rfphrase-disabled'
        # Wait until the body element is present
        body_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.TAG_NAME, 'body'))
        )
        body_class = body_element.get_attribute('class')
        print(body_class)
        
        if(body_class == cookie_class_name):
            print('Cookie bulundu valla')
            return body_class
        # Find the child element containing the text "close"
        #close_element = element.find_element(By.XPATH, f".//*[contains(text(), '{text_to_find}')]")
        
        return body_class  #
        
    except Exception as e:
        print(f"Privacy policy banner not found or already closed. Error: {str(e)}")

# Example usage:
url = 'https://www.accuweather.com/'

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()
try :
    # Navigate to the URL
    driver.get(url)
    
    DAHA_FAZLASINI_GORUN_XPATH = '/html/body/div/div[6]/div[1]/div[1]/div[1]/p/a'
    DAHA_FAZLASINI_GORUN_BUTTON = find_element_by_xpath(driver, DAHA_FAZLASINI_GORUN_XPATH)
    if(DAHA_FAZLASINI_GORUN_BUTTON):
        DAHA_FAZLASINI_GORUN_BUTTON.click()
        print('Daha fazlasini gorun butonuna tiklandi')
    else:
        print('Daha fazlasini gorun butonu cikmadi')
        
    time.sleep(4) 
    #cookie_closer(driver = driver)

    # kocaeli ilcelerine git
    CITY_LIST_XPATH = '/html/body/div/div[7]/div[1]/div[1]/div[2]'
    table = find_element_by_xpath(driver, CITY_LIST_XPATH)
    items = table.find_elements(By.TAG_NAME, 'a')
    for item in items:
        city_name = item.text
        if(city_name == 'Kocaeli'):
            print('Kocaeli bulundu')
            item.click()    
            break
except Exception as e:
    print(f"Error: {str(e)}")

time.sleep(2)

ILCE_LIST_XPATH = '/html/body/div/div[7]/div[1]/div[1]/div[2]'
try:
    table = find_element_by_xpath(driver, ILCE_LIST_XPATH)
    print("table found")
    #print(table.text)
    table = table.find_element(By.TAG_NAME, 'a')
    for item in items:
        print(f"item = {item.text}")
    
except Exception as e:
    print(f"Error: {str(e)}")



time.sleep(1000)




# cookie_button = find_element_by_xpath(driver, '/html/body/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div', 5)
# time.sleep(1000)
# if(cookie_button):
#     cookie_button.click()
#     print('Cookie kabul edildi')
# else:
#     print('Cookie cikmadi')
    
    
    
driver.quit()