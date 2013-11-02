""" CLI for EasyScraper
"""

import argparse
import logging
import json
import es
from scraper import Scraper

logger = logging.getLogger(__name__)

def es():
  """ The function parses the arguments, train the scraper,
  and generates the output based on the arguments. """
  parser = argparse.ArgumentParser()
  parser.add_argument("sample", help="the sample file name")
  parser.add_argument("url", help="the url of the page to be parsed")
  args = parser.parse_args()
  logger.debug(args)
  scraper = Scraper.train(json=args.sample, url=args.url)
  if scraper is None:
    logger.error("A scraper cannot be trained.")
    return
  result = scraper.parse(url=args.url)
  logger.debug(json.dumps(result))


if __name__ == "__main__":
  logging.basicConfig()
  logger.setLevel(logging.DEBUG)
  es()
