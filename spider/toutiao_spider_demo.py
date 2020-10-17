# Spider Excise
import random
import requests
import json
import time


def get_one_user_agent():
    my_user_agent = requests.get(url="https://fake-useragent.herokuapp.com/browsers/0.1.8")
    agent_json = json.loads(my_user_agent.text)
    browsers = agent_json["browsers"]

    # 随机出来一个浏览器类型
    i = random.randint(0, len(browsers))
    if i == 0:
        browser_name = "chrome"
    elif i == 1:
        browser_name = "opera"
    elif i == 2:
        browser_name = "firebox"
    elif i == 3:
        browser_name = "internetexplorer"
    else:
        browser_name = "safari"

    final_browser = browsers[browser_name][random.randint(0, len(browsers[browser_name]))]

    current_time = int(time.time())

    header = {
        "user-agent": final_browser}
    response = requests.get(
        url="https://www.toutiao.com/api/pc/feed/?"
            "max_behot_time=" + str(current_time) +
            "&category=__all__"
            "&utm_source=toutiao&widen=1"
            "&tadrequire=true"
            "&_signature=_02B4Z6wo00501F855IQAAIBBEnc23cKQIQBfPeAAAEhJef8RGG57l30lSTnrOiLz0L"
            ".cdTNfuacO5XDz1TcOqWicL7-wAHTtLFl9BYUCkqUOZdir-IZjfh1WbxY0MuoIKE3bZwvIzq11h54rd4 "
        , headers=header)
    print(response.text.encode("utf-8").decode("unicode_escape"))


get_one_user_agent()
