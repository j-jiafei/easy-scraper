import logging
import sys
import urllib2
import re
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def produce(url, sample):
  if not url or not sample:
    logger.error('Invalid input')
    return
  result = urllib2.urlopen(url)
  if not result:
    logger.error('Cannot open the url')
    return
  soup = BeautifulSoup(result)
  taglist = [[find_tag(soup, value) for value in item.values()] \
      for item in sample]
  logger.debug(taglist)
  lcas = [lca(tagset) for tagset in taglist]
  logger.debug(lcas)
  item_selector = train_selector(lcas, root=None)
  if not item_selector:
    logger.error('Cannot train an item selector')
    return None
  for item in soup.select(item_selector):
    print item.prettify()
  return

def find_tag(soup, value):
  string = soup.find(text=value)
  if not string:
    string = soup.find(text=re.compile('.*' + value + '.*'))
  if not string:
    string = soup.find('a', href=value)
  return string

def allsame(tup):
  return min([i == tup[0] for i in tup] + [True])

def lca(tags):
  if not tags:
    return None
  paths = [list(tag.parents)[::-1] for tag in tags]
  m = [allsame(t) for t in zip(*paths)]
  m.append(False)
  lca_index = m.index(False) - 1
  return paths[0][lca_index] if lca_index >= 0 else None

def train_selector(tags, root=None):
  return ' > '.join([tag.name for tag in list(tags[0].parents)[::-1][2:]])

if __name__ == '__main__':
  logger.setLevel(logging.DEBUG)
  logging.basicConfig()
  url = 'https://news.ycombinator.com/'
  sample = [
    {
      "title": "How to lose $172,222 a second for 45 minutes",
      "url": "http://pythonsweetness.tumblr.com/post/64740079543/how-to-lose-172-222-a-second-for-45-minutes",
      "link": "pythonsweetness.tumblr.com"
    },
    {
      "title": "Dawn of Autonomous Corporations, Powered by Bitcoin",
      "url": "http://btcgeek.com/dawn-of-autonomous-corporations/",
      "link": "btcgeek.com"
    }
  ]
  produce(url, sample)
