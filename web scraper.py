import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup

driver_path = "C:/Users/AHMED/OneDrive/Desktop/MOD 3/CIS 403 Python aPPLICATION/WEEK 17/web_scraping/msedgedriver.exe"

service = Service(driver_path)
driver = webdriver.Edge(service=service)

url = "https://oxylabs.io/blog"
driver.get(url)

results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

headings = soup.find_all(['p'])

for heading in headings:
    title = heading.get_text(strip=True)
    if title not in results:
        results.append(title)

df = pd.DataFrame({'All Text': results})
df.to_csv('text.csv', index=False, encoding='utf-8')