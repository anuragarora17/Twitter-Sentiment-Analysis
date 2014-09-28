import sys
import json

word_frequency={}
results = []
sentence = []

def cal_tweet_frequency(tweet_file):
        for line in tweet_file:
                information = json.loads(line)
                results.append(information)
        for dictionary in results:
                for key in dictionary:
                        if(key == 'text'):
                                sentence.append(dictionary[key].encode('utf-8','ignore').split())
                                
        for lists in sentence:
                for tweet_word in lists:
                        word_frequency[tweet_word] = word_frequency.get(tweet_word, 0.0) + 1.0
                        
def main():
    tweet_file = open(sys.argv[1])
    cal_tweet_frequency(tweet_file)
    total_words = sum(word_frequency.values())
    for word, count in word_frequency.items():
            frequency = count / total_words 
            print word, frequency

if __name__ == '__main__':
    main()
