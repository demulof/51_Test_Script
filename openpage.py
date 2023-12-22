from selenium import webdriver
from selenium.webdriver.chrome.options import Options
## BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
from BeautifulReport import BeautifulReport
## Chrome WebDriver 需要DRIVER Manager的支援
from webdriver_manager.chrome import ChromeDriverManager
## 延遲時間相關
import time
## 單元測試模組，線性測試用不到
import unittest

## 設定Chrome的瀏覽器彈出時遵照的規則
## 這串設定是防止瀏覽器上頭顯示「Chrome正受自動控制」
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension('D:\\test_script\\1.6.0_0.crx')

## 關閉自動記住密碼的提示彈窗
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})

## 我們如果要將CASE拆成幾個不同的方法，需要用一個Unitest Class包覆起來
## 然後加上修飾符@classmethod
class Test(unittest.TestCase):
    @classmethod
    ## setUpClass這邊的設定是，可以讓所有Case進行過程中只開啟一次瀏覽器
    ## 執行時會依照這個順序循環一次 setUpClass > test > teardown
    ## self則是作為我們的區域參數來定義作用域
    def setUpClass(self):
        ## 定義WebDriver以及ActionsChain的變數便於後頭應用        
        self.driver = webdriver.Chrome(options = options)
        self.action = ActionChains(self.driver)
        ## 開啟Chrome新視窗，前往履約系統網址並最大化視窗
        self.URL_51 = "https://demo.srgeo.com.tw/TP_PROJECT_MCP_NEW/signin/?token=G67tAAZ5CYm53aNBnyWRUP5Y7mPTgNGx"
        self.URL_ex = "chrome-extension://bfgblailifedppfilabonohepkofbkpm/index.html"
        self.driver.get(self.URL_51)
        self.driver.execute_script("window.open('','_blank');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(self.URL_ex)
        self.driver.maximize_window()
    
    @classmethod
    def tearDownClass(self):
        ## 關閉伺服器
        self.driver.quit()

    def click_button(self, xpath):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()
    
    def send_input(self, xpath, value):
        input = self.driver.find_element(By.XPATH, xpath)
        input.send_keys(value)

    ## Test Case 的命名方式務必以「test_01_* ~ test_99_*」為主，讓爬蟲依照順序走
    ## """裡面的註解就是報表產生後的CASE描述文字。
    ## time.sleep(number)數字代表一秒
    def test_01_extension(self):
        """
        設置驗證碼插件
        """
        #新增請求請求攔截規則(New Rule Group)
        self.click_button("/html/body/app-root/div/div[1]/app-rule-groups/div/div[1]/ul[1]/li/sl-tooltip/button")
        #點擊請求類型運算式
        self.click_button("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[1]/div/div[2]/ng-select")
        #選擇請求類型運算式
        self.click_button("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[1]/div/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[2]")
        #輸入請求值
        self.send_input("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[1]/div/div[3]/input", "https://demo.srgeo.com.tw/TP_PROJECT_SV/api/v1/Member/Login_User")
        #點擊執行動作
        self.click_button("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[2]/div/table/tbody/tr/td[1]/ng-select")
        #選擇執行動作
        self.click_button("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[2]/div/table/tbody/tr/td[1]/ng-select/ng-dropdown-panel/div/div[2]/div[7]")
        #輸入動作名稱
        self.send_input("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[2]/div/table/tbody/tr/td[2]/input", "loginFrom")
        #輸入動作值
        self.send_input("/html/body/app-root/div/div[1]/app-rule-groups/div/div[2]/app-edit-rule-group/div/div/div[2]/div/ul/li/app-edit-rule/div/div[2]/div/table/tbody/tr/td[3]/input", "0")
        #點擊開啟設定
        self.click_button("/html/body/app-root/div/nav/div/ul/li[5]/sl-tooltip/app-toggle/div")
        #點擊儲存
        self.click_button("/html/body/app-root/div/nav/div/ul/li[4]/sl-tooltip/button")

        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        # button_uploadfile = self.driver.find_element(By.XPATH, "/html/body/app-root/div/nav/div/ul/li[3]/sl-tooltip/button")
        # button_uploadfile.send_keys("D:\\test_script\\request_interceptor_rules.json")
        # button_uploadfile.click()
        # time.sleep(2)
        # file_input = self.driver.find_element(By.XPATH, '//input[@type="file"]')
        # file_input.send_keys("D:\\test_script\\request_interceptor_rules.json")
    
    def test_02_login(self):
        """
        開啟並登入履約系統
        """
        ## 等待頁面中的HTML，XPATH = '帳號欄位xpath'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]"))
            )
        finally:
            ## 找到帳號、密碼、驗證碼框的XPATH並且輸入
            ## 配合chrome插件Request-Interceptor
            ## 寫法上也通driver.find_element(By.XPATH, '//xxx')
            input_Account = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]")
            input_Account.send_keys("tsuno")
            input_Password = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/input[1]")
            input_Password.send_keys("Samuer20000118*")
            input_Captcha = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/input[1]")
            input_Captcha.send_keys("111111")
            ## 找到登入按鈕後按下
            button_Login = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]")
            button_Login.click()

            time.sleep(3)

    def test_03_createsubproject(self):
        """
        新增分支計畫資料
        """
        time.sleep(1)
        ## 等待頁面中的HTML，XPATH = '預算管控xpath'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]"))
            )
        finally:
            time.sleep(1)
        button_Budget = self.driver.find_element(By.XPATH, "//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
        button_Budget.click()

        # time.sleep(3)

# basedir就是存放所有TEST Case的目錄，讓它爬 pattern = '*.py'，所以要做哪個類別的測試就指定哪個前贅
# 路徑盡量放D槽喔，除非你的電腦只有C
basedir = "D:/test_script/"
if __name__ == '__main__':
    # 取得資料夾目錄底下，符合後面任何副檔名為.py，並進行所有test的測試項目
    test_suite = unittest.defaultTestLoader.discover(
        basedir, pattern='*.py')

    # 測試結果加入到 BeautifulReport 套件內
    result = BeautifulReport(test_suite)

    # 結果產生Report 檔案名稱為 filename, 敘述為 description, log_path 預設放在跟目錄底下就行
    result.report(filename='report',
                  description='first_test', log_path='D:/test_script/')

# 啟動自動化指令，在終端機輸入: & C:/Users/你的使用者帳號/AppData/Local/Programs/Python/Python+版本號/python.exe d:/資料夾名稱/檔案名稱.py
