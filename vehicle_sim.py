import httplib2
from datetime import datetime
import simplejson
import time


URL = 'http://localhost:7778/loc_api/new_location'
imei = "351891081562248"
mob_num = "8085461683"

def random_movement():
    lat= 13.09809
    lng= 77.09809
    while True:
        lat += 0.000050
        lng+= 0.000056
        data = {"longitude": lng, "mobile_number": mob_num,
            "type":"android", "imei":imei, "latitude": lat}
        print(data)
        client = httplib2.Http()
        resp, content = client.request(URL,
                          'POST',
                          simplejson.dumps(data),
                          headers={'content-Type': 'application/json'})
        time.sleep(30)

random_movement()














