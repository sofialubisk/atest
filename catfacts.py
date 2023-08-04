import requests
def get_data(param):
    url = 'https://catfact.ninja/'
    result = requests.get(url+param)
    data = result.json()
    print(data)
    try:
        if data['code'] == '404':
            return False
    except:
        return True
