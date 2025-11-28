import requests, time, random
URL = 'http://localhost:5000/api/alerts'
labels = ['chainsaw','truck','fire','bird','background']
def gen_alert():
    label = random.choice(labels)
    return {'device_id':f'sim-{random.randint(1,5)}','label':label,'confidence':round(random.uniform(0.6,0.99),2),'timestamp':int(time.time()),'gps':{'lat':20.0+random.uniform(-0.5,0.5),'lon':78.0+random.uniform(-0.5,0.5)}}
if __name__=='__main__':
    for _ in range(10):
        p = gen_alert()
        print('POST', p)
        try:
            r = requests.post(URL, json=p, timeout=5)
            print('->', r.status_code, r.text)
        except Exception as e:
            print('error', e)
        time.sleep(2)
