import sys
import json

scores={}
results = []
sentence = []
derived_scores = {}

def sentiment_score(fp):
	for line in fp:
		term,score = line.split("\t")
		scores[term] = int(score)

def cal_tweet_sentiment(tweet_file):
        for line in tweet_file:
                information = json.loads(line)
                results.append(information)
        for dictionary in results:
                for key in dictionary:
                        if(key == 'text'):
                                sentence.append(dictionary[key].encode('utf-8','ignore').split())
                                
        for lists in sentence:
                summ = 0
                known_words = scores.keys()
                for tweet_word in lists:
                    if(scores.has_key(tweet_word)):
                          summ += int(scores[tweet_word])
                new_words = filter(lambda word: word not in known_words, lists)
                for word in new_words:
                    derived_scores[word] = derived_scores.get(word,0) + summ

                                        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_score(sent_file)
    cal_tweet_sentiment(tweet_file)
    for sentiment, score in derived_scores.items():
            print sentiment, score

if __name__ == '__main__':
    main()
