import os
import json
import tweepy

# env
CK = os.environ['CONSUMER_KEY']
CS = os.environ['CONSUMER_KEY_SECLET']
AT = os.environ['ACCESS_TOKEN']
AS = os.environ['ACCESS_TOKEN_SECLET']
LIST_ID = os.environ['LIST_ID']
OWNER_SCREEN_NAME = os.environ['OWNER_SCREEN_NAME']

# api
auth = tweepy.OAuthHandler(CK, CS)
auth.set_access_token(AT, AS)
api = tweepy.API(auth)


def lambda_handler(event, context):
    query = create_query('Apple Watch')
    res = api.search(q=query)
    print(res)
    return {
        "body": "???"
    }


def create_query(query: str):
    return query + ' list:' + LIST_ID
