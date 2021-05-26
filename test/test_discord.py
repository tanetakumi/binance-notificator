# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests
import test_import


test_import.ppprint()
'''
# dotenv_path = join(dirname(__file__), '.env')
load_dotenv()

wh = os.getenv("WEBHOOK")

print(wh)
 
main_content = {
  "username": "webhookテストさん",
  "avatar_url": "https://www.google.co.jp/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png",
  "content": "コンテンツの中身:grinning: :grimacing: "
}
 
requests.post(wh, main_content)
'''