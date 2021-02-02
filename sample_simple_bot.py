from pyrogram import Client
import credentials
import config

# install lib pytogram with:
#   pip install -u pyrogram

# create in https://my.telegram.org/apps
api_id = -000   # integer variable. Not string.
api_hash = ''

# Get in t.me/MissRose_bot
# 1. Add her into a group.
# 2. And send the command: /id
chat_id = ''

# create in t.me/BotFather
#  Is the code that they said after the text:
#       "Use this token to access the HTTP API:"
bot_token = ''


def send_file(file_path, file_name_mask, caption):

    with Client("bot", api_id, api_hash,
                bot_token=bot_token) as app:
        app.send_document(chat_id,
                          file_path,
                          file_name=file_name_mask,
                          caption=caption)


# Let's test send a file into a group!

# 1.: Add your bot into a group. 
#  The BotFather will say the link after 'You will find it at'


file_path=''
file_name_mask='' # with extension!
caption=''

send_file(file_path, file_name_mask, caption)