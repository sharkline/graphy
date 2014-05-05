import re
import sys
import urllib2
import BeautifulSoup
from datetime import datetime

def main():
    url = 'http://reddit.com/r/asoiaf'
    data = urllib2.urlopen(url).read()

    bs = BeautifulSoup.BeautifulSoup(data)
    topics_title = bs.find('a', {'class':'may-blank'})
    all_topics = [s.getText().strip() for s in topics_title.findAll('li')]

    now = datetime.now()
    str_now = now.strftime('%Y %m %d')
    filename = '_'.join([str_now, 'asoif_dump.txt'])
    with open(filename, 'w') as outf:
        outf.write('\n'.join(all_topics))

if __name__ == '__main__':
    main()
