# coding=utf-8
from account.key import *
from mongo.key import *


import json
# import time
# import random
# from datetime import datetime, timedelta
import hashlib
import logging
import re
from random import *
import requests

token = 'EAABgFOnpxJoBAKK6l2bhOlcHesBSadHUQYWEbUeiBA1MIpwFZAMXNRqVZB6xiS5g5HI7WcgqnvCiZCExK7gPykKeW5qQwxhKZBtHoxgwg4AwxgLpav78fZCcmeidRX1pnhrZBWNgbhqrJtCMZAfu2L7q438JgYbDHS7RccvbiDZBleVUXe4rXP6bRwqvybL1q3JNZBYf41b3J12KKCLj2dIlt'
targeturl='raylovelulumi'
# targeturl='DoctorKoWJ'


url = 'https://graph.facebook.com/v3.1/'+targeturl+'?fields=feed%7Battachments%2Cmessage%7D&access_token='+token
# print(url)
# exit()
# response = requests.get(url)

response = requests.request("GET", url)
response.encoding = 'utf-8'

res = json.loads(response.text) 

## curl -i -X GET \
## "https://graph.facebook.com/v3.1/raylovelulumi?fields=feed%7Battachments%2Cmessage%7D&access_token=EAABgFOnpxJoBAKZBT9Pl514CJ75x4OOvrMZBap4HQUlHCNkqcFiqDRpgyyv8OjYtRojt9Xqk66DnCMSWEqwi1wFVOZCfZBDSIiY28DhnCRlDXqB0eWTGPnjpy7UGCrXTYNAmIoZAodml2FPC2nFBqNOijZCZC3tn9BYBpooznKxPZBIN0JmGZAW5poULgyLtXTrsZD"
postcount = len(res['feed']['data'])
# print(postcount)
post = 0
while post < postcount:
    # print(res['feed']['data'][post]['message'])

    # print(res['feed']['data'][post]['attachments']['data'][0])
    # exit()

    if 'title'  in res['feed']['data'][post]['attachments']['data'][0]:
        print(res['feed']['data'][post]['attachments']['data'][0]['title'])##摘要  發文文字
    elif 'description' in res['feed']['data'][post]['attachments']['data'][0]:
        print(res['feed']['data'][post]['attachments']['data'][0]['description'])## 目前看起來只有 發文有文字的狀態下沒有
    else:
        print(res['feed']['data'][post]['message'])
    # exit()
    
    print(res['feed']['data'][post]['attachments']['data'][0]['type'])## 
    print(res['feed']['data'][post]['attachments']['data'][0]['url'])##貼文url
    # exit()
    
    piclist = []
    if 'subattachments' in res['feed']['data'][post]['attachments']['data'][0]:
        
        picturelecount = len(res['feed']['data'][post]['attachments']['data'][0]['subattachments']['data'])
        picture = 0
        
        while picture < picturelecount:
            SRC = res['feed']['data'][post]['attachments']['data'][0]['subattachments']['data'][picture]['media']['image']['src']
            print(SRC)
            HEIGHT = res['feed']['data'][post]['attachments']['data'][0]['subattachments']['data'][picture]['media']['image']['height']
            print(HEIGHT)
            WIDTH = res['feed']['data'][post]['attachments']['data'][0]['subattachments']['data'][picture]['media']['image']['width']
            print(WIDTH)
            piclist.append(SRC)
            picture = picture + 1
            # if picture == (picturelecount - 1):
            #     print(XXX)
            #     exit()

        # print(piclist)
        # exit()
    else:
        print(res['feed']['data'][post]['attachments']['data'][0]['media']['image']['src'])##
        print(res['feed']['data'][post]['attachments']['data'][0]['media']['image']['height'])##
        print(res['feed']['data'][post]['attachments']['data'][0]['media']['image']['width'])##
    ## post 最後加
    
    post = post + 1
    # print(piclist)
    # exit()
# print(res['feed']['data'][''])
# message = html['posts']['data'][0]['message']
# print(message.encode('utf-8'))
