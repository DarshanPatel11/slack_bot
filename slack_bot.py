# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:42:16 2019
@author: Darshan
"""
import os
import time
from slackclient import SlackClient
import datetime
# instantiate Slack client
slack_client = SlackClient(os.environ['TOKEN'])
# starterbot's user ID in Slack: value is assigned after the bot starts up


def send_morning_msg(): 
    slack_client.api_call("chat.postMessage",channel="#general",text="What are you planning to accomplish today?")
    print("Morning Msg Sent...")
    time.sleep(100)


def send_evening_msg(): 
    slack_client.api_call("chat.postMessage",channel="#general",text="So, What did you achieved today?")
    print("Evening Msg Sent...")
    time.sleep(100)



print('started...')
#dt = datetime.datetime.now()
from pytz import timezone
#print(dt)        
while True:
    now_utc = datetime.datetime.now(timezone('UTC'))    
    dt = now_utc.astimezone(timezone('Asia/Kolkata'))
    #dt = datetime.datetime.now()
    if dt.hour == 18 and dt.minute == 25:
        send_evening_msg()
    elif dt.hour == 10 and dt.minute == 15:
        send_morning_msg()
