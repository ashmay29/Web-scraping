import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/tv/features/best-tv-shows/"
response = requests.get(url=URL)
website_html = response.text
soup = BeautifulSoup(website_html,"html.parser")
all_tvshows = soup.findAll(name="h2")
titles = [show.getText() for show in all_tvshows][::-1]
with open('Top100tvshows.txt',mode="w") as file:
    for movie in titles:
        file.write(f"{movie}\n")