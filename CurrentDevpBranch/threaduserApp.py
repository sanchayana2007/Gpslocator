#!/usr/bin/python

import threading
import time
import user_app_simver
exitFlag = 0
user_app_simver.setlogger()
class myThread (threading.Thread):
   def __init__(self, mobno, vid, counter):
      threading.Thread.__init__(self)
      self.mobno = mobno
      self.vid = vid
      self.counter = counter
   def run(self):
      print( "Starting " + str(self.counter))
      user_app_simver.Userapp_Create(self.mobno,self.vid)
      print( "Exiting " + str(self.counter))



