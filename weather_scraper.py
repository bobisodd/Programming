from bs4.element import TemplateString
import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=weather+youngstown+ohio"
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")

current_temp = soup.find_all('div', class_={"class", 'BNeawe iBp4i AP7Wnd'})
print(f"The current temperature in youngstown ohio is {current_temp[0].text}")

for div in current_temp:
    print(div.text)
