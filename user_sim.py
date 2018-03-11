import httplib2
from datetime import datetime
import simplejson
import time


URL = 'http://localhost:7777/api/newuser'
role = "driver"
uname = "hitesh"
fullname = "hitesh katre"
mob_num = "8085461683"
email_id = "hkkatre@gmail.com"
v_id = "jhgfdshddsd"

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhIjp7IjIiOnRydWV9LCJzdWIiOiI1YTU3YWY1NTE2Nzk2NzUwZDU4YTdlNGMiLCJleHAiOjE1MjEyMTI0NTB9.kWs0kh4RR18jG8do2ABdBGizHW48-YwsAdUReVLWfz8'
headers={'content-Type': 'application/json', 'Authorization':'Bearer '+token}

def user_movement():
    #lat= 13.09809
    #lng= 77.09809
    while True:
       # lat += 0.000050
        #lng+= 0.000056
        data = {"role": role, "username": uname,"full_name" : fullname,"mobile_number" : mob_num,
        "email_id" : email_id , "v_id": v_id}
        print(data)
        client = httplib2.Http()
        resp, content = client.request(URL,
                          'POST',
                          simplejson.dumps(data),
                          headers=headers)
        print("Return ", resp)
        time.sleep(30)

user_movement()














