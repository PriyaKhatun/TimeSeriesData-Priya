import requests
from bs4 import BeautifulSoup
import csv
import os

class MyScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        titles = soup.find_all('h2', class_='news-title')
        links = [title.a['href'] for title in titles]
        return titles, links

    def save_to_csv(self, titles, links):
        csv_filename = 'scraper_output.csv'
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['Title', 'Link'])
            for title, link in zip(titles, links):
                csv_writer.writerow([title.text, link])

if __name__ == '__main__':
    scraper = MyScraper('scraper_output.csv'')
    scraped_titles, scraped_links = scraper.scrape()
    scraper.save_to_csv(scraped_titles, scraped_links)
