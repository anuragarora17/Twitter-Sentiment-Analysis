import sys
import json

sentiments = {}
tweets = []

def print_stats():
  print "Number of sentiments : " + str(len(sentiments.keys()))
  print "Sample of sentiments"
  sample_keys = sentiments.keys()[0:5]
  for key in sample_keys : print key + " => " + str(sentiments[key])
  print "The value for \"not working\" " + str(sentiments["not working"])
  print "-------------------------------"
  print "Number of tweets : " + str(len(tweets))
  print "Sample of tweets"
  for index in range(0,5):
    print tweets[index]

def build_sentiment_dict(sent_file):
  for line in sent_file.readlines():
    sentiment, score = line.split("\t")
    sentiments[sentiment] = int(score)

def build_tweet_list(tweet_file):
  for line in tweet_file.readlines():
    tweet = json.loads(line)
    if "text" in tweet.keys():
      tweets.append(tweet["text"])

def main():
  # Get arguments
  sent_file = open(sys.argv[1])
  tweet_file = open(sys.argv[2])
  # Load files to data structs.
  build_sentiment_dict(sent_file)
  build_tweet_list(tweet_file)

  # For debugging.
  #print_stats()

  # Scoring only using words.
  #for tweet in tweets:
    #print tweet.encode('ascii', 'ignore')
    #print float(sum(map(lambda word: sentiments.get(word, 0), tweet.split(' '))))

  # Scoring using sentiments, takes more time, but I think this is more accurate.
  # For example, in cases where phrases are used.
  for tweet in tweets:
    score = 0.0
    for sentiment in sentiments.keys():
      if sentiment in tweet.encode('ascii', 'ignore'):
        score = score + sentiments[sentiment]
    #print tweet.encode('ascii', 'ignore')
    print str(score)

if __name__ == '__main__':
  main()