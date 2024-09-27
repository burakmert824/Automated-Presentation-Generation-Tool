
from html2image import Html2Image
from file_functions import read_file, wrap_with_dimensions, write_file


hti = Html2Image()
component_name = 'element'

html = read_file(f'{component_name}.html')
#css  = read_file(f'{component_name}.css')
# screenshot an HTML string (css is optional)
#hti.screenshot(html_str= html,css_str=css,  save_as=f'{component_name}.png',size=(800, 400))
hti.screenshot(html_str= html, save_as=f'{component_name}.png',size=(800, 400))