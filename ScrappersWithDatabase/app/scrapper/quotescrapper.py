import requests
from bs4 import BeautifulSoup
from app.core.logger import logger

def scarpedata():
  logger.info("Scrapping Starts Starts")
  response = requests.get("https://quotes.toscrape.com")
  logger.info("Parsing HTML")
  soup = BeautifulSoup(
    response.text,
    "html.parser"
  )
  logger.info("finding all quotes")
  allquoutes = soup.find_all("div",class_="quote")
  data = [];
  for quote in allquoutes:
    quotetext = quote.find("span",class_="text")
    quoteauthor = quote.find("small",class_="author")
    taglist = quote.find_all("a",class_="tag")
    tags = [tag.text for tag in taglist]
    data.append({
      "quotetext":quotetext.text,
      "quoteauthor":quoteauthor.text,
      "tags":tags
    })
  return data