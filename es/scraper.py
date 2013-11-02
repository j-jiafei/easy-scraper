class Scraper(object):
  """ a scraper object is composed of a parser and a url_generator.
  """
  @staticmethod
  def train(json, url):
    """ produces a scraper based on the sample file and url.
    """

  def __init__(self, parser, url_generator):
    self.parser = parser
    self.url_generator = url_generator
