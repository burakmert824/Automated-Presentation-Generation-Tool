from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import os
import urllib.parse

def ensure_folder_exists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def download_css_files(url, output_folder):
    try:
        # Ensure output folder exists
        ensure_folder_exists(output_folder)

        # Setup Selenium Chrome webdriver using webdriver_manager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Open the website
        driver.get(url)

        # Get page source
        page_source = driver.page_source

        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(page_source, 'html.parser')

        # Find all CSS <link> elements
        css_links = soup.find_all('link', rel='stylesheet')

        # Download each CSS file
        for link in css_links:
            css_url = link.get('href')

            if css_url:
                # Create the output path
                parsed_url = urllib.parse.urlparse(css_url)
                filename = os.path.basename(parsed_url.path)
                output_path = os.path.join(output_folder, filename)

                # Download the CSS file
                response = requests.get(css_url)
                if response.status_code == 200:
                    with open(output_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Downloaded: {css_url} to {output_path}")
                else:
                    print(f"Failed to download: {css_url}. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        # Close the browser
        if driver:
            driver.quit()

# Example usage:
url = 'https://www.accuweather.com/tr/tr/izmir/318290/weather-forecast/318290'  # Replace with your desired URL
output_folder = 'css_files'  # Output folder to save downloaded CSS files
download_css_files(url, output_folder)
