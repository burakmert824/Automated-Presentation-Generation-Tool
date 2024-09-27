from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

from file_functions import read_file, write_file

def print_element_html(url, xpath):
    # Setup Selenium Chrome webdriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Open the website
        driver.get(url)
        print('waiting')
        # Wait until the element with the specified class appears
        wait = WebDriverWait(driver, 5)  # Adjust timeout as needed
        element = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        # code wait one second
        time.sleep(2)
        
        element.screenshot('selenuim.png')
        
        print('waiting ended')
        # Once element is found, print its HTML content
        print(element.get_attribute('outerHTML'))
        return element.get_attribute('outerHTML')
    except Exception as e:
        print(f"Error: {str(e)}")
    
    finally:
        # Close the browser
        driver.quit()

# Example usage:
url = 'https://www.accuweather.com/tr/tr/izmir/318290/weather-forecast/318290'  # Replace with your desired URL
xpath = '/html/body/div/div[7]/div[1]/div[1]/a[1]'  # Replace with the desired class name
html = print_element_html(url, xpath)
write_file(file_path='element.html', content=html)

