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



# Example usage:
url = 'https://www.accuweather.com/tr/tr/izmir/318290/weather-forecast/318290'

# Initialize WebDriver (e.g., Chrome)
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)
time.sleep(1)  # Adjust wait time as needed

####### Closing the cookie banner #######
COOKIE_XPATH = '//*[@id="privacy-policy-banner"]/div/div'
try:
    accept_button = find_element_by_xpath(driver, COOKIE_XPATH)
    accept_button.click()    
except Exception as e:
    print(f"Privacy policy banner not found or already closed. Error: {str(e)}")
#########################################



######### Find Current Data And Give Screenshot#############

CURRENT_WEATHER_XPATH = '/html/body/div/div[7]/div[1]/div[1]/a[1]'

# Find element by XPath
element = find_element_by_xpath(driver, CURRENT_WEATHER_XPATH)
# Take screenshot of the current weather element
element.screenshot('current_weather.png')

###########################################################

######## Find Next Days Weather And Give Screenshot########

NEXT_DAYS_WEATHER_XPATH = '/html/body/div/div[7]/div[1]/div[1]/div[2]'

element = find_element_by_xpath(driver, NEXT_DAYS_WEATHER_XPATH,wait_after=1)

element.screenshot('next_days_weather.png')



if element:
    print(f"Element found: {element}")
    element.screenshot('element.png')
    # Further actions with the found element (e.g., element.text, element.click(), etc.)
else:
    print("Element not found.")

# Close the browser
driver.quit()
