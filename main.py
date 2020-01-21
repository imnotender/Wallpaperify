import requests
import json
import ctypes
import tempfile
import os
import time
import base64

from dotenv import load_dotenv
load_dotenv()


REFRESH_TOKEN = os.getenv("REFRESH_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
EXPIRATION_TIME = float(os.getenv("EXPIRATION_TIME"))
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
authorization_str = CLIENT_ID + ":" + CLIENT_SECRET
authorization_str = base64.b64encode(authorization_str.encode("utf-8"))

#print("EXPIRATION_TIME={}".format(EXPIRATION_TIME))
#print("REFRESH_TOKEN= {} \n ACCESS_TOKEN=
def get_token():
    global EXPIRATION_TIME
    global REFRESH_TOKEN
    global ACCESS_TOKEN
    global CLIENT_ID
    global CLIENT_SECRET
    global authorization_str
    if (time.time() > EXPIRATION_TIME):
       
        headers = {
            'Authorization': 'Basic OGIyOGEzYmFkMWZkNDM0Mjk3OTMwYzAyOGI1YTdjYjY6NWEwM2QyZGNhM2NkNDBmNjk0YWM4N2M1ZWQxYmZhMmM='.format(authorization_str),
        }

        data = {
          'grant_type': 'refresh_token',
          'refresh_token': '{}'.format(REFRESH_TOKEN)
        }

        r = requests.post('https://accounts.spotify.com/api/token', headers=headers, data=data)
        print("REFRESH TOKEN REQUEST RESPONSE: {}".format(r.text))
        return(r.text)
    else:
        print("Access token hasn't expired: returning stored one")
        return ACCESS_TOKEN
    
    
def get_current_album():
    global ACCESS_TOKEN
    global album_id
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
    }   
    
    ra = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
    if not (ra.status_code == "200"):
        if (ra.status_code == "429"):
            print("RATE LIMITED")
        print("STATUS CODE FROM GET ALBUM FUNCTION: {}".format(ra.status_code))

    jsondata = json.loads(ra.text)

    album_link = jsondata["item"]['album']['images'][0]["url"]
    album_id = jsondata["item"]['album']['id']
    print("Album id: " + album_id)

    return(album_link, album_id)

def set_album(album_link, album_id):
    fldr = tempfile.gettempdir() + "\\wallpaperify\\"
    file = fldr + album_id + ".png"
    
    if not os.path.isdir(fldr):
        os.mkdir(fldr)
    if os.path.exists(file):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file , 0)    
    else:
        rf = requests.get(album_link)
        with open(file, 'wb') as f:
            f.write(rf.content)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, file , 0)

def main():
    get_token()
    album_link, album_id = get_current_album()
    set_album(album_link, album_id)
    
while True:   
    main()
    time.sleep(60)
    



    


