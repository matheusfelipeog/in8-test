from pprint import pprint

from app import scraper

print('Scraper started, please wait...')
pprint(scraper.run(), indent=4)
