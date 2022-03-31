import sys
from pyrogram import Client
from pyrogram.errors import FloodWait
import time
import pickle


app = Client('session', workdir='./session')
chat = 'mossdelka'  # Назва чату чи його ID
app.start()

"""chunk = app.get_chat_members(chat)"""

nn = 0





original_stdout = sys.stdout


l00 =[]
l000 = []


"""with open(chat + '.txt', 'w', encoding='utf-8') as f:
    sys.stdout = f # Change the standard output to the file we created."""


for member in app.iter_chat_members(chat, filter="restricted"):
    try:
        nn += 1
        l00.append(nn)
        l00.append(member.user.phone_number)
        l00.append(member.user.username)
        l00.append(member.user.first_name)
        l00.append(member.user.last_name)
        l000.append(l00)
        l00 = []
    except FloodWait as e:
        time.sleep(e.x)
        continue


with open(chat + ".pickle" , 'wb') as f1:
    pickle.dump(l000, f1)



app.stop()
