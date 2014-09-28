import sys
import json

results = []
hashtags = {}

def cal_tweet_frequency(tweet_file):
        for line in tweet_file:
                information = json.loads(line)
                results.append(information)
        for dictionary in results:
                for key in dictionary:
                        if(key == 'entities'):
                               for ht in dictionary["entities"]["hashtags"]:
                                       hashtag = ht["text"]
                                       hashtags[hashtag] = hashtags.get(hashtag, 0.0) + 1.0
                               
def main():
    tweet_file = open(sys.argv[1])
    cal_tweet_frequency(tweet_file)
    top_ten_tags = sorted(hashtags.iteritems(), key=lambda x: x[1], reverse=True)[:10]
    for tag, count in top_ten_tags:
            print tag.encode('utf-8', 'ignore'), count

if __name__ == '__main__':
    main()
