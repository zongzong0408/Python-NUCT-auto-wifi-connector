"""
    version C v2.2

    using Python 3.7.0
    using Windows 11 Home

    using selenium 3.0.0
    using urllib 1.2.01

    using Chrome browser driver
"""

from selenium import webdriver
import requests
import time
import sys
import os

TEST_URL                    = "https://www.google.com"
WAL_URL                     = "http://172.16.170.254:1000/login?admin"

DETECT_CONNECT_ALIVE_TIME   = 10
OPEN_PAGE_WAITE_TIME        = 3
CLEAR_TERMINAL_SCR_TIMES    = 50
ACCOUNT = {
    "account"   : "ncutvip@ncut.edu.tw",
    "password"  : "23924505"
}

_header = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"
}

def reconnect(url: str, account: str, password: str) -> bool:

    try:

        driver = webdriver.Firefox()

        driver.get(url)

        sys.stdout.write("提示：開啟連接視窗程序...\n")

        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

        sys.stdout.write("提示：正在尋找帳密輸入框...\n")

        username_field.send_keys(account)
        password_field.send_keys(password)

        sys.stdout.write("提示：正在輸入帳密資訊...\n")
        
        time.sleep(OPEN_PAGE_WAITE_TIME)

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()
    
        sys.stdout.write("提示：成功送出帳密資訊。\n")

        driver.quit()

    except:

        driver.quit()

        sys.stdout.write("錯誤：模組出現非預期錯誤。\n")

    if (dynamic_detect_connect(url = TEST_URL) == True):

        sys.stdout.write("提示：重新連結網路成功\n")

        return True

    else:

        sys.stdout.write("錯誤：重新連結網路失敗\n")

        return False
    
def dynamic_detect_connect(url: str) -> bool:

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

    now_times = 0

    while True:

        if (dynamic_detect_connect(url = TEST_URL) == False):
            
            sys.stdout.write(f"錯誤：網路異常，啟動重連程序...\n")
            sys.stdout.write(f"提示：該程序大致在 {OPEN_PAGE_WAITE_TIME + 2} 後完成執行。\n")

            reconnect(url = WAL_URL, account = ACCOUNT["account"], password = ACCOUNT["password"])

        sys.stdout.write(f"提示：網路一切正常，請安心使用，等待 {DETECT_CONNECT_ALIVE_TIME} 秒後再次檢測。(times: {now_times})\n")

        time.sleep(DETECT_CONNECT_ALIVE_TIME)

        now_times += 1

        if (now_times >= CLEAR_TERMINAL_SCR_TIMES):
            
            os.system("cls")
            now_times = 0

    # return

main()