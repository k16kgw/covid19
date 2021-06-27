# from webdriver_manager.chrome import ChromeDriverManager
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
import os
# import time
# import yaml
# import datetime
import slackweb
import argparse
# import textwrap
# from bs4 import BeautifulSoup
# import warnings
import urllib.parse
# from dataclasses import dataclass
import requests

import cv2

def send2app(img: numpy.ndarray, slack_id: str, line_token: str) -> None:
    # slack
    if slack_id is not None:
        slack = slackweb.Slack(url=slack_id)
        slack.notify(img=img)

    # line
    if line_token is not None:
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_token}'}
        data = {'message': f'message: {img}'}
        requests.post(line_notify_api, headers=headers, data=data)
        
        
def main():
  # debug用
  parser = argparse.ArgumentParser()
  parser.add_argument('--slack_id', default=None)
  parser.add_argument('--line_token', default=None)
  args = parser.parse_args()

  slack_id = os.getenv("SLACK_ID") or args.slack_id
  line_token = os.getenv("LINE_TOKEN") or args.line_token

  img = cv2.imread('tokyo/outputs/daily_inyear.png', 0)
  # img = 'test'
  send2app(img, slack_id, line_token)

if __name__ == "__main__":
    main()
