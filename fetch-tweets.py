import tweepy
import os
import pandas as pd
from dotenv import dotenv_values
from typing import TypedDict


class TwitterConfig(TypedDict):
    API_KEY:str
    API_KEY_SECRET:str
    BEARER_TOKEN:str
    SUBJECT:str

config:TwitterConfig = {
    **dotenv_values(".env"),  # load default env variable
    **dotenv_values(".env.local"),  # load local env variable
    **os.environ,  # override loaded values with environment variables
}
base_twitter_url = "https://api.twitter.com/"
api_example_endpoint = (f"2/tweets/search/recent")


def search_recent_tweets(query:str) -> dict:
    bearer:str = config["BEARER_TOKEN"]
    client = tweepy.Client(bearer_token=bearer)
    tweets = client.search_recent_tweets(query=query,
                                     tweet_fields = ["created_at", "text", "source"],
                                     user_fields = ["name", "username", "location", "verified", "description"],
                                     max_results = 10,
                                     expansions='author_id'
                                     )
    return tweets

def create_dataset_from_tweets(tweets:dict) -> pd.DataFrame:
    tweet_info_ls = []
    for tweet, user in zip(tweets.data, tweets.includes['users']):
        tweet_info = {
            'created_at': tweet.created_at,
            'text': tweet.text,
            'source': tweet.source,
            'name': user.name,
            'username': user.username,
            'location': user.location,
            'verified': user.verified,
            'description': user.description
        }     
        tweet_info_ls.append(tweet_info) 
    # create dataframe from the extracted records
    tweets_df = pd.DataFrame(tweet_info_ls)
    # display the dataframe
    return tweets_df


if __name__ == "__main__":
    # query to search for tweets
    subject = config["SUBJECT"]
    query = f"#{subject} lang:fr"
    print(query)
    tweets = search_recent_tweets(query)
    dataset = create_dataset_from_tweets(tweets)
    print(dataset.head())