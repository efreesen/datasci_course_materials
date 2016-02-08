import json
import string
import sys

class SentimentDictionary:
  def __init__(self, sent_file):
    afinnfile = open(sent_file)
    self.scores = {}
    self.new_terms = {}

    for line in afinnfile:
      term, score = line.split("\t")
      self.scores[term] = int(score)

  def new_terms(self):
    self.new_terms

  def score(self, tweet):
    total = 0
    punct_table = dict((ord(char), None) for char in string.punctuation)
    terms = tweet.translate(punct_table).replace("\n", "").split(" ")
    tweet_new_terms = []

    for term in terms:
      lterm = term.lower()

      if lterm in self.scores:
        total += self.scores[lterm]
      else:
        tweet_new_terms.append(lterm)

    for term in tweet_new_terms:
      lterm = term.lower()

      if lterm not in self.new_terms.keys():
        self.new_terms[lterm] = [total]
      else:
        self.new_terms[lterm].append(total)
  
    return total

def main():
  sent_file = sys.argv[1]
  tweets_file = sys.argv[2]
  tweets = [line.rstrip("\n") for line in open(tweets_file)]
  dictionary = SentimentDictionary(sent_file)

  for tweet in tweets:
    tweet_data =  json.loads(tweet)

    if 'text' in tweet_data:
      dictionary.score(tweet_data['text'])

  for key, value in dictionary.new_terms.items():
    try:
      "{key}".format(**locals())
      term_total = sum(value) / float(len(value))
      print("{key} {term_total}".format(**locals()))
    except UnicodeEncodeError as u:
      next


if __name__ == '__main__':
    main()
