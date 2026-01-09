import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

data = []
total_words = 0

headers = {"User-Agent": "Mozilla/5.0"}

# 🌍 Multiple travel blog sources
base_urls = {
    "NomadicMatt": "https://www.nomadicmatt.com/travel-blog/",
    "BlondeAbroad": "https://theblondeabroad.com/blog/",
    "ExpertVagabond": "https://expertvagabond.com/blog/",
    "DanFlyingSolo": "https://www.danflyingsolo.com/category/travel/"
}

def get_article_links(base_url):
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", href=True)
    article_links = []

    for link in links:
        href = link['href']
        if href.startswith("http") and "travel" in href:
            article_links.append(href.split("?")[0])

    return list(set(article_links))


def extract_text(article_url):
    response = requests.get(article_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    paragraphs = soup.find_all("p")
    text = " ".join(p.get_text() for p in paragraphs)

    return text, len(text.split())


for source, url in base_urls.items():
    print(f"\n🔍 Scraping from {source}")
    article_urls = get_article_links(url)

    for article in article_urls:
        if total_words >= 80000:
            break

        try:
            text, wc = extract_text(article)

            if wc > 400:
                data.append({
                    "source": source,
                    "url": article,
                    "content": text,
                    "word_count": wc
                })

                total_words += wc
                print(f"{source} | {wc} words | Total: {total_words}")

            time.sleep(2)

        except:
            pass

    if total_words >= 80000:
        break


df = pd.DataFrame(data)
df.to_csv("travel_blog_corpus.csv", index=False)

print("\n✅ DONE")
print("Total words collected:", total_words)
