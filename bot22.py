import samino
import json
import websocket
import sys
import pyfiglet
import time
import os
os.system("clear")

c = samino.Client("22D3085F471DF87A00FB4CE43052685FE93239644F93AD2140B23F3C77277FF6CAE5A0C164593CD9A8")

Y = "\033[1;33m"
print(Y+pyfiglet.figlet_format("Online Bot"))
def Animation(text):
	for letter in text + '\n':
	    sys.stdout.write(letter)
	    sys.stdout.flush()
	    time.sleep(15/1000)

Animation(Y+'''
 
Онлайн бот - - - > КОМЬЮНИТИ
           - - - > ЧАТ
/---------------------------------\\

              by tek1
     group: t.me/coin_tilted
     github.com/tek1bot

\---------------------------------/
_____________________________________
''')

print("\n 1- Community Only")
print("\n 2- Community , Chat")
opt = int(input("\n 1 Or 2 : "))

p = input("Password : ")
url = c.get_from_link(input("Url com: "))
ComId = url.comId
ChatId = url.objectId

def Online_Chat(header,comId,chatId):
	websocket.enableTrace(False)
	ws =websocket.WebSocket()
	data = json.dumps({"o":{"actions":["Chatting"],"target":f"ndc://x{comId}/chat-thread/{chatId}","ndcId":int(comId),"params":{"threadType":2,"channelType":5},"id":"168113004"},"t":304})
	ws.connect("wss://ws4.narvii.com", header=header)
	ws.send(data)

for e in open("emails.txt","r").read().splitlines():
	try:
		c.login(e,p)
	except:
			continue
	c.join_community(ComId)
	local = samino.Local(ComId)
	if opt ==2:
		local.join_chat(ChatId)
		Online_Chat(c.headers,ComId,ChatId)
	print(f"Online Status Activated {e}")