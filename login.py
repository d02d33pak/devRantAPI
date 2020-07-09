import requests


requestURL = 'https://devrant.com/api/users/auth-token'
username = str(input('enter username : '))
username = 'd02d33pak'
password = str(input('enter password  : '))
password = 'qwerty529'
header = {"content-type": "application/json"}
payload = {'app': 3, 'username': username, 'password': password}

response = requests.post(requestURL, payload, header)
res_json = response.json()

if (res_json['success'] == True):
    feedURL = 'https://devrant.com/api/devrant/rants'
    sort = 'algo'
    limit = 10
    token_id = res_json['auth_token']['id']
    token_key = res_json['auth_token']['key']
    user_id = res_json['auth_token']['user_id']

    payload = {'app': 3, 'sort': sort, 'limit': limit, 'token_id': token_id, 'token_key': token_key, 'user_id': user_id}
    
    rants = requests.get(feedURL, payload)
    rants_json = rants.json()
    for rant in rants_json['rants']:
        if rant['attached_image'] == '':
            print(rant['text'])
            print(20*'-')

