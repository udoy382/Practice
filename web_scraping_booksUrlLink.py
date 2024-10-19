import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from openpyxl import Workbook
from multiprocessing import Pool
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def scrape_website(url):
    session = requests.Session()
    retry_strategy = Retry(total=5, backoff_factor=2, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    try:
        response = session.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        books = soup.select('.product_pod')[:1000]

        data = []
        for book in books:
            title = book.h3.a['title']
            book_url = urljoin(url, book.h3.a['href'])
            data.append((title, book_url))

        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while scraping {url}: {e}")
        return []

if __name__ == '__main__':
    websites = ['http://books.toscrape.com', 'http://example.com', 'http://anotherwebsite.com']

    workbook = Workbook()
    sheet = workbook.active
    sheet['A1'] = 'Title'
    sheet['B1'] = 'URL'

    with Pool(processes=len(websites)) as pool:
        results = pool.map(scrape_website, websites)

    for index, website_data in enumerate(results, start=2):
        for title, book_url in website_data:
            sheet[f'A{index}'] = title
            sheet[f'B{index}'] = book_url
            index += 1

    workbook.save('book_data3.xlsx')
