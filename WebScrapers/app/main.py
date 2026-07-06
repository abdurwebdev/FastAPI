# import requests
# from bs4 import BeautifulSoup


# url = "https://quotes.toscrape.com"

# response = requests.get(url)

# soup = BeautifulSoup(response.text,"html.parser")
# quote = soup.find("span",class_='text')
# print(quote.text)

import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")

soup = BeautifulSoup(response.text,"html.parser")

quotes = soup.find_all("span",class_="text")

for quote in quotes:
  print(quote.text)
  
authors = soup.find_all("small",class_="author")

scrapped_data = []

for author in authors:
  print(author.text)
  
quote_divs = soup.find_all("div",class_="quote")

for quote in quote_divs:
  text = quote.find("span",class_="text").text
  author = quote.find("small",class_="author").text
  scrapped_data.append({
    "text":text,
    "author":author
  })

print(f"Number of quotes: {len(scrapped_data)}")
print(scrapped_data)