# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

class Notify:
    def __init__(self) -> None:
        load_dotenv()
        self.webhook = os.getenv("WEBHOOK")
    
    def toDiscord(self,message):
        main_content = {
            "username": "webhookテストさん",
            "avatar_url": "https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
            "content": message+":grinning: :grimacing: "
        }
        requests.post(self.webhook, main_content)

if __name__ == '__main__':
    notify = Notify()
    notify.toDiscord('こんにちわ')