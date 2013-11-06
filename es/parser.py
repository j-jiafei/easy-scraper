# local
# library
import logging
from bs4 import BeautifulSoup
import re

logger = logging.getLogger(__name__)

class Parser(object):
  """
  """
  @staticmethod
  def train(html, sample):
    """ html is a stream of html text, and sample is given by user for the
    page. The method returns a parser which can parse similar page as html, and
    returns complete data items beside sample.
    """
    logger.info("Starting training a parser")
    soup = BeautifulSoup(html)
    taglist = [[Parser.find_tag(soup, value) for value in item.values()] \
        for item in sample if item is not None]
    logger.debug(taglist)
    lcas = [Parser.lca(tagset) for tagset in taglist if tagset is not None]
    logger.debug(lcas)
    item_selector = Parser.train_selector(lcas, root=None)
    if not item_selector:
      logger.error('Cannot train an item selector')
      return None
    for item in soup.select(item_selector):
      print item.prettify()
    return Parser()

  def parse(html):
    """ html is a stream of html text. The method returns a list of items
    parsed from thml.
    """
    logger.info("Starting parsing a html")
    pass

  def __init__(self):
    pass

  @staticmethod
  def find_tag(soup, value):
    string = soup.find(text=value)
    if not string:
      string = soup.find(text=re.compile('.*' + value + '.*'))
    if not string:
      string = soup.find('a', href=value)
    return string

  @staticmethod
  def allsame(tup):
    return min([i == tup[0] for i in tup] + [True])

  @staticmethod
  def lca(tags):
    if not tags:
      return None
    paths = [list(tag.parents)[::-1] for tag in tags if tag is not None]
    m = [Parser.allsame(t) for t in zip(*paths)]
    m.append(False)
    lca_index = m.index(False) - 1
    return paths[0][lca_index] if lca_index >= 0 else None

  @staticmethod
  def train_selector(tags, root=None):
    if not tags or not tags[0]:
      return None
    return ' > '.join([tag.name for tag in list(tags[0].parents)[::-1][2:]])
