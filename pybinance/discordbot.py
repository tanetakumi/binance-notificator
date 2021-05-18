import discord
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor
import asyncio


class Bot(discord.Client):
    def __init__(self,brands_list):
        super().__init__()
        self.brands = brands_list

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


    
if __name__ == "__main__":
    manager = Manager()
    # bot = Bot(manager.list())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(Bot(manager.list()).run("ODE1NTY4NDkxMDE2MzU1ODQw.YDuTWA.8r4a_aJ6c9F6oxNhHLkUn0DEa8A"))
    Bot(manager.list()).start("ODE1NTY4NDkxMDE2MzU1ODQw.YDuTWA.8r4a_aJ6c9F6oxNhHLkUn0DEa8A")
    print("Hello")
"""
    process_pool = [] # プロセス生成したい関数を登録
    process_pool.append(Bot(manager.list()).run("ODE1NTY4NDkxMDE2MzU1ODQw.YDuTWA.8r4a_aJ6c9F6oxNhHLkUn0DEa8A")) # 引数に上記で作成した変数を与える

    with ProcessPoolExecutor(max_workers=2) as executor: # max_workerは同時に動かすプロセスの最大数 Noneを指定するとコア数 * 4の値になる
        for process in process_pool:
            executor.submit(process) # submit関数で、list内の関数をプロセス生成
"""

    # bot.run("ODE1NTY4NDkxMDE2MzU1ODQw.YDuTWA.8r4a_aJ6c9F6oxNhHLkUn0DEa8A")
    


