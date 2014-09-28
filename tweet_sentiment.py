import sys
import json

scores={}
results = []
sentence = []

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
                                sentence.append(dictionary[key].split(" "))
                                
        for lists in sentence:
                summ = 0
                for word in lists:
                    if(scores.has_key(word)):
                          summ += int(scores[word])
                print summ
                                        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_score(sent_file)
    calc_tweet_sentiment(tweet_file)

if __name__ == '__main__':
    main()
