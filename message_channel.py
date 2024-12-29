#!/usr/bin/env python3
import requests

channel_url = "https://discord.com/api/v9/channels/1271346196069486676/messages"
my_channel = "https://discord.com/api/v9/channels/1271397067490852978/messages"
juliet_channel = "https://discord.com/api/v9/channels/1271397067490852978/messages"
bot_token = "MTI3MTM0NDMxOTYwNDg1MDcxMQ.GVQq70.psKOL-8vtz_TRGlIfZy6ylldbcrDDB7gicihhg"
user_id = "726601126161547384"
juliet_id = "1271368126482616342"

def send_msg(message):
	payload = {
		"content":str(f"<@{user_id}> Program Notification: {message}")
	}
	headers = {
		"authorization":bot_token
	}
	res = requests.post(my_channel,payload,headers=headers)
	