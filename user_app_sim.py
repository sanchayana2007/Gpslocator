#!/usr/bin/python
import websocket
import thread
import time
import json
import requests
import sys

URL = "https://live.trakiga.com/api/"
WS_URL = "wss://live.trakiga.com/api/rt_socket"
mob_num = None
vid = "5a9e0ee3167967658a3f2875"
jwt = None

def get_auth_token():
    global jwt
    r = requests.get(URL+'test_auth_token?mobile_number='+mob_num)
    resp = r.json()
    print "Resp from Server %r" % resp
    if resp["resp_code"]:
    	jwt = resp["token"]
    	print "jwt auth: " + jwt
    	return True
    else:
	
    	print "ERROR Msg: ", resp["data"]
        return False



def on_message(ws, msg):
    msg = str(msg)
    if msg.find('conn_ready') > 0:
        print "Sending SUB request"
        sub(ws)
        return
    print(mob_num + ' got: ' + msg)

def on_error(ws, error):
    print "onError", error

def on_close(ws):
    print "onClosed"

def on_open(ws):
    global jwt
    print ("Conn estd, sending register")
    print jwt
    register_msg = {
            "auth_token": jwt,
            "msg_type" : "register"
        }
    ws.send(json.dumps(register_msg))


def sub(ws):
    sub_msg = {
            "msg_type" : "sub",
            "vid" : vid
          }
    ws.send(json.dumps(sub_msg))

def unsub(ws):
    unsub_msg = {
            "msg_type" : "unsub",
            "vid" : "simple_id"
          }
    ws.send(json.dumps(unsub_msg))

def ws_comm():
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp(WS_URL,on_message = on_message,on_error = on_error,on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    mob_num = sys.argv[1]
    print "User : " + mob_num
    ret = get_auth_token()
    if ret:
        ws_comm()

