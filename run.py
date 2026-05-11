from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import subprocess
import requests
import time
import sys
import os

os.environ['WDM_SSL_VERIFY'] = '0'

chromedriver_path = "./chromedriver.exe"
chrome_portable_path = "./chrome-win64/chrome.exe"

http_code = 404
wait_time = 10

def auto_reconnector() -> None:

    while (True):
    
        try:
            http_code = requests.get("https://www.google.com.tw").status_code
        except Exception as e:
            http_code = 404
            # sys.stdout.write(f"{e}")
            sys.stdout.write("系統：\t網路連接失敗\n")

        if http_code == 404:
            try:
                chrome_options = Options()
                chrome_options.binary_location = chrome_portable_path
                chrome_options.add_argument("--headless")
                chrome_options.add_argument("--disable-gpu") 
                chrome_options.add_argument("--log-level=3")
                service = Service(executable_path = chromedriver_path, log_path = os.devnull) 
                # service = Service(executable_path = chromedriver_path) 
                
                driver = webdriver.Chrome(service = service, options = chrome_options)
                
                sys.stdout.write("系統：\t成功開啟瀏覽器\n")
            except Exception as e:
                sys.stdout.write(f"{e}")
                sys.stdout.write("系統：\t錯誤 1\n")
                return
            
            try:
                ipconfig_result = subprocess.check_output(['ipconfig'], stderr = subprocess.STDOUT, shell = True, universal_newlines = True)
                ipconfig_lines = ipconfig_result.split('\n')

                default_gateway = []
                gate = None

                for line in ipconfig_lines:
                    if "預設閘道" in line or "Default Gateways" in line:
                        gate = line.split(':')[-1].strip()
                        if gate:
                            default_gateway.append(gate)
                print(default_gateway)

                if default_gateway:
                    pass
                else:
                    sys.stdout.write(f"\t\t無法找到預設閘道，請檢查您的網路設定\n")
            except Exception as e:
                sys.stdout.write(f"{e}")
                sys.stdout.write("系統：\t錯誤 2\n")
                break
            
            for gateway in default_gateway:
                try:
                    if gateway == '26.0.0.1':
                        continue
                    driver.set_page_load_timeout(wait_time)
                    driver.get(f"http://{gateway}:1000/login?admin")
                    sys.stdout.write(f"系統：\t連線 http://{gateway}:1000/login?admin\n")
                    # os.system("pause")
                    
                    driver.set_page_load_timeout(wait_time)
                    username_field = driver.find_element(By.NAME, 'username')
                    password_field = driver.find_element(By.NAME, 'password')
                    sys.stdout.write("系統：\t尋找密碼框\n")
                    # os.system("pause")

                    driver.set_page_load_timeout(wait_time)
                    username_field.send_keys("ncutvip@ncut.edu.tw")
                    password_field.send_keys("23924505")
                    sys.stdout.write("系統：\t輸入密碼\n")
                    # os.system("pause")

                    driver.set_page_load_timeout(wait_time)
                    buttom_field = driver.find_element(By.XPATH, '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button')
                    # os.system("pause")
                    buttom_field.click()
                    sys.stdout.write("系統：\t送出密碼\n")
                
                    driver.quit()
                    
                    if requests.get("https://www.google.com").status_code == 200:
                        sys.stdout.write("\t\t恢復網路連接\n")
                        break
                
                except Exception as e:
                    sys.stdout.write(f"{e}")
                    sys.stdout.write("系統：\t錯誤 3\n")
                    break

        elif http_code == 200:
            sys.stdout.write("系統：\t網路正常\n")
        
        time.sleep(1)

auto_reconnector()