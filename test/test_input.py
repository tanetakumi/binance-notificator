import time
from multiprocessing import Process

import discord
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor
import asyncio

from dotenv import load_dotenv

load_dotenv()
# 環境変数を参照
import os
DISCORD_TOKEN = os.getenv('ACCESS_TOKEN')

class Bot(discord.Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self,message):
        # 「おはよう」で始まるか調べる
        if message.content.startswith("おはよう"):
            # 送り主がBotだった場合反応したくないので
            if self.user != message.author:
                print(message.author)
                # print("スレッド番号:",th.get_ident()) 
                # メッセージを書きます
                # m = "おはようございます" + message.author.name + "さん！"
                # メッセージが送られてきたチャンネルへメッセージを送ります
                # await message.channel.send(m)
                # return message.content

class TestClass():
    def test_f(self):
        ctr = 0
        while True:
            ctr += 1
            print("     ", ctr)
            time.sleep(1.0)
 
if __name__ == '__main__':
    ## run function in the background
    CT = Bot()
    
    # loop = asyncio.get_event_loop()
    # loop.run_forever(CT.start(DISCORD_TOKEN))
    # p = Process(target=CT.run(DISCORD_TOKEN))
    # p.start()
 
 
     ## will not exit if function finishes, only when
     ## "q" is entered, but this is just a simple exampleq
    while True:
        time.sleep(5)
        print("Hello")
             ## do something else
"""
stop_char=""
while stop_char.lower() != "q":
stop_char=input("Enter 'q' to quit ")
if stop_char.lower() == "u":
    print("Hello")
        ## do something else

    print("terminate process")
    if p.is_alive():
        p.terminate()
"""