import requests, json, pprint

sw_ip = '10.31.70.210'
login = 'restapi'
password = 'j0sg1280-7@'

sw_url = 'https://' + sw_ip + ':55443'

zapros1 = requests.post(sw_url + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = zapros1.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
#zapros2 = requests.get(sw_url + '/api/v1/interfaces/GigabitEthernet1/state', headers=header, verify=False)
#https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/restapi/restapi/RESTAPIipinterface.html
zapros2 = requests.get(sw_url + '/api/v1/interfaces/GigabitEthernet1/statistics', headers=header, verify=False)
pprint.pprint(zapros2.json())