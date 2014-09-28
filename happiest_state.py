import sys
import json

scores={}
state_sentiments = {}
results = []
state_codes = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def sentiment_score(fp):
	for line in fp:
		term,score = line.split("\t")
		scores[term] = int(score)

def calc_tweet_sentiment(tweet_file):
        for line in tweet_file:
                information = json.loads(line)
                results.append(information)
        for dictionary in results:
                for key in dictionary:
                        if "place" and "text" in key:
                            if "place" is not None:
                                if(dictionary["place"]["country"] == "United States"):
                                    word = dictionary["text"].split()
                                    tweet_sentiment = sum(map(lambda word: scores.get(word, 0.0), word))
                                    tweet_state = dictionary["place"]["full_name"][-2:]
                                    if tweet_state in state_codes:
                                            state_sentiments[tweet_state] = state_sentiments.get(tweet_state, 0.0) + 1
                                        
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    sentiment_score(sent_file)
    calc_tweet_sentiment(tweet_file)
    happy_state = sorted(state_sentiments.items(), key=lambda x: x[1], reverse=True)[0][0]
    print happy_state

if __name__ == '__main__':
    main()
