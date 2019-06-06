# -*- coding: utf-8 -*-
"""
Created on Sat May 25 22:42:16 2019

@author: Darshan
"""
import os
import time
from slackclient import SlackClient
import schedule
# instantiate Slack client
slack_client = SlackClient(os.environ['TOKEN'])
# starterbot's user ID in Slack: value is assigned after the bot starts up


def send_morning_msg(): 
    slack_client.api_call("chat.postMessage",
   channel="#test",
   text="What are you planning to accomplish today?")


def send_evening_msg(): 
    slack_client.api_call("chat.postMessage",
   channel="#test",
   text="So, What did you achieved today?")


# Task scheduling 
# After every 10mins geeks() is called.  
#schedule.every(1).minutes.do(send_msg) 
schedule.every().monday.at("10:15").do(send_morning_msg)
schedule.every().monday.at("18:25").do(send_morning_msg)    

schedule.every().tuesday.at("10:15").do(send_morning_msg)
schedule.every().tuesday.at("18:25").do(send_morning_msg)

schedule.every().wednesday.at("10:15").do(send_morning_msg)
schedule.every().wednesday.at("18:25").do(send_morning_msg)

schedule.every().thursday.at("10:15").do(send_morning_msg)
schedule.every().thursday.at("18:25").do(send_morning_msg)

schedule.every().friday.at("10:15").do(send_morning_msg)
schedule.every().friday.at("18:25").do(send_morning_msg)

print("Started...")
while True:
    # Checks whether a scheduled task  
    # is pending to run or not 
    schedule.run_pending() 
    time.sleep(1) 
    