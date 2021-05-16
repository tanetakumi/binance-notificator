import discord

class Bot(discord.Client):

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')
        # print("スレッド番号:",th.get_ident()) 

    async def on_message(self,message) -> str:
        # 「おはよう」で始まるか調べる
        if message.content.startswith("おはよう"):
            # 送り主がBotだった場合反応したくないので
            if self.user != message.author:
                # print(message.author)
                # print("スレッド番号:",th.get_ident()) 
                # メッセージを書きます
                # m = "おはようございます" + message.author.name + "さん！"
                # メッセージが送られてきたチャンネルへメッセージを送ります
                # await message.channel.send(m)
                return message.content

        # print("スレッド番号:",th.get_ident()) 
      


