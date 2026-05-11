# 勤益科大校園網路自動重連工具

給我朋友做的。
這是一個專為 **國立勤益科技大學 (NCUT)** 校園網路環境設計的自動化維護工具。  
當系統偵測到網路斷線時，會自動透過 Selenium 模擬瀏覽器行為，完成閘道器驗證頁面的登入程序，確保網路連線不間斷。  

## 🚀 核心功能

* **即時網路監控**：定時透過 `requests` 檢測 Google 連線狀態，確保偵測的準確性。
* **動態閘道偵測**：自動呼叫 `ipconfig` 解析當前環境的「預設閘道 (Default Gateway)」，適應不同宿舍或教學大樓的網路環境。
* **無頭模式執行 (Headless Mode)**：採用 Chrome 無頭模式技術，在背景安靜執行，完全不干擾使用者的工作或遊戲。
* **可攜式環境支援**：專為免安裝版 Chrome 設計，避免因系統瀏覽器更新導致的驅動程式版本衝突。
* **自動跳過 VPN**：具備特定網段（如 `26.0.0.1`）過濾機制，防止在 VPN 連線狀態下進行無效重連。

## 🛠️ 環境需求

本專案主要針對 Windows 系統開發，需具備以下環境：

* **Python 3.8+**
* **Chrome 瀏覽器 (Portable)**：需放置於專案根目錄。
* **ChromeDriver**：版本需與 Chrome 瀏覽器版本對應。

## 📂 專案結構

為了確保 `run.py` 正常運作，請保持以下目錄結構：

```text
Python-NUCT-auto-wifi-connector/
├── run.py                 # 核心執行程式
├── chromedriver.exe       # Chrome 驅動程式
├── chrome-win64/          # Chrome 可攜式瀏覽器資料夾
│   └── chrome.exe         # 瀏覽器主程式
└── requirements.txt       # 相關套件清單

```

## 📦 安裝步驟

1. **複製儲存庫**：
```bash
git clone https://github.com/zongzong0408/Python-NUCT-auto-wifi-connector.git
cd Python-NUCT-auto-wifi-connector
```


2. **安裝必要套件**：
```bash
pip install -r requirements.txt
```


3. **配置瀏覽器**：
請確保 `chromedriver.exe` 與 `chrome-win64/` 資料夾已正確放置於專案根目錄。

## 🖥️ 使用說明

直接執行 `run.py` 即可啟動監控服務：

```bash
python run.py
```

### 系統輸出範例：

* `系統： 網路正常`：表示目前網路連線中。
* `系統： 成功開啟瀏覽器`：偵測到斷線，正在啟動自動化連線流程。
* `系統： 輸入密碼` -> `系統： 送出密碼`：自動完成校園網頁驗證。

## ⚙️ 程式碼配置 (Configuration)

在 `run.py` 中，您可以根據需求修改以下變數：

* `wait_time`：設定網頁載入的逾時秒數（預設為 10 秒）。
* `username_field` / `password_field`：腳本內建使用 `ncutvip` 帳號，如需更換請修改 `send_keys` 內容。

## ⚠️ 免責聲明與注意事項

1. **資訊安全**：本腳本目前將帳號密碼以明文方式儲存於原始碼中，請勿將包含個人帳密的檔案上傳至公開儲存庫。
2. **合理使用**：請遵守國立勤益科技大學校園網路使用規範，本工具僅供學術研究與個人便利使用，請勿用於非法用途。
3. **相容性**：若校園登入頁面之 HTML 結構變更（如標籤 ID 或 XPATH 改變），可能導致腳本失效，屆時需手動更新定位符。