import requests
from bs4 import BeautifulSoup

def get_ranking(url, keywords):
    rankings = {}
    for keyword in keywords:
        search_url = "https://www.google.com/search?q=" + keyword
        response = requests.get(search_url)
        soup = BeautifulSoup(response.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True) if a.text]
        try:
            rankings[keyword] = links.index(url) + 1
        except ValueError:
            rankings[keyword] = "Not found"
    return rankings

if __name__ == "__main__":
    url = input("Enter the website URL: ")
    keywords = input("Enter a list of keywords separated by commas: ").split(",")
    rankings = get_ranking(url, keywords)
    for keyword, ranking in rankings.items():
        print(f"{keyword}: {ranking}")

