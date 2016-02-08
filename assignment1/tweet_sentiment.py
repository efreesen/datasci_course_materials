import json
import string
import sys

class SentimentDictionary:
  def __init__(self, sent_file):
    afinnfile = open(sent_file)
    self.scores = {}

    for line in afinnfile:
      term, score = line.split("\t")
      self.scores[term] = int(score)

  def score(self, tweet):
    total = 0
    punct_table = dict((ord(char), None) for char in string.punctuation)
    terms = tweet.translate(punct_table).replace("\n", "").split(" ")

    for term in terms:
      if term in self.scores:
        total += self.scores[term]
  
    return total

def main():
  sent_file = sys.argv[1]
  tweets_file = sys.argv[2]
  tweets = [line.rstrip("\n") for line in open(tweets_file)]

  for tweet in tweets:
    tweet_data =  json.loads(tweet)

    if 'text' in tweet_data:
      print str(SentimentDictionary(sent_file).score(tweet_data['text']))
    else:
      print '0'

if __name__ == '__main__':
  main()
