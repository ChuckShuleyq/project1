from bs4 import BeautifulSoup  as BS
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
def HH(programming_language: str, city: str):
    service = Service('D:\\chromedriver.exe')
    c = 0
    service.start()

    driver = webdriver.Chrome(service=service)
    driver.get(f'https://{city}.hh.ru/?customDomain=1')
    try: 
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "HH-React-Root"))
        )
        search = element.find_element(By.ID, 'a11y-search-input')
        search.send_keys(f'{programming_language} developer')


        driver.find_element(By.CLASS_NAME, "bloko-button").click()
        current_url = driver.current_url
        driver.get(f'{current_url}?page=0')

        # extracting information
        all_info = []
        def extract_info(all_info: list):
            vacancys = driver.find_elements(By.CLASS_NAME, 'serp-item')
            for vacancy in vacancys:
                item = vacancy.get_attribute('outerHTML')
                item = item.replace("&nbsp;",' ').replace('\u202f', ' ').encode('utf-8')
                soup = BS(item, 'html.parser')
                title = soup.select_one('.serp-item__title')
                link = title['href']
                salary = soup.select_one('span[data-qa="vacancy-serp__vacancy-compensation"]')
                company = soup.select_one('.bloko-link_kind-tertiary')
                if salary:
                    try:
                        total = (title.text, link, salary.text, company.text)
                    except AttributeError:
                        continue
                else:
                    try:
                        total = (title.text, link, '' , company.text)
                    except AttributeError:
                        continue
                all_info.append(total)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "HH-React-Root"))
        )
        extract_info(all_info)
        next_page = driver.find_element(By.CSS_SELECTOR, '[data-qa="pager-next"]')
        while next_page:
            next_page = driver.find_element(By.CSS_SELECTOR, '[data-qa="pager-next"]')
            c += 1
            driver.get(f'{current_url}?page={c}')
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "HH-React-Root"))
            )
            extract_info(all_info)
    except NoSuchElementException:
        print(all_info)
    finally:
        driver.quit()