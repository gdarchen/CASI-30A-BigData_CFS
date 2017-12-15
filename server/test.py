from server import Server 
from odm import Odm

def main():
    print("\n")
    s = Server()
    print("---------------- Tweets ----------------")
    s.print_tweets()

    print("\n")

    print("----------------- Dict -----------------")
    s.print_dict()

    print("\n")
    print("------------- Tokenization -------------")
    tokens = {}
    for tweet in s.tweets:
        t,_,_ = s.tokenize_tweet(tweet.text)
        tokens[tweet.text] = t
        print(t)
    print("\n")

    print("------------ Global valence ------------")
    for tweet in s.tweets:
        print("%s : valence=%d"%(tweet.text, s.get_tweet_valence(tweet.text)))
    print("\n")

 
if __name__ == '__main__':
    main()