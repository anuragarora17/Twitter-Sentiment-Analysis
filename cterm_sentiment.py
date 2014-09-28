import sys
import json

known_sentiments = {}
derived_sentiments = {}

def build_sentiment_dict(sent_file):
  for line in sent_file.readlines():
    sentiment, score = line.split("\t")
    known_sentiments[sentiment] = int(score)

def calc_tweet_sentiment(tweet):
  if "text" not in tweet: return 0.0
  score = 0.0
  tweet_text = tweet["text"].encode('utf-8', 'ignore')
  for sentiment in known_sentiments.keys():
    if sentiment in tweet_text: score = score + known_sentiments[sentiment]
  return score

def main():
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  build_sentiment_dict(sent_file)
  known_words = known_sentiments.keys()
  datalines = tweet_file.readlines()
  tweets = map(lambda tweet: json.loads(tweet.encode('utf-8', 'ignore')), datalines)

  #print "Total number of tweets : ", len(tweets)
  #print "Sample tweet : ", tweets[113]["text"]
  #print "Score : ", calc_tweet_sentiment(tweets[113])
  #print "Known words : ", len(known_words)
  #print "New words : ", len(derived_sentiments)
  #print "Starting analysis..."

  for tweet in tweets:
    if "text" in tweet:
      tweet_score = calc_tweet_sentiment(tweet)
      tweet_words = tweet["text"].encode('utf-8', 'ignore').split()
      new_words = filter(lambda word: word not in known_words, tweet_words)
      for word in new_words:
        derived_sentiments[word] = derived_sentiments.get(word, 0.0) + tweet_score

  #print "New words learnt :", len(derived_sentiments)
  for sentiment, score in derived_sentiments.items():
    print sentiment, score

if __name__ == '__main__':
  main()
