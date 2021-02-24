from bs4 import BeautifulSoup
import grequests as requests

# client = http3.AsyncClient()

async def fetchQuest(url):
  r = (grequests.get(u) for u in url.split("\n"))
  page = grequests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  section = soup.find(class_="single_fatwa__question")
  question = section.find('p').get_text()
  return question
  # return page.text