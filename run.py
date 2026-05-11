from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import subprocess
import requests
import time
import sys
import os

"""
    *** 自訂義參數 ***
"""
# 腳本偵測網路是否斷線的時間間隔
wait_detect_timeout = 1
# VPN 排除預設閘道
vpn_bypass_default_gateway = ['26.0.0.1']
# 自動模式 開啟：1 關閉：0
loop_mode = 1
# 除錯模式 開啟：1 關閉：0
debug_mode = 0
# 清除輸出的數目
clear_count = 100

"""
    固定常數
"""
# 解除 SSL 認證
os.environ['WDM_SSL_VERIFY'] = '0'
# Chrome 驅動路徑
chromedriver_path = "./chromedriver.exe"
# Chrome 可攜式瀏覽器路徑
chrome_portable_path = "./chrome-win64/chrome.exe"
# 錯誤代碼
http_code = 404
# 腳本連項網頁的時間間隔
wait_load_timeout = 10

def auto_reconnector() -> bool:

    try:
        chrome_options = Options()
        chrome_options.binary_location = chrome_portable_path
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu") 
        chrome_options.add_argument("--log-level=3")
        service = Service(executable_path = chromedriver_path, log_path = os.devnull) 
        driver = webdriver.Chrome(service = service, options = chrome_options)
        sys.stdout.write("系統：\t成功開啟瀏覽器\n")
    except Exception as e:
        if debug_mode:
            sys.stdout.write(f"{e}")
        sys.stdout.write("系統錯誤：\t初始化瀏覽器失敗\n")
        return False
    
    try:
        ipconfig_result = subprocess.check_output(['ipconfig'], stderr = subprocess.STDOUT, shell = True, universal_newlines = True)
        ipconfig_lines = ipconfig_result.split('\n')
        default_gateway = []
        for line in ipconfig_lines:
            if "預設閘道" in line or "Default Gateway" in line:
                gate = line.split(':')[-1].strip()
                if gate != None and gate != "":
                    default_gateway.append(gate)
        print(f"系統：\t成功尋找到預設閘道：{default_gateway}\n")
        if default_gateway == []:
            sys.stdout.write(f"系統錯誤：\t無法找到預設閘道，請檢查您的網路設定\n")
            return False
    except Exception as e:
        if debug_mode:
            sys.stdout.write(f"{e}")
        sys.stdout.write("系統錯誤：\t無法找到預設閘道，請檢查您的網路設定\n")
        return False
    
    for gateway in default_gateway:
        if gateway in vpn_bypass_default_gateway:
            continue
        sys.stdout.write(f"系統：\t預計連線 http://{gateway}:1000/login?admin\n")
        try:
            driver.set_page_load_timeout(wait_load_timeout)
            driver.get(f"http://{gateway}:1000/login?admin")
            sys.stdout.write(f"系統：\t連線完成 http://{gateway}:1000/login?admin\n")
        except Exception as e:
            sys.stdout.write("系統：\t無法連線網頁\n")
            return False
        try:
            driver.set_page_load_timeout(wait_load_timeout)
            username_field = driver.find_element(By.NAME, 'username')
            password_field = driver.find_element(By.NAME, 'password')
            sys.stdout.write("系統：\t尋找密碼框\n")
        except Exception as e:
            sys.stdout.write("系統：\t無法尋找密碼框\n")
            return False
        try:
            driver.set_page_load_timeout(wait_load_timeout)
            username_field.send_keys("ncutvip@ncut.edu.tw")
            password_field.send_keys("23924505")
            sys.stdout.write("系統：\t輸入密碼\n")
        except Exception as e:
            sys.stdout.write("系統：\t無法輸入密碼\n")
            return False
        try:
            driver.set_page_load_timeout(wait_load_timeout)
            buttom_field = driver.find_element(By.XPATH, '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button')
            buttom_field.click()
            sys.stdout.write("系統：\t送出密碼\n")
        except Exception as e:
            sys.stdout.write("系統：\t無法送出密碼\n")
            return False
        try:
            driver.quit()
            sys.stdout.write("系統：\t有關閉網頁\n")
        except Exception as e:
            sys.stdout.write("系統：\t無法關閉網頁\n")
            return False
        
        sys.stdout.write("系統：\t成功運行完整程式\n")
            
        if requests.get("https://www.google.com").status_code == 200:
            sys.stdout.write("系統：\t恢復網路連接 code 200\n")
            return True
    return True

def main() -> None:
    if loop_mode:
        sys.stdout.write("系統：\t自動運行 auto_reconnector()\n")
        count = 0
        while True:
            http_code = 000
            try:
                http_code = requests.get("https://www.google.com.tw").status_code
                sys.stdout.write(f"系統：\t網路運行 code {http_code}\n")
            except:
                http_code = 404
            finally:
                if http_code == 404:
                    sys.stdout.write(f"系統：\t網路運行 code {http_code}\n")
                    sys.stdout.write(f"系統：\t{auto_reconnector()}\n")
                else:
                    pass
            count += 1
            if count == clear_count:
                if os.name == 'nt':
                    subprocess.run("cls", shell = True)
                else:
                    subprocess.run("clear", shell = True)
            time.sleep(wait_detect_timeout)
    else:
        sys.stdout.write("系統：\t運行一次 auto_reconnector()\n")
        sys.stdout.write(f"系統：\t{auto_reconnector()}\n")

        if debug_mode:
            input("debug mode: wait any key to exit.")
            return
        else:
            return

if __name__ == "__main__":
    main()