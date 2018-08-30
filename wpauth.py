# coding=utf-8

import json

import logging
import re
import requests

def creattoken(name,pwd):
    creaturl = "https://healthnice.org/wp-json/jwt-auth/v1/token"

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+name+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+pwd+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    creatheaders = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'cache-control': "no-cache",
    'postman-token': "bafa8bff-a1dc-8f77-4a68-746be2b54644"
    }

    response = requests.request("POST", creaturl, data=payload, headers=creatheaders)

    res = json.loads(response.text)

    print('token:%s' % res['token'])
    return res['token']

def authtoken(token):
    validurl = "https://healthnice.org/wp-json/jwt-auth/v1/token/validate"

    validheaders = {
    'authorization': "Bearer "+token,
    'cache-control': "no-cache",
    # 'postman-token': "b3268ccc-4460-afb2-29d5-28f079bfc3ec"
    }

    response = requests.request("POST", validurl, headers=validheaders)

    valid = json.loads(response.text)

    if valid['data']['status'] == 200:
        print('驗證正確')
    else:
        print('驗證失敗')

if __name__ == "__main__":

    name = 'paui'
    pwd = 'paui'

    # creaturl = "https://healthnice.org/wp-json/jwt-auth/v1/token"

    # payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"username\"\r\n\r\n"+name+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"password\"\r\n\r\n"+pwd+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    # creatheaders = {
    # 'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    # 'cache-control': "no-cache",
    # 'postman-token': "bafa8bff-a1dc-8f77-4a68-746be2b54644"
    # }

    # response = requests.request("POST", creaturl, data=payload, headers=creatheaders)

    # # print(response.text)

    # res = json.loads(response.text)

    # print('token:%s' % res['token'])
    # # ("這篇文章重複了,文章url:%s" % aurl)

    token = creattoken(name,pwd)

    # validurl = "https://healthnice.org/wp-json/jwt-auth/v1/token/validate"

    # validheaders = {
    # 'authorization': "Bearer "+res['token'],
    # 'cache-control': "no-cache",
    # # 'postman-token': "b3268ccc-4460-afb2-29d5-28f079bfc3ec"
    # }

    # response = requests.request("POST", validurl, headers=validheaders)

    # valid = json.loads(response.text)

    # # print(valid['data']['status'])
    # # exit()
    # if valid['data']['status'] == 200:
    #     print('驗證正確')
    # else:
    #     print('驗證失敗')
    authtoken(token)
