import json
import operator
import sys

class HashtagsCounter:
  def __init__(self):
    self.hashtags_count = {}

  def count_hashtags(self, hashtags):
    try:
      for hash_list in hashtags:
        text = hash_list['text']

        if text in self.hashtags_count:
          self.hashtags_count[text] += 1
        else:
          self.hashtags_count[text] = 1
    except UnicodeEncodeError as u:
      return None

  def top_ten(self):
    sorted_count = sorted(self.hashtags_count.items(), key=operator.itemgetter(1), reverse=True)

    for hashtag in sorted_count[:10]:
      print "{hashtag[0]} {hashtag[1]}".format(**locals())

def main():
  tweets_file = sys.argv[1]
  tweets = [line.rstrip("\n") for line in open(tweets_file)]
  counter = HashtagsCounter()

  for tweet in tweets:
    tweet_data =  json.loads(tweet)

    if 'entities' in tweet_data:
      str(counter.count_hashtags(tweet_data['entities']['hashtags']))

  counter.top_ten()

if __name__ == '__main__':
  main()
