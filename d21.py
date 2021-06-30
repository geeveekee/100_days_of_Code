from bs4 import BeautifulSoup
import requests

print("Returns to you the article with the most votes on yconbinator news, and the link to that article!")

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name='a', attrs='storylink')
article_texts_list = []
article_links_list = []
for article_tag in articles:
    article_text = article_tag.get_text()
    article_texts_list.append(article_text)
    article_link = article_tag.get("href")
    article_links_list.append(article_link)

article_upvote_list = [int(score.get_text().split()[0]) for score in soup.select(selector=".score")]

#print(article_texts_list)
#print(article_links_list)
#print(article_upvote_list)

best_article = article_upvote_list.index(max(article_upvote_list))

print(article_texts_list[best_article])
print(article_links_list[best_article])
print(article_upvote_list[best_article])




