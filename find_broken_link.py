import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(chrome_options=options,
                          executable_path=r'C:\Users\hp\chromedriver.exe')
driver.get('https://pratapsharma.in/')
links = driver.find_elements_by_css_selector("a")
for link in links:
    r = requests.head(link.get_attribute('href'))
    # print(link.get_attribute('href'), r.status_code)  # All links with status code show
    if(r.status_code == 400 or r.status_code == 404):
        print(link.get_attribute('href'), r.status_code)
