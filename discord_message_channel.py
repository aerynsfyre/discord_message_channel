#!/usr/bin/env python3
import requests

channel_url = "https://discord.com/api/v9/channels/<YOUR-CHANNEL-ID-HERE>/messages"
bot_token = "<BOT-ACCOUNT-AUTHORISATION-TOKEN-HERE>"
user_id = "<YOUR-USER-ID-HERE>"

def send_msg(message):
	payload = {
		"content":str(f"<@{user_id}> Program Notification: {message}")
	}
	headers = {
		"authorization":bot_token
	}
	res = requests.post(my_channel,payload,headers=headers)
	
