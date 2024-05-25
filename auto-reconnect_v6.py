"""
    version C v6.0

    using Python 3.7.0
    using Windows 11 Home
    
    using selenium 4.5.0
    using urllib 1.2.01

    using Chrome browser driver
"""

from selenium import webdriver
import subprocess
import requests
import time
import sys

while (True):

    http_code = 404
    
    try:

        http_code = requests.get("https://www.google.com").status_code
    
    except Exception as e:
        
        pass

    if (http_code != 200):

        sys.stdout.write("網路連接失敗\n")

        driver = webdriver.Chrome()

        driver.implicitly_wait(5)

        ipconfig_result = subprocess.check_output(['ipconfig'], stderr = subprocess.STDOUT, shell = True, universal_newlines = True)
        ipconfig_lines = ipconfig_result.split('\n')

        for line in ipconfig_lines:
            if "預設閘道" in line:
                default_gateway = line.split(':')[-1].strip()

        driver.implicitly_wait(3)
        driver.get(f"http://{default_gateway}:1000/login?admin")

        driver.implicitly_wait(8)

        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

        driver.implicitly_wait(3)

        username_field.send_keys("ncutvip@ncut.edu.tw")
        password_field.send_keys("23924505")

        driver.implicitly_wait(3)

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()

        driver.quit()

        sys.stdout.write("恢復網路連接\n")

    else:

        sys.stdout.write("連接網路正常\n")

    time.sleep(3)