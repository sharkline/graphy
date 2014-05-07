import re
import sys
import click
import urllib2
import BeautifulSoup
from datetime import datetime

@click.command()
@click.option('--url', default='http://www.reddit.com/r/asoiaf',
              help='Parse links in this url')
def main(url):
    data = urllib2.urlopen(url).read()
    
    asoif_links = []
    bs = BeautifulSoup.BeautifulSoup(data)
    all_topics = bs.findAll('a')
    print 'fetched topics'
    for topic in all_topics:
        asoif_links.append(topic)

    reddit_links = []
    for topic in bs.findAll('a'):
        current_topic = topic.get('href', None)
        if not current_topic is None:
            if 'comments' in current_topic and current_topic.startswith('http://'):
                reddit_links.append(current_topic)
    
    now = datetime.now()
    str_now = now.strftime('%Y_%m_%d')
    filename = '_'.join([str_now, 'asoif_dump.txt'])
    with open(filename, 'w') as outf:
        outf.write('\n'.join([topic for topic in reddit_links]))

if __name__ == '__main__':
    main()
