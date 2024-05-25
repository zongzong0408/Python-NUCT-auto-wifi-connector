"""
    version CF v4.0

    using Python 3.7.0
    using Windows 11 Home

    using selenium 3.0.0
    using urllib 1.2.01

    using Chrome OR FireFox browser driver
"""

import requests
import time
import sys
import os

try:
    
    from selenium import webdriver

except Exception as e:

    sys.stdout.write("system ERROR:\t error on LINE <16>\n")
    sys.stdout.write("system ERROR:\t the selenium module hasn't been installed yet.\n")
    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
    sys.stdout.write("system INFO:\t visit https://pypi.org/project/selenium/ to get more information.\n")
    sys.stdout.write("system INFO:\t you can run <$: pip install selenium > in your terminal to quick install package.\n")
    sys.stdout.write("system INFO:\t after that you need install the drive match you target browser then that's all.\n")

else:

    sys.stdout.write("system INFO:\t successfully input selenium module.\n\n")

"""
    constant values description

    TEST_IS_CONNECT_WAL_URL     : (str) the URL that you can check if you are disconnect to WAL or not.
    TARGET_TO_CONNECT_WAL_URL   : (str) the URL that you connect WAL.
    DETECT_CONNECT_ALIVE_TIME   : (int uint8_t) the range that you detect is connecting to WAL or not.
    OPEN_PAGE_WAITE_TIME        : (int uint8_t) the time that you wait program insert information to website then close page.
    CLEAR_TERMINAL_SCR_TIMES    : (int uint8_t) the time that you clear your local terminal screen.
    LOGIN_ACCOUNT               : (dic) the dictionary store your login account and password information.
"""

TEST_IS_CONNECT_WAL_URL     = "https://www.google.com"
TARGET_TO_CONNECT_WAL_URL   = "http://192.168.0.2"

DETECT_CONNECT_ALIVE_TIME   = 10
OPEN_PAGE_WAITE_TIME        = 3
CLEAR_TERMINAL_SCR_TIMES    = 50

LOGIN_ACCOUNT = {
    "account"   : "ncutvip@ncut.edu.tw",
    "password"  : "23924505"
}

def connect(url: str, account: str, password: str) -> None:

    try:

        '''
            only in selenium version below v4.6.0
            can use below code
        '''
        option = webdriver.ChromeOptions()
        option.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome(executable_path = "./chromedriver.exe", options = option)

    except Exception as e:

        sys.stdout.write("system ERROR:\t error on LINE <58>\n")
        sys.stdout.write("system ERROR:\t cannot open Chrome browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t program is going to shutdown. pls using popular browser.\n")

        # try:

        #     driver = webdriver.Chrome("./firefoxdriver.exe")

        # except Exception as e:

        #     sys.stdout.write("system ERROR:\t error on LINE <58>\n")
        #     sys.stdout.write("system ERROR:\t cannot open Firefox browser.\n")
        #     sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        #     sys.stdout.write("system INFO:\t program is going to shutdown. pls using popular browser.\n")

        # else:

        #     sys.stdout.write("system INFO:\t successfully open FireFox driver.\n")

    else:

        sys.stdout.write("system INFO:\t successfully open Chrome driver.\n")
        sys.stdout.write("system INFO:\t now is going to open FireFox.\n")

    try:

        driver.implicitly_wait(OPEN_PAGE_WAITE_TIME)
        driver.get(url)

    except Exception as e:

        sys.stdout.write("system ERROR:\t error on LINE <73>\n")
        sys.stdout.write("system ERROR:\t cannot connect your target url.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write(f"system INFO:\t you are trying connect {url}, pls try another LAN IP.\n")

    else:

        sys.stdout.write(f"system INFO:\t successfully connect target url. {url}\n")

    try:

        username_field = driver.find_element("name", "username")
        password_field = driver.find_element("name", "password")

    except Exception as e:
    
        sys.stdout.write("system ERROR:\t error on LINE <91>\n")
        sys.stdout.write("system ERROR:\t cannot find input field and bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls find available and correct input field XPath.\n")

    else:

        sys.stdout.write("system INFO:\t successfully find input field and bottom.\n")

    try:

        username_field.send_keys(account)
        password_field.send_keys(password)

    except Exception as e:
    
        sys.stdout.write("system ERROR:\t error on LINE <104 & 105>\n")
        sys.stdout.write("system ERROR:\t cannot insert account and password data to input field.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls find available and correct input field XPath.\n")

    else:

        sys.stdout.write("system INFO:\t successfully input account and password information.\n")

    try:

        time.sleep(OPEN_PAGE_WAITE_TIME)

    except Exception as e:

        sys.stdout.write("system ERROR:\t error on LINE <120>\n")
        sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

    else:

        sys.stdout.write("system ERROR:\t successfully waiting website get and refresh information.\n")

    try:

        username_field = driver.find_element("xpath", '//*[@id="login_form_div"]/form/table/tbody/tr[1]/td[2]/button').click()
    
    except Exception as e:

        sys.stdout.write("system ERROR:\t error on LINE <135>\n")
        sys.stdout.write("system ERROR:\t cannot click input bottom.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls input correct sleep time {  belongs to R }.\n")

    else:

        sys.stdout.write("system INFO: successfully send account & password information.\n")

    try:
        
        driver.quit()

    except Exception as e:

        sys.stdout.write("system ERROR:\t error on LINE <150>\n")
        sys.stdout.write("system ERROR:\t cannot quit selenium browser.\n")
        sys.stdout.write(f"system DETAIL:\t {e}\n\n")
        sys.stdout.write("system INFO:\t pls quit it by yourself or shutdown program.\n")

    else:

        sys.stdout.write("system INFO: successfully quit selenium browser.\n")

    return
    
def detect_connection(url: str) -> bool:

    status_code = 404

    try:

        status_code = requests.get(url).status_code
    
    except Exception:

        sys.stdout.write("system ERROR:\t error on LINE <171>\n")
        sys.stdout.write(f"system ERROR:\t cannot ping {url}, make sure WAL connection is available.\n")
        sys.stdout.write(f"system DETAIL:\t {status_code}\n\n")
        sys.stdout.write("system INFO:\t detect WAL connection is failed. the program is going to reconnect WAL.\n")

        return False

    else:

        return True

def main() -> None:

    if (LOGIN_ACCOUNT["account"] == "..." or LOGIN_ACCOUNT["password"] == "..."):

        sys.stdout.write("system ERROR:\t error on LINE <188>\n")
        sys.stdout.write("system ERROR:\t your are not input login account & password yet.\n")
        sys.stdout.write(f"system INFO:\t pls key your data to LOGIN_ACCOUNT[] list.\n")

        return

    counting_start_time = time.time()
    detection_times = 1

    while True:

        if (detect_connection(TEST_IS_CONNECT_WAL_URL) == False):
            
            sys.stdout.write("system ERROR:\t cannot connect WAL.\n")
            sys.stdout.write(f"system INFO:\t program will finished reconnect WAL after {OPEN_PAGE_WAITE_TIME} times.\n")

            connect(TARGET_TO_CONNECT_WAL_URL, LOGIN_ACCOUNT["account"], LOGIN_ACCOUNT["password"])

        time_tuple  = time.localtime()
        time_string = time.strftime("%m/%d/%Y, %H:%M:%S", time_tuple)
        sys.stdout.write(f"system INFO:\t (now time: {time_string}) WAL connection is all well.\n")
        sys.stdout.write(f"system INFO:\t it is going to check connection after {DETECT_CONNECT_ALIVE_TIME} seconds. (detection times {detection_times})\n")
        counting_end_time = time.time()
        
        try:

            sys.stdout.write(f"system INFO:\t program has already run {round((counting_end_time - counting_start_time) / 60 / 60)} hours.\n\n")

        except Exception as e:

            sys.stdout.write("system ERROR:\t error on LINE <216>\n")
            sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

        else:

            sys.stdout.write("system ERROR:\t successfully waiting website get and refresh information.\n")

        try:

            time.sleep(DETECT_CONNECT_ALIVE_TIME)

        except Exception as e:

            sys.stdout.write("system ERROR:\t error on LINE <231>\n")
            sys.stdout.write("system ERROR:\t cannot let python script sleeping.\n")
            sys.stdout.write(f"system DETAIL:\t {e}\n\n")
            sys.stdout.write("system INFO:\t pls input correct sleep time { time belongs to R }.\n")

        else:

            sys.stdout.write("system ERROR:\t successfully waiting website get and refresh information.\n")

        detection_times += 1

        if (detection_times >= CLEAR_TERMINAL_SCR_TIMES):
            
            try:
            
                os.system("cls")
            
            except Exception as e:
            
                sys.stdout.write("system ERROR:\t error on LINE <250>\n")
                sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                sys.stdout.write("system INFO:\t this program is developed under Windows system, if <cls> command isn't working, then it's going to run <clear> command.\n")

                try:
            
                    os.system("clear")

                except Exception as e:
                    
                    sys.stdout.write("system ERROR:\t error on LINE <261>\n")
                    sys.stdout.write("system ERROR:\t cannot clear terminal screen.\n")
                    sys.stdout.write(f"system DETAIL:\t {e}\n\n")
                    sys.stdout.write("system INFO:\t pls using Windows or Linux system, make sure that is popular OS. the program cannot clear terminal screen.\n")

            finally:

                detection_times = 0

    # return

main()