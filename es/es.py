""" CLI for EasyScraper
"""

# local
from parser import Parser
# library
import argparse
import logging
import json
import urllib2

logger = logging.getLogger(__name__)

def es():
  """ The function parses the arguments, train the scraper,
  and generates the output based on the arguments. """
  cmd_parser = argparse.ArgumentParser()
  cmd_parser.add_argument("sample", help="the sample file name")
  cmd_parser.add_argument("url", help="the url of the page to be parsed")
  args = cmd_parser.parse_args()
  try:
    html = urllib2.urlopen(args.url)
  except urllib2.URLError:
    logger.error("Cannot open url: " + args.url)
    return
  sample_file = open(args.sample)
  sample = json.load(sample_file)
  parser = Parser.train(html, sample)


if __name__ == "__main__":
  logging.basicConfig()
  logging.getLogger().setLevel(logging.DEBUG)
  es()
