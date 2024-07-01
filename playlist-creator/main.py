import requests
from bs4 import BeautifulSoup

year = input("Which year would you like to travel to? Type the date in YYYY-MM-DD format.")
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/"+year)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
print(soup.prettify())
