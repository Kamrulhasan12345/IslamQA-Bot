import grequests as requests

from bs4 import BeautifulSoup


async def fetchQuest(url):
  r = (requests.get(u) for u in url.split("\n"))
  page = requests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  section = soup.find(class_="single_fatwa__question")
  question = section.find('p').get_text()[0:200] + '...'
  return question
  
async def fetchTitle(url):
  r = (requests.get(u) for u in url.split("\n"))
  page = requests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  return soup.title.text
  
async def fetchCategories(url):
  r = (requests.get(u) for u in url.split("\n"))
  page = requests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  a = soup.find_all('a', class_='card post-card')
  p = [text.getText().replace('\n', '') for text in soup.find_all('p', class_='card-title')]
  href = [link['href'] for link in a]
  answers = list(zip(p, href)) + [soup.title.text]
  return answers
  
async def fetchImportantTopics(url):
  r = (requests.get(u) for u in url.split("\n"))
  page = requests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  a = soup.find_all('a', class_='has-calligraphy-bg')
  p = [text.getText().replace("\n", "") for text in a]
  href = [link['href'] for link in a]
  title = soup.find_all('h2', class_='title')
  title = title[1].getText()
  topics = list(zip(p, href)) + [title]
  return topics

async def fetchArticles(url):
  r = (requests.get(u) for u in url.split("\n"))
  page = requests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  a = soup.find_all('a', class_='card post-card')
  p = [line.find('p', class_='card-title').getText().replace('\n', '') for line in a]
  href = [line['href'] for line in a]
  articles = list(zip(p, href)) + [soup.title.text]
  return articles

async def fetchArticle(url):
  r = (requests.get(u) for u in url.split("\n"))
  page = requests.map(r)[0]
  soup = BeautifulSoup(page.text, 'html.parser')
  p_ = soup.find_all('p', {"align":"JUSTIFY"})
  p = [line.getText().replace('\n', '') for line in p_]
  article = ''.join(p)[0:200].replace(u'\xa0', u' ') + '...'
  return article