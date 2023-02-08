from bs4 import BeautifulSoup  as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service('D:\\chromedriver.exe')
service.start()

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)
driver.get('https://hh.ru/?customDomain=1')
# navigate to the page we need

search = driver.find_element(By.ID, 'a11y-search-input')
driver.implicitly_wait(3)
search.send_keys('python developer')
driver.find_element(By.CLASS_NAME, "bloko-button").click()
driver.implicitly_wait(5)

# extracting information
all_info = []
def extract_info(all_info: list):
    vacancys = driver.find_elements(By.CLASS_NAME, 'serp-item')
    for vacancy in vacancys:
        soup = BS(vacancy.get_attribute('outerHTML').encode('utf-8'), 'html.parser', from_encoding='utf-8')
        title = soup.select_one('.serp-item__title')
        link = title['href']
        salary = soup.select_one('span[data-qa="vacancy-serp__vacancy-compensation"]')
        company = soup.select_one('.bloko-link_kind-tertiary')
        total = (title, link, salary, company)
        all_info.append(total)


nextPage = driver.find_element(By.CSS_SELECTOR, '[data-qa="pager-next"]')

while nextPage:
    nextPage = driver.find_element(By.CSS_SELECTOR, '[data-qa="pager-next"]')
    nextPage.click()
