import json
import re
import string
import sys

states = {
  'AK': 'Alaska',
  'AL': 'Alabama',
  'AR': 'Arkansas',
  'AS': 'American Samoa',
  'AZ': 'Arizona',
  'CA': 'California',
  'CO': 'Colorado',
  'CT': 'Connecticut',
  'DC': 'District of Columbia',
  'DE': 'Delaware',
  'FL': 'Florida',
  'GA': 'Georgia',
  'GU': 'Guam',
  'HI': 'Hawaii',
  'IA': 'Iowa',
  'ID': 'Idaho',
  'IL': 'Illinois',
  'IN': 'Indiana',
  'KS': 'Kansas',
  'KY': 'Kentucky',
  'LA': 'Louisiana',
  'MA': 'Massachusetts',
  'MD': 'Maryland',
  'ME': 'Maine',
  'MI': 'Michigan',
  'MN': 'Minnesota',
  'MO': 'Missouri',
  'MP': 'Northern Mariana Islands',
  'MS': 'Mississippi',
  'MT': 'Montana',
  'NA': 'National',
  'NC': 'North Carolina',
  'ND': 'North Dakota',
  'NE': 'Nebraska',
  'NH': 'New Hampshire',
  'NJ': 'New Jersey',
  'NM': 'New Mexico',
  'NV': 'Nevada',
  'NY': 'New York',
  'OH': 'Ohio',
  'OK': 'Oklahoma',
  'OR': 'Oregon',
  'PA': 'Pennsylvania',
  'PR': 'Puerto Rico',
  'RI': 'Rhode Island',
  'SC': 'South Carolina',
  'SD': 'South Dakota',
  'TN': 'Tennessee',
  'TX': 'Texas',
  'UT': 'Utah',
  'VA': 'Virginia',
  'VI': 'Virgin Islands',
  'VT': 'Vermont',
  'WA': 'Washington',
  'WI': 'Wisconsin',
  'WV': 'West Virginia',
  'WY': 'Wyoming'
}

class SentimentDictionary:
  def __init__(self, sent_file):
    afinnfile = open(sent_file)
    self.scores = {}
    self.state_scores = {}

    for line in afinnfile:
      term, score = line.split("\t")
      self.scores[term] = int(score)

  def get_state(self, location):
    try:
      splitted = re.split(", |: ", str(location))
      state = None

      if len(splitted) == 2:
        last = splitted[1]

        if last == 'USA':
          state = splitted[0]
        else:
          state = last
      else:
        state = splitted[0]

      if len(state) == 2:
        try:
          states[state]
        except KeyError as k:
          state = None
      else:
        if state in states.values():
          index = states.values().index(state)

          state = states.keys()[index]
        else:
          state = None
      
      if state is not None:
        return str(state)
      
      return None
    except UnicodeEncodeError as u:
      return None

  def score(self, tweet):
    total = 0
    punct_table = dict((ord(char), None) for char in string.punctuation)
    terms = tweet['text'].translate(punct_table).replace("\n", "").split(" ")

    state = self.get_state(tweet['user']['location'])

    for term in terms:
      if term in self.scores:
        total += self.scores[term]
  
    if state is not None:
      if state in self.state_scores: 
        self.state_scores[state].append(total)
      else:
        self.state_scores[state] = [total]

    return total

  def happiest_state(self):
    scores = {}

    for key, value in self.state_scores.items():
      scores[key] = sum(value)/float(len(value))

    values = scores.values()

    max_value = max(values)
    max_index = values.index(max_value)

    print scores.keys()[max_index]

def main():
  sent_file = sys.argv[1]
  tweets_file = sys.argv[2]
  tweets = [line.rstrip("\n") for line in open(tweets_file)]
  dictionary = SentimentDictionary(sent_file)

  for tweet in tweets:
    tweet_data =  json.loads(tweet)

    if 'text' in tweet_data:
      str(dictionary.score(tweet_data))

  dictionary.happiest_state()

if __name__ == '__main__':
  main()
