"""
    version C v1.2

    using Python 3.7.0
    using Windows 11 Home

    using requests

    using Chrome browser driver
"""

"""
    精靈：自動化重連學校網路腳本
    時間：2023/08/08
    作者：zong zong
    緣由：...
"""

"""
    regulation:

        login page:

        http://172.16.170.254:1000/login?020f9ad3f058513d
        http://172.16.170.254:1000/login?

        connect page:

        http://172.16.170.254:1000/keepalive?040d09050b0a0403
        http://172.16.170.254:1000/keepalive?0a0a0f01000e0d09

        logout page:

        http://172.16.170.254:1000/logout?020f9ad3f058513d
        http://172.16.170.254:1000/logout?
"""

import requests
import urllib
import time
import bs4
import sys

TEST_URL    = "https://www.google.com"
WAL_URL     = "http://172.16.170.254:1000/login?admin"

DETECT_CONNECT_ALIVE_TIME = 10
ACCOUNT = {
    "account"   : "school id@student.ncut.edu.tw",
    "password"  : "id card"
}

_header = {
    "User-Agent" : "..."
}

def reconnect(url: str) -> bool:

    # print(requests.get(url, headers = _header).status_code)

    session = requests.Session()

    website_code = session.get(WAL_URL, headers = _header)

    website_fitter = bs4.BeautifulSoup(website_code.text, "html.parser")
    
    account = website_fitter.find("input", attrs = {"name" : "username"})
    password = website_fitter.find("input", attrs = {"name" : "password"})


    return True

def url_connect(url: str) -> bool:
    
    code = 404

    try:

        code = requests.get(url).status_code

        return True
    
    except Exception:

        sys.stdout.write("錯誤：無法連接網站，請檢測網路環境是否正常。\n")
        sys.stdout.write(f"提示：網路錯誤代碼 -> {code}\n")
        sys.stdout.write(f"提示：偵測到網路斷線，啟動重連程序...\n")

        return False

def main() -> None:

    # while (True):

    #     if (url_connect(url = TEST_URL) == False):

    #         reconnect(url = WAL_URL)

    reconnect(WAL_URL)

    return

main()