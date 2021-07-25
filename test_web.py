import requests
import json
import asyncio
from aiohttp import ClientSession
import webbrowser


send_data={
    "API_key" : 'test'
}

#r_post=requests.post(url='http://localhost:8080/home/', data=send_data)
#print(r_post.status_code)
#res=r_post.json()
#print(res['session'])
#session=requests.Session()
#sess=session.get('http://localhost:8080/home/')
#print('session: {}'.format(sess.text))
'''with ClientSession() as session:
    async def Hello_world():
        websocket=await session.ws_connect('http://localhost:8080/home/')
        websocket.send_str("Hello_world")
        print("Received: ", (await websocket.receive()).data)
        await websocket.close()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(Hello_world())'''

session = requests.session()
session.trust_env = True
token = session.get('http://localhost:8080/home_site/')
#token.json()
print("SESSION:"+ str(token.json))

requests.post('http://localhost:8080/home_site/',
            data={
                'username': 'nejc',
                'password': 'TEST1234',
                'csrfmiddlewaretoken': token})
'''webbrowser.open('http://localhost:8080/start_listening')'''

#token = session.get('http://localhost:8080/home/')
#data = json.dumps({'test': 'value'})
#print(str(data))
#session.post('http://localhost:8080/home/',
#        data={
 #           'test' : 'TEST'})
            #'csrfmiddlewaretoken': token,
            #'data': data})
#session_get = session.get('http://localhost:8080/home/')
#print(str(session_get.))
#session_get.
# '''