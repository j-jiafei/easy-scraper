class Scraper(object):
  """ a scraper object is composed of a parser and a url_generator.
  """
  @staticmethod
  def train(sample_json):
    """ train produces a scraper object based on the sample_json.
    """
    url = sample_json["url"]
    sample = sample_json["sample"]

  def __init__(self, parser, url_generator):
    self.parser = parser
    self.url_generator = url_generator
