#replicate the User App
#!/usr/bin/python

#Core imports 
import thread
import time
import json
import sys
import logging 
logger=None 

try: 
   import websocket
   import requests
except ImportError:

   print('Install 3rd party Module: websocket-client,requests')
   	
def setlogger():
    # create logger
	
    global logger
    logger = logging.getLogger('USER SIM APP')
    logger.setLevel(logging.DEBUG)
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)





class Userapp:
   
    def __init__(self,mn,vid):
        self. URL = "http://dev.xlayer.in/api/"
        self.WS_URL = "ws://dev.xlayer.in/api/rt_socket"
        self.mob_num = mn
        self.vid = vid
        self.jwt = None
	self.ws = None 
        



    def get_auth_token(self):
        r = requests.get(self.URL+'test_auth_token?mobile_number='+ self.mob_num)
        resp = r.json()
        logger.debug("Response from the Server  %r", resp)
        if resp["resp_code"]:
    	    self.jwt = resp["token"]
    	    logger.debug("jwt auth: "+ self.jwt)
    	    return True
        else:
	    logger.error("No Auth Token received" + jwt)
            return False 
        


    def on_message(self,ws, msg):
        msg = str(msg)
        if msg.find('conn_ready') > 0:
            logger.info( "Sending SUB request")
    	    logger.debug(' got:CONN READY from Server  '+ msg)
            self.sub()
            return True
	else:
	    logger.error("Server is not Conn ready State",msg) 

    def on_error(self,ws, error):
	logger.error("Server ",error) 

    def on_close(self,ws):
        logger.info( "On closed ")

    def on_open(self,ws):
        logger.info("Conn estd, sending register")
        logger.debug(self.jwt)
        register_msg = {"auth_token": self.jwt,"msg_type" : "register"}
        self.ws.send(json.dumps(register_msg))


    def sub(self):
        sub_msg = {"msg_type" : "sub","vid" : self.vid}
        self.ws.send(json.dumps(sub_msg))

    def unsub(self):
        unsub_msg = {"msg_type" : "unsub","vid" : "simple_id"}
        self.ws.send(json.dumps(unsub_msg))

    def ws_comm(self):
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.WS_URL,on_message = self.on_message,on_error =self.on_error,on_close = self.on_close)
	if self.ws:
             self.ws.on_open = self.on_open
             self.ws.run_forever()
	else:
	     logger.critical('Websocket connection is not posible')

if __name__ == "__main__":
    #mob_num = sys.argv[1]
    #vid = sys.argv[2]
    setlogger()




    mob_num = '3563563563'
    vid = '5aa918f535238929e8bbdade3563563563'
    logger.info('user number:%s and vid %s',mob_num,vid)
    user1=Userapp(mob_num,vid)
    ret = user1.get_auth_token()
    if ret:
        user1.ws_comm()
