"""
"""

import argparse
import logging
import json
import es
from scraper import Scraper

logger = logging.getLogger(__name__)

def cmd():
  parser = argparse.ArgumentParser()
  parser.add_argument("sample")
  args = parser.parse_args()
  sample = args.sample
  sample_file = open(sample, "r")
  sample_json = json.load(sample_file)
  scraper = Scraper.train(sample_json)

  page_parser = es.produce(url, sample)
  results = page_parser.parse(url)
  logger.debug(json.dumps(results))

if __name__ == "__main__":
  logging.basicConfig()
  logger.setLevel(logging.DEBUG)
  cmd()
