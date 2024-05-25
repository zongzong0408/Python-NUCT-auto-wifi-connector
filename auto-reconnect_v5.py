"""
    version C v5.6

    using Python 3.7.0
    using Windows 11 Home
    
    using selenium 4.5.0
    using urllib 1.2.01

    using Chrome browser driver
"""

from inspect import currentframe, getframeinfo
import subprocess
import requests
import winreg
import shutil
import time
import sys
import os
# import re

try:
    
    from selenium import webdriver

    sys.stdout.write("system OK:\t successfully input selenium module.\n\n")

except Exception as e:

    sys.stdout.write("system ERROR:\t error on LINE <16>\n")
    sys.stdout.write("system ERROR:\t the selenium module hasn't been installed yet.\n")
    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
    sys.stdout.write("system INFO:\t visit https://pypi.org/project/selenium/ to get more information.\n")
    sys.stdout.write("system INFO:\t you can run <$: pip install selenium > in your terminal to quick install package.\n")
    sys.stdout.write("system INFO:\t after that you need install the drive match you target browser then that's all.\n")

"""
    constant values description

    TEST_IS_CONNECT_WAL_URL     : (str) the URL that you can check if you are disconnect to WAL or not.
    TARGET_TO_CONNECT_WAL_URL   : (str) the URL that you connect WAL.
    DETECT_CONNECT_ALIVE_TIME   : (int uint8_t) the range that you detect is connecting to WAL or not.
    OPEN_PAGE_WAITE_TIME        : (int uint8_t) the time that you wait program insert information to website then close page.
    CLEAR_TERMINAL_SCR_TIMES    : (int uint8_t) the time that you clear your local terminal screen.
    LOGIN_ACCOUNT               : (dic) the dictionary store your login account and password information.
"""

TEST_IS_CONNECT_WAL_URL     = "https://www.google.com/"
TARGET_TO_CONNECT_WAL_URL   = "http://172.16.170.254:1000/login?"

DETECT_CONNECT_ALIVE_TIME   = 10
OPEN_PAGE_WAITE_TIME        = 3
CLEAR_TERMINAL_SCR_TIMES    = 50
BROWSER                     = "chrome"

LOGIN_ACCOUNT = {
    "account"   : "ncutvip@ncut.edu.tw",
    "password"  : "23924505"
}

def connect(url: str, account: str, password: str) -> None:

    if (BROWSER == "chrome"):

        try:

            a = time.time()
            
            option = webdriver.ChromeOptions()
            option.add_argument('--headless=new')
            option.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Chrome(options = option)
            
            b = time.time()
            init = round(b - a)

            sys.stdout.write(f"system INFO:\t initialize Chrome drive cost {init} second(s).\n")
            sys.stdout.write("system OK:\t successfully open Chrome driver.\n\n")

        except Exception as e:

            frameinfo = getframeinfo(currentframe())
            sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
            sys.stdout.write("system ERROR:\t cannot open Chrome browser.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write("system INFO:\t ...\n\n")
            # sys.stdout.write("system OK:\t now is going to open FireFox.\n")

    elif (BROWSER == "firefox"):

        try:

            a = time.time()
            
            option = webdriver.FirefoxOptions()
            option.add_experimental_option("excludeSwitches", ["enable-logging"])
            driver = webdriver.Firefox(options = option)
            
            b = time.time()
            init = round(b - a)

            sys.stdout.write(f"system INFO:\t initialize Firefox drive cost {init} second(s).\n")
            sys.stdout.write("system OK:\t successfully open Firefox driver.\n\n")

        except Exception as e:

            frameinfo = getframeinfo(currentframe())
            sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
            sys.stdout.write("system ERROR:\t cannot open Firefox browser.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write("system INFO:\t ...\n\n")

    try:

        driver.implicitly_wait(OPEN_PAGE_WAITE_TIME)
        driver.get(url)

        sys.stdout.write(f"system OK:\t successfully connect target url. {url}\n\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        
        status_code = detect_http_connection(url)

        if (status_code != 200):

            sys.stdout.write(f"system ERROR:\t cannot connect your target url, error http code {status_code}.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write(f"system INFO:\t you are trying connect {url}, pls try another LAN IP.\n\n")
        
        else:

            sys.stdout.write(f"system OK:\t successfully get request {status_code}.\n")
            sys.stdout.write(f"system INFO:\t you are already connected school WAL.\n")

        driver.quit()
        return

    try:

        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

        sys.stdout.write("system OK:\t successfully find input field and bottom.\n\n")

    except Exception as e:
        
        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot find input field and bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls find available and correct input field XPath.\n\n")

    try:

        username_field.send_keys(account)
        password_field.send_keys(password)

        sys.stdout.write("system OK:\t successfully input account and password information.\n")

        time.sleep(OPEN_PAGE_WAITE_TIME)

        sys.stdout.write("system OK:\t successfully waiting website get and refresh information.\n\n")

    except Exception as e:
        
        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot insert account and password data to input field.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")

    try:

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()

        sys.stdout.write("system OK : successfully send account & password information.\n\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot click input bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time {  belongs to R }.\n\n")

    try:
        
        driver.quit()

        sys.stdout.write("system OK: successfully quit selenium browser.\n\n")

    except Exception as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t cannot quit selenium browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls quit it by yourself or shutdown program.\n\n")

    return
    
def detect_connection(url: str) -> bool:

    status_code = detect_http_connection(url)

    if status_code == 200:

        sys.stdout.write("system OK:\t successfully get WAL.\n")

        return True
    
    else:

        sys.stdout.write(f"system ERROR:\t cannot ping {url}, make sure WAL connection is available.\n")
        sys.stdout.write(f"system DETAIL:\t {status_code}\n\n")
        sys.stdout.write("system INFO:\t detect WAL connection is failed. the program is going to reconnect WAL.\n")

        return False 

def detect_http_connection(url: str) -> int:

    try:

        return requests.get(TEST_IS_CONNECT_WAL_URL).status_code

    except requests.exceptions.HTTPError as e:
    
        return 504
    
    except requests.exceptions.SSLError as e:
    
        return 495
    
    except requests.exceptions.ConnectionError as e:
    
        return 503
    
    except requests.exceptions.Timeout as e:
    
        return 408

def detect_default_gateway() -> str:

    try:

        # output = subprocess.check_output(["ipconfig", "/all"], universal_newlines=True)
        # gateway_match = re.search(r"Default Gateway.*: ([\d.]+)", output)

        ipconfig_result = subprocess.check_output(['ipconfig'], stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        ipconfig_lines = ipconfig_result.split('\n')

        for line in ipconfig_lines:
            if "預設閘道" in line:
                default_gateway = line.split(':')[-1].strip()
                return default_gateway
                
        return default_gateway
    
    except subprocess.CalledProcessError as e:

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write(f"system DETAIL:\t {e.output}\n\n")
        
        return None

def copy_driver_and_add_path(file_dir: str) -> bool:

    target_dir = os.path.join(os.path.dirname(sys.executable), "Scripts", os.path.basename(file_dir))

    try:
    
        shutil.copyfile(file_dir, target_dir)

        sys.stdout.write(f"system OK:\t file '{file_dir}' copied to '{target_dir}' successfully.\n")

    except FileNotFoundError:
    
        sys.stdout.write("system ERROR:\t file not found!\n")
    
        return False

    except shutil.SameFileError:
    
        sys.stdout.write("system ERROR:\t source and destination are the same file.\n")

        return False

    # except shutil.IsADirectoryError:
    
    #     sys.stdout.write("system ERROR:\t destination is a directory.\n")
        
    #     return False

    _key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_ALL_ACCESS)
    current_path_value, _ = winreg.QueryValueEx(_key, 'PATH')

    if target_dir not in current_path_value:

        new_path_value = f"{current_path_value};{target_dir}"
        winreg.SetValueEx(_key, "PATH", 0, winreg.REG_EXPAND_SZ, new_path_value)

        sys.stdout.write(f"system OK:\t directory '{target_dir}' added to user's PATH variable.\n")

    else:

        sys.stdout.write(f"system INFO:\t directory '{target_dir}' already exists in user's PATH variable.\n")

        return None

    winreg.CloseKey(_key)

    os.environ["PATH"] = new_path_value

    _path = os.environ.get("PATH", "")

    if target_dir not in _path:

        os.environ["PATH"] = f"{target_dir}"
        sys.stdout.write(f"system OK:\t script path '{target_dir}' added to PATH variable successfully.\n\n")
    
        return True

    else:

        sys.stdout.write("system INFO:\t script path already exists in PATH variable.\n\n")

        return True

def main() -> None:

    os.system("title NCUT wifi connector v5")

    TARGET_TO_CONNECT_WAL_URL = f"http://{detect_default_gateway()}:1000/login?"

    sys.stdout.write(f"system INFO:\t the Default Gateway is '{TARGET_TO_CONNECT_WAL_URL}'\n\n")

    if (BROWSER == "chrome"):

        if (copy_driver_and_add_path("./driver/chromedriver.exe") == False):

            frameinfo = getframeinfo(currentframe())

            sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
            sys.stdout.write("system ERROR:\t call function copy_driver_and_add_path() error.\n\n")
            # sys.stdout.write(f"system DETAIL:\t {e}\n\n")

            return

    elif (BROWSER == "firefox"):

        if (copy_driver_and_add_path("./driver/firefoxdriver.exe") == False):

            frameinfo = getframeinfo(currentframe())

            sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
            sys.stdout.write("system ERROR:\t call function copy_driver_and_add_path() error.\n\n")
            # sys.stdout.write(f"system DETAIL:\t {e}\n\n")

            return
        
        else:

            sys.stdout.write(f"system OK:\t successfully copy file and add path to PATH.\n")

    if (LOGIN_ACCOUNT["account"] == "..." or LOGIN_ACCOUNT["password"] == "..."):

        frameinfo = getframeinfo(currentframe())
        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
        sys.stdout.write("system ERROR:\t your are not input login account & password yet.\n")
        sys.stdout.write(f"system INFO:\t pls _key your data to LOGIN_ACCOUNT[] list.\n\n")

        return
    
    else:

        sys.stdout.write(f"system OK:\t successfully read ACCOUNT[] data.\n\n")

    counting_start_time = time.time()
    detection_times = 1

    while True:

        if (detect_connection(TEST_IS_CONNECT_WAL_URL) == False):
            
            sys.stdout.write("system ERROR:\t program cannot connect WAL.\n")
            sys.stdout.write("system INFO:\t program is trying reconnect WAL.\n\n")

            try:
                
                connect(TARGET_TO_CONNECT_WAL_URL, LOGIN_ACCOUNT["account"], LOGIN_ACCOUNT["password"])
            
            except Exception as e:

                frameinfo = getframeinfo(currentframe())
                sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                sys.stdout.write("system ERROR:\t cannot run function -> connect()\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")

                sys.stdout.write("system ERROR:\t cannot connect WAL.\n")
                sys.stdout.write(f"system INFO:\t program will finished reconnect WAL after {OPEN_PAGE_WAITE_TIME} seconds.\n\n")
                time.sleep(OPEN_PAGE_WAITE_TIME)

                # break

                while detect_connection(TEST_IS_CONNECT_WAL_URL) == False:

                    sys.stdout.write("system ERROR:\t cannot connect WAL.\n")
                    sys.stdout.write(f"system INFO:\t program will finished reconnect WAL after {OPEN_PAGE_WAITE_TIME} seconds.\n\n")
                    time.sleep(OPEN_PAGE_WAITE_TIME)

        else:

            time_tuple  = time.localtime()
            time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
            sys.stdout.write(f"system INFO:\t (now time: {time_string}) WAL connection is all well.\n")
            sys.stdout.write(f"system INFO:\t it is going to check connection after {DETECT_CONNECT_ALIVE_TIME} seconds. (detection times {detection_times})\n")
            counting_end_time = time.time()
            
            try:

                sys.stdout.write(f"system INFO:\t program has already run {round((counting_end_time - counting_start_time) / 60 / 60)} hours.\n\n")

            except Exception as e:

                frameinfo = getframeinfo(currentframe())
                sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

            try:

                time.sleep(DETECT_CONNECT_ALIVE_TIME)

            except Exception as e:

                frameinfo = getframeinfo(currentframe())
                sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

            detection_times += 1

            if (detection_times >= CLEAR_TERMINAL_SCR_TIMES):
                
                try:
                
                    os.system("cls")
                
                except Exception as e:
                
                    frameinfo = getframeinfo(currentframe())
                    sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                    sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                    sys.stdout.write("system INFO:\t this program is developed under Windows system, if <cls> command isn't working, then it's going to run <clear> command.\n")

                    try:
                
                        os.system("clear")

                    except Exception as e:

                        frameinfo = getframeinfo(currentframe())              
                        sys.stdout.write(f"system ERROR:\t error on LINE <{frameinfo.lineno}>\n")
                        sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                        sys.stdout.write("system INFO:\t pls using Windows or Linux system, make sure that is popular OS. the program cannot clear terminal screen.\n")

                finally:

                    detection_times = 0

    # return

main()