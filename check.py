import requests

url = 'https://devrant.com/api/devrant/rants'
app = 3
sort = 'algo'
limit = 3
token_id = '2384447'
token_key = '8wYpFFxWDuEWiTKd54Wve1CqyrmSvE4BsmHHum_L'
user_id = '115067'

params = {'app': app, 'sort': sort, 'limit': limit, 'token_id': token_id, 'token_key':token_key, 'user_id':user_id}
res = requests.get(url, params)
res_j = res.json()
for rant in res_j['rants']:
    print(rant['text'])
    print(20*'*')
