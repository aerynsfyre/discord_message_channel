This file sends a message with an @ mention of a user to a discord channel, and is called from within a python program. 
It requires the following:
- A discord account for the person who is being notified.
- A discord account which will be the bot who messages the updates.
- A text channel on your own discord server for the messages to be posted to.

Download the code as a compressed folder, extract the files, and then make the following changes to the discord_message_channel.py file. Once these are made, run the following command in the directory of the files to install the code.

              python3 setup.py install

Initial Setup Steps:
1. To identify your user ID, follow these instructions: 
https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID#h_01HRSTXPS5H5D7JBY2QKKPVKNA

2. To find the bot authorisation token, make sure you are logged into your bot's discord account, and then follow this set of instructions: 
https://www.androidauthority.com/get-discord-token-3149920/

3. Find your channel ID: 
https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID#h_01HRSTXPS5FMK2A5SMVSX4JW4E

Once you have those three pieces, you can edit the code to add these notes.

MUST:
1. Bot token should be changed to the token string identified above.
2. Edit the URL string in the code to enter your channel ID.
3. User ID is the ID of the account which will be mentioned as @ in the message - your account.

       channel_url = "https://discord.com/api/v9/channels/<YOUR-CHANNEL-ID-HERE>/messages"
       bot_token = "<BOT-ACCOUNT-AUTHORISATION-TOKEN-HERE>"
       user_id = "<YOUR-USER-ID-HERE>"

Once these changes are made to the file, you can install the python package, and you can import it to your project with the standard import call:

    import discord_message_channel
If you want to simplify the function call, you can instead use: 

    from discord_message_channel import send_msg
The call to send a message is then: 

    send_msg(MESSAGE_STRING)
This should send a message to your channel with a mention of your ID. 

The purpose of this code is to allow you to set up notifications as your code runs or encounters errors. For example:

    try:
      something
    except Exception as e:
      send_msg(e)

Once the import has been called in your project file, you can organise a message to be sent at any point you like.

An example of a recommended function for calling the program is shown below. It ensures the message is formatted with the program name.

  	def update(message):
	  send_msg(f"{os.path.basename(__file__)} successfully completed task {message}")
