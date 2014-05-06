import re
import sys
import urllib2
import BeautifulSoup
from datetime import datetime

def main():
    url = 'http://www.reddit.com/r/asoiaf/'
    data = urllib2.urlopen(url).read()
    
    asoif_links = []
    bs = BeautifulSoup.BeautifulSoup(data)
    all_topics = bs.findAll('a')
    for topic in all_topics:
        asoif_links.append(topic)

    all_topics = [topic.get('href') for topic in bs.findAll('a')]

    now = datetime.now()
    str_now = now.strftime('%Y %m %d')
    filename = '_'.join([str_now, 'asoif_dump.txt'])
    with open(filename, 'w') as outf:
        outf.write('\n'.join([topic for topic in all_topics]))

if __name__ == '__main__':
    main()
