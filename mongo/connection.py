#from pymongo import MongoClient

from key import *


# client = MongoClient('mongodb://192.168.120.103:27017/',
#                     username='paul2486',
#                     password='pauli<3breaktime',
#                     authSource='admin',
#                     authMechanism='SCRAM-SHA-1')


db = client['WP']  ## 庫
collect = db['wp'] ## 表



#collect.insert({"website":'華視',"title":"惡男拍打柯基 家屬拍手叫好!","creation_date":"2018-03-31","category":"社會","url": "https://news.cts.com.tw/cts/society/201803/201803301919300.html"}) ## 直接寫入
#collect.update({"title":"惡男拍打柯基 家屬拍手叫好!"},{"$set":{"website":"華視第一台","category":"天理"}})
#collect.remove() ## 

re = collect.find({})

#print(re)

for item in re:
    print(item)