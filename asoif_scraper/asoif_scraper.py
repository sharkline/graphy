#!/Users/le/.virtualenvs/graphy/bin/python
"""
Scraper to grab asoif links with comments, used later
for further scraping/analysis

To run: ./asoiaf_scraper.py
"""
import re
import sys
import click
import urllib2
import logging
import BeautifulSoup
from datetime import datetime

log = logging.basicConfig(__name__)

def _write_to_file(links):
    """
    Helper method, write the list to a file seperated by
    new lines
    """
    now = datetime.now()
    str_now = now.strftime('%Y_%m_%d')
    filename = '_'.join([str_now, 'asoif_dump.txt'])
    with open(filename, 'w') as outf:
        outf.write('\n'.join([topic for topic in links]))

def fetch_links(url='http://www.reddit.com/r/asoiaf', runs=10, retry=3):
    """
    Fetch the links of a given url, used to grab links for further
    scraping
    """
    if runs and retry:
        data = urllib2.urlopen(url).read()

        asoif_links = []
        bs = BeautifulSoup.BeautifulSoup(data)
        all_topics = bs.findAll('a')

        for topic in all_topics:
            asoif_links.append(topic)

        # Ugh...once this works refactor into something more
        # sane
        reddit_links = []
        for topic in bs.findAll('a'):
            current_topic = topic.get('href', None)
            if not current_topic is None:
                if current_topic.startswith('http://'):
                    if 'comments' in current_topic:
                        reddit_links.append(current_topic)
                    elif '?count' in current_topic:
                        _write_to_file(reddit_links)
                        runs -= 1
                        try:
                            fetch_links(url=current_topic, runs=runs)
                        except:
                            retry -= 1
                            fetch_links(url=current_topic, runs=runs, retry=retry)

if __name__ == '__main__':
    fetch_links()
