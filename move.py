import argparse
import time
import json

import pyrogram
from pyrogram.errors import FloodWait

parser = argparse.ArgumentParser()

parser.add_argument("--api-id")
parser.add_argument("--api-hash")
parser.add_argument("--origin-chat")
parser.add_argument("--destination-chat")

options = parser.parse_args()

origin_chat = int(options.origin_chat)
destination_chat = int(options.destination_chat)

tg = pyrogram.Client(
	session_name="bot",
	api_id=options.api_id,
	api_hash=options.api_hash,
	no_updates=True
)

tg.start()

message_id = 0

with open("posted.json", mode="r") as file:
	posted = json.loads(file.read())

while True:
	
	message_id = message_id + 1
	
	if message_id in posted:
		continue
	
	try:
		message = tg.get_messages(origin_chat, message_id)
	except FloodWait as e:
		time.sleep(e.x)
		message = tg.get_messages(origin_chat, message_id)
	
	if message.empty:
		posted += [message.message_id]
		continue
	
	if message.photo:
		photo_id = message.photo.file_id
		if message.caption:
			caption = message.caption.markdown
			try:
				tg.send_photo(chat_id=destination_chat, photo=photo_id, caption=caption, parse_mode="markdown", disable_notification=True)
			except FloodWait as e:
				time.sleep(e.x)
				tg.send_photo(chat_id=destination_chat, photo=photo_id, caption=caption, parse_mode="markdown", disable_notification=True)
	
	if message.text:
		text = message.text.markdown
		try:
			tg.send_message(chat_id=destination_chat, text=text, parse_mode="markdown", disable_notification=True, disable_web_page_preview=True)
		except FloodWait as e:
			time.sleep(e.x)
			tg.send_message(chat_id=destination_chat, text=text, parse_mode="markdown", disable_notification=True, disable_web_page_preview=True)
	
	if message.document:
		document_id = message.document.file_id
		try:
			tg.send_document(chat_id=destination_chat, document=document_id, parse_mode="markdown", disable_notification=True)
		except FloodWait as e:
			time.sleep(e.x)
			tg.send_document(chat_id=destination_chat, document=document_id, parse_mode="markdown", disable_notification=True)
	
	posted += [message.message_id]
	
	with open("posted.json", mode="w") as file:
		file.write(json.dumps(posted))
