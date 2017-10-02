# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

#import stuff
import requests
from bs4 import BeautifulSoup

def read_file(file_path):
    with open(file_path) as csvFile:
        return [url.rstrip() for url in csvFile]

#create source_urls_list from csv
source_urls_list = read_file('/Users/haweber/Desktop/source_urls.csv')

#Fill a second list with triggers from a csv
triggers = read_file('/Users/haweber/Desktop/triggers.csv')

for source_url in source_urls_list:
    res = requests.get(source_url)

    #check if any of the triggers appear in scraped_data
    #using list comprehension. 
    matching = [trigger for trigger in triggers if trigger in res.text]
    if matching:
        print((source_url, matching))
