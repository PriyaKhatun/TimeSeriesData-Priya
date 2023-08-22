from scraper import MyScraper

if __name__ == '__main__':
    url = 'scraper_output.csv''
    scraper = MyScraper(url)
    scraped_titles, scraped_links = scraper.scrape()
    scraper.save_to_csv(scraped_titles, scraped_links)
    print('Data extracted and saved to CSV.')
