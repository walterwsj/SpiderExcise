import json
import random
import requests

"""
    # json和字符串相互转换
    # loads 用于将str(字符串类型)转换为相应类型，如dict(字典类型)，list(列表类型)等
    # dumps 是将dict(字典格式)转换为str(字符串格式)。
    # 操作文件的
    # dump 是将dict(字典格式)转换为str(字符串格式)，并且写入到json文件中
    # load 用于从json文件中读取数据
"""


def write_browser_info_to_file():
    my_user_agent = requests.get(url="https://fake-useragent.herokuapp.com/browsers/0.1.8")

    with open("browser_info.json", "w") as f:
        json.dump(my_user_agent.text, f)


def get_random_browser():
    with open("browser_info.json", "r") as f:
        browsers_json = json.load(f)
        browsers_json = json.loads(browsers_json)

        browsers = browsers_json["browsers"]
        i = random.randint(0, len(browsers))
        if i == 0:
            browser_name = "chrome"
        elif i == 1:
            browser_name = "opera"
        elif i == 2:
            browser_name = "firefox"
        elif i == 3:
            browser_name = "internetexplorer"
        else:
            browser_name = "safari"

        final_browser = browsers[browser_name][random.randint(0, len(browsers[browser_name]))]

    return final_browser

