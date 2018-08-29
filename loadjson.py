import json
import requests

url = "https://healthnice.org/wp-json/wp/v2/posts/6599"

headers = {
    'cache-control': "no-cache",
    'postman-token': "ef62011a-2836-56fa-919f-2cee4764d65a"
    }

response = requests.request("GET", url, headers=headers)
response.encoding = 'utf-8'
res = json.loads(response.text)##先爬目錄
# return res
# print(res['id'])

print(res)