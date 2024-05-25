# NUCT WAL auto connector 勤益科大網路連接腳本
## v2 lightness version 輕量化版本

國立勤益科技大學，全自動連接網路腳本，開源程式碼，沒有任何技術專利，安心使用。  


## 開發環境

- Windows Home 11
- Python 3.7.0
- selenium 4.5
- urllib3 1.26.6


## 如何執行

步驟 一：如果沒有安裝 `Python` 請先[安裝](https://www.python.org/downloads/)，版本大於 `>= 3.7.0`。  

步驟 二：安裝 `selenium` 視覺化爬蟲模組（使用版本 `>= 4.5`）。  

```bash
pip install selenium==4.5.0
```
> 備註：簡單方便輸入帳號密碼和送出表單。

步驟 三：安裝相依模組（`requests`、`subprocess`）。  

```bash
pip install requests
```
> 備註：檢測網路連線和獲得 HTTP 代碼。

```bash
pip install subprocess
```
> 備註：獲得網路登入介面內網 IP 位置。


步驟 四：`ssl` 的版本與 `urllib3` 不相容，[參見議題](https://stackoverflow.com/questions/76187256/importerror-urllib3-v2-0-only-supports-openssl-1-1-1-currently-the-ssl-modu)。  

```bash
pip install urllib3==1.26.6
```

步驟 五：啟動腳本。

- 1. 點擊 `auto-reconnect.py`  
---
- 2. 在資料夾內開啟終端機
        ```bash
        python auto-reconnect.py
        ```

大功告成！它會自動執行，當你網路斷線，它會自動重新連線，過程非常快，不會有斷網的感覺，24/7執行。


## 貢獻

都是自己寫的，哈哈，這頗簡單ㄚ。  
可以輸入自己的帳號密碼，或是用內建學校公用的帳密。


## 著作權

此專案受到 [GPL-3.0](https://www.gnu.org/licenses/gpl-3.0.zh-tw.html) 保障。  
Copyright © 2024 zong zong ( zongzong0408 )