import requests

siteler = ['https://www.youtube.com/watch?v=u9EOsPlvn-Q']

for x in siteler:
    r = requests.get(x)
    if r.status_code == 200: 
        print('Url Bulundu : {}'.format(x))
    elif r.status_code == 404: 
        print('Url Hatalı')