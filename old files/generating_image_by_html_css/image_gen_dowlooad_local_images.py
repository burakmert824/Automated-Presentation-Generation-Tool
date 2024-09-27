from html2image import Html2Image
from file_functions import read_file, write_file
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
import os


# Dictionary to store cached image paths by URL
image_cache = {}

#download images and save them locally
def download_image(url, output_folder):
    global image_cache  # Use global variable to store cached image paths

    try:
        # Check if image URL is already cached
        if url in image_cache:
            return image_cache[url]

        response = requests.get(url, stream=True)
        if response.status_code == 200:
            # Get the file name from the URL
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            output_path = os.path.join(output_folder, filename)

            # Save the image locally if not already cached
            if not os.path.exists(output_path):
                with open(output_path, 'wb') as f:
                    f.write(response.content)
            
            # Cache the image path by URL
            image_cache[url] = os.path.abspath(output_path)
            return image_cache[url]
        else:
            print(f"Failed to download image from {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error downloading image from {url}: {str(e)}")
        return None

'''
replace web images with downlaoded images
'''
def replace_image_urls_with_local(html_content, output_folder):
    soup = BeautifulSoup(html_content, 'html.parser')
    img_tags = soup.find_all('img')
    
    for img_tag in img_tags:
        img_url = img_tag.get('src')
        if img_url:
            local_image_path = download_image(img_url, output_folder)
            if local_image_path:
                img_tag['src'] = local_image_path
    return str(soup)

hti = Html2Image()
component_name = 'hourly_guess'


html = read_file(f'{component_name}.html')
css  = read_file(f'{component_name}.css')


# Create a folder to store downloaded images
output_folder = 'downloaded_images'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# Replace image URLs with local paths
html_with_local_images = replace_image_urls_with_local(html, output_folder)

# Save the modified HTML content back to file if needed
write_file(file_path=f'{component_name}_modified.html', content=html_with_local_images)

# Screenshot the modified HTML with CSS
hti.screenshot(html_str=html_with_local_images, css_str=css, save_as=f'{component_name}.png', size=(800, 400))
