import requests
import time
import json
import pandas as pd
from utility import get_random_browser


def get_request_url_and_heads():
    user_agent = get_random_browser()

    current_time = int(time.time())

    headers = {"header": user_agent}

    base_url = "https://www.toutiao.com/api/pc/feed/?" \
               "max_behot_time=" + str(current_time) + \
               "&category=__all__" \
               "&utm_source=toutiao&widen=1" \
               "&tadrequire=true" \
               "&_signature=_02B4Z6wo00501F855IQAAIBBEnc23cKQIQBfPeAAAEhJef8RGG57l30lSTnrOiLz0L" \
               ".cdTNfuacO5XDz1TcOqWicL7-wAHTtLFl9BYUCkqUOZdir-IZjfh1WbxY0MuoIKE3bZwvIzq11h54rd4 "

    return base_url, headers


def get_response_html():
    request_url, headers = get_random_browser()
    response = requests.get(url=request_url, headers=headers)
    # .encode("utf-8").decode("unicode_escape")

    global response_json
    response_json = json.loads(response.text)
    if response_json["message"] == "error":
        get_response_html()

    return response_json


def data_to_file():
    data = response_json["data"]

    for i in range(len(data)):
        data_dict = data[i]

        with open("toutiao.json", "a+") as f:
            json.dump(data_dict, f, ensure_ascii=False)
            f.write("\n")


df=pd.read_json("toutiao.json",lines=True)
df.to_excel("toutiao.xlsx")