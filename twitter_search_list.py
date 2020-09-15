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
    query_str = 'Apple Watch'
    query = add_from(query_str, LIST_ID)
    res = api.search(q=query)
    print(res)
    return {
        "body": "???"
    }


def create_query(query: str):
    return query + ' list:' + LIST_ID


def add_from(query: str, list_id: str):
    members = get_list_members(list_id)
    query += ' AND ' + ' OR '.join(['from:' + mem for mem in members])
    return query[:500]


def get_list_members(list_id: str):
    members = []
    res_members = api.list_members(list_id=list_id)

    for mem in res_members:
        members.append(mem.screen_name)
    return members
