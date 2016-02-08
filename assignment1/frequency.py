import json
import string
import sys

class FrequencyCalculator:
  def __init__(self):
    self.all_frequency = 0
    self.terms_frequency = {}

  def print_frequencies(self):
    for key, value in self.terms_frequency.items():
      try:
        term_frequency = value/float(self.all_frequency)
        print("{key} {term_frequency}".format(**locals()))
      except UnicodeEncodeError as u:
        next


  def frequency(self, tweet):
    punct_table = dict((ord(char), None) for char in string.punctuation)
    terms = tweet.translate(punct_table).replace("\n", "").split(" ")
    
    for term in terms:
      lterm = term.lower()

      self.all_frequency += 1

      if lterm in self.terms_frequency:
        self.terms_frequency[lterm] += 1
      else:
        self.terms_frequency[lterm] = 1

def main():
  tweets_file = sys.argv[1]
  tweets = [line.rstrip("\n") for line in open(tweets_file)]
  calculator = FrequencyCalculator()

  for tweet in tweets:
    tweet_data =  json.loads(tweet)

    if 'text' in tweet_data:
      calculator.frequency(tweet_data['text'])

  calculator.print_frequencies()


if __name__ == '__main__':
    main()
