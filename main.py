from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from time import *

app = Client("my_account")

stop = 1

@app.on_message(filters.text & filters.private)
def echo(client, message):
    text = message.text
    return_text = ""

    i = 0 
    k = 1
    progress = 0
    if text[0] == ".":
        while progress <= 100:
            message.edit("Текст печатается: " + str(progress) + "%")
            progress += 10
            sleep(0.01)

    
        while i < 1:
            try:
            

                if return_text == "":
                    message.edit(return_text + "#")
            
                return_text += text[k]

                message.edit(return_text + "#")

                if text[k] == ".":
                    i = 1
            
                k += 1

                sleep(0.03)
            except FloodWait as e:
                sleep(0.01)

        message.edit(text)
    
    if text[0] == "~":
        stop = 0
        while stop == 0:
            message.reply_text(text)

    if text == "stop":
        stop = 1
        
        

app.run()  # Automatically start() and idle()