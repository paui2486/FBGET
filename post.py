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

def get():
    # url = "https://healthnice.org/wp-json/wp/v2/posts/6626"
    url = "https://healthnice.org/wp-json/wp/v2/posts/6599"

    headers = {
    'cache-control': "no-cache",
    # 'postman-token': "ef62011a-2836-56fa-919f-2cee4764d65a"
    }

    response = requests.request("GET", url, headers=headers)
    response.encoding = 'utf-8'
    res = json.loads(response.text)
    return (res)

def getlist():
    # url = "https://healthnice.org/wp-json/wp/v2/posts/6626"
    # url = "https://healthnice.org/wp-json/wp/v2/posts"
    url = "https://healthnice.org/wp-json/wp/v2/posts?per_page=5" ##回傳五比

    headers = {
    'cache-control': "no-cache",
    # 'postman-token': "ef62011a-2836-56fa-919f-2cee4764d65a"
    }

    response = requests.request("GET", url, headers=headers)
    response.encoding = 'utf-8'
    res = json.loads(response.text)
    return (res)

## 檢查機制 需要另外一個ＤＢ 將內容 encode(hash or other) 儲存 每次拉資料回來 儲存 之前 檢查
def check():
    print('FFF')



##  儲存 將某個內容 hash 
def store(data):

    db = client['WP']  ## 庫
    collect = db['wp'] ## 表

    m = hashlib.md5()
    m.update(str(data[num]["content"]["rendered"]).encode("utf-8"))
    content_hashid = m.hexdigest()


    collect.insert({"title":str(data[num]["title"]["rendered"]),"content":str(data[num]["content"]["rendered"]),"excerpt":str(data[num]["excerpt"]["rendered"]),"categories":categorie,"tags":tags,"status":status,"author":author,"content_hashid":content_hashid})

def save(url,title,content,excerpt,categorie,status,tags,authorization,author):

    params = {"title":title,"content":content,"excerpt":excerpt,"status":status,"categories":categorie,"tags":tags,"author":author}
    
    # print(params)

    payload = json.dumps(params).encode('utf8')
    # print(payload)
    # exit()
    headers = {
    'authorization': authorization,
    'content-type': "application/json",
    'cache-control': "no-cache",
    #'postman-token': "f14a90a1-830c-36cb-3e68-a0b3db2ce4d5"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

def savejsonsignle(data,authorization):

    params = {"title":str(data["title"]["rendered"]),"content":str(data["content"]["rendered"]),"excerpt":str(data["excerpt"]["rendered"]),"categories":categorie,"tags":tags,"status":status,"author":author}
    
    print(params)
    # exit()

    payload = json.dumps(params).encode('utf8')
    # payload = params
    headers = {
    'authorization': authorization,
    'content-type': "application/json",
    'cache-control': "no-cache",
    #'postman-token': "f14a90a1-830c-36cb-3e68-a0b3db2ce4d5"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

def savejsonMultiple(data,num,authorization):

    params = {"title":str(data[num]["title"]["rendered"]),"content":str(data[num]["content"]["rendered"]),"excerpt":str(data[num]["excerpt"]["rendered"]),"categories":categorie,"tags":tags,"status":status,"author":author}
    
    print(params)
    # exit()

    payload = json.dumps(params).encode('utf8')
    # payload = params
    headers = {
    'authorization': authorization,
    'content-type': "application/json",
    'cache-control': "no-cache",
    #'postman-token': "f14a90a1-830c-36cb-3e68-a0b3db2ce4d5"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    return response

if __name__ == "__main__":
    # json = [{"title":Hello World!CC,"content":ContentCC,"excerpt":ExcerptUU,"status":publish,"categories":19195,"tags":21364}]
    # json = json.dumps(json)
    ## title 標題 content 內容 excerpt 摘要 前面這三個必填 status 半必填 （建議 publish 不然預設是 draft 草稿 ） 後面選填  author 作者 （是填ＩＤ）sticky – 文章的置顶状态: true or false. 默认为 false. (boolean) optional
    ##內容預計 會被丟進來
    url = "https://healthnice.org/wp-json/wp/v2/posts"
    title = 'ＫＴＭ 1190 ADV 相關訊息及心得'
    content = '全稱KTM Sportmotorcycle AG' ##長文測試ＯＫ
    excerpt = 'ExcerptGG'
    status = 'publish'
    categorie = '19195'
    tags = '21364'
    author = '55'
    data = getlist()
    # print(len(data))

    for num in range(0,len(data)):
        print(data[num])
        # print('間隔')
        store(data)
        response = savejsonMultiple(data,num,authorization)
        print(response.text)


    # print('level is rises 粉絲團聲勢上升中')
    # title = (data["title"]["rendered"])


    # response = save(url,title,content,excerpt,categorie,status,tags,authorization,author)
    # response = savejson(data,authorization)
    # print(response.text)