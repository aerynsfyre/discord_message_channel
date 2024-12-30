#!/usr/bin/env python3
# Change channel, token, and user id. This can be done via python discord_message_channel set_auth <token> <channel_id> <user_id>
# Token requires the creation of another Discord account to send your messages.
# Channel should be a text channel on your server.
# User is the ID of the account which will be mentioned as @ in the message.

import requests
import pickle

global auth
auth = {
"token": "<your-token>",
"channel":"https://discord.com/api/v9/channels/<your-channel-url>/messages",
"user": "<your-user-id>",
}

def get_auth():
	global auth
	with open("auth.pickle","rb") as auth_info:
		auth = pickle.load(auth_info)
	return auth

def write_auth():
	global auth
	with open("auth.pickle","wb") as a:
		pickle.dump(auth)
		
def set_auth(values):
	global auth
	auth["token"] = values[0]
	auth["channel"] = values[1]
	auth["user"] = values[2]
	write_auth()

def send_msg(message):
	global auth
	auth = get_auth()
	payload = {
		"content":str(f"<@{auth['user']}> Program Notification: {message}")
	}
	headers = {
		"authorization":auth["token"]
	}
	res = requests.post(auth["channel"],payload,headers=headers)
	
def update_token(token):
	global auth
	auth = get_auth()
	auth["token"] = token
	write_auth()
	
def update_channel(channel_new):
	global auth
	auth = auth = get_auth()
	auth["channel"] = channel_new
	write_auth()
	
def update_user(user_new):
	global auth
	auth = get_auth()
	auth["user"] = user_new
	write_auth()
	
def get_channel():
	global auth
	auth = get_auth()
	return auth["channel"]

def get_token():
	global auth
	auth = get_auth()
	return auth["token"]

def get_user():
	global auth
	auth = get_auth()
	return auth["user"]
