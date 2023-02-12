# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36", "X-Forwarded-For": "123.456.789.0"}
# nextPage = driver.find_element(By.CSS_SELECTOR, '[data-qa="pager-next"]')
# while nextPage:
    #     nextPage = driver.find_element(By.CSS_SELECTOR, '[data-qa="pager-next"]')
    #     nextPage.click()
    #     extract_info(all_info)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome('D:\\chromedriver.exe')

driver.get('https://hh.ru/vacancies/python-developer?page=0')

print(driver.find_element(By.CLASS_NAME, 'bloko-button_pressed').find_element(By.TAG_NAME, 'span').text)

driver.quit()