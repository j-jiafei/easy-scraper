import logging

logger = logging.getLogger(__name__)

class Parser(object):
  """
  """
  @staticmethod
  def train(url, json):
    """ train produces a parser based on the url and json.
    One drawback is that the json sample file may be obsolete.
    """
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

  def parse(url):
    """
    """

  def _find_tag(soup, value):
    string = soup.find(text=value)
    if not string:
      string = soup.find(text=re.compile('.*' + value + '.*'))
    if not string:
      string = soup.find('a', href=value)
    return string

  def _allsame(tup):
    return min([i == tup[0] for i in tup] + [True])

  def _lca(tags):
    if not tags:
      return None
    paths = [list(tag.parents)[::-1] for tag in tags]
    m = [allsame(t) for t in zip(*paths)]
    m.append(False)
    lca_index = m.index(False) - 1
    return paths[0][lca_index] if lca_index >= 0 else None

  def _train_selector(tags, root=None):
    return ' > '.join([tag.name for tag in list(tags[0].parents)[::-1][2:]])
