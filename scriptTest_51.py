<<<<<<< HEAD
from imports import *

## 帳號
global account
account = "tsuno"
## 密碼
global passWord
passWord = "Samuer20000118*"
## 分支計畫名稱 subProjectName
## 計畫名稱 projectName
## 標案名稱 bidName
=======
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
## 上傳檔案
import pyautogui
##  時間api
from datetime import datetime


>>>>>>> aab64432afabd8009bf4f7d404973ee6ed29a290

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
<<<<<<< HEAD
=======
        ## 關閉伺服器
>>>>>>> aab64432afabd8009bf4f7d404973ee6ed29a290
        self.driver.quit()

    def click_button(self, xpath):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()
    
    def send_input(self, xpath, value):
        input = self.driver.find_element(By.XPATH, xpath)
        input.send_keys(value)

    ## Test Case 的命名方式務必以「test_01_* ~ test_99_*」為主，讓爬蟲依照順序走
    ## """裡面的註解就是報表產生後的CASE描述文字。
    def test_01_Extension(self):
        """
        設置驗證碼插件
        """   
        ## 配合chrome插件Request-Interceptor
        self.send_input("/html/body/app-root/div/nav/div/ul/li[3]/sl-tooltip/button/input", "D:\\test_script\\request_interceptor_rules.json")
        self.click_button("/html/body/app-root/div/nav/div/ul/li[5]/sl-tooltip/app-toggle/div")
        self.click_button("/html/body/app-root/div/nav/div/ul/li[4]/sl-tooltip/button")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
    
    def test_02_Login(self):
        """
        開啟並登入履約系統
        """
<<<<<<< HEAD
        global wait
        wait = WebDriverWait(self.driver, 10)
        ## 等待頁面中有帳號輸入欄位
        wait.until(
            EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]"))
        )
        ## 輸入帳號
        self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]", account)
        ## 輸入密碼
        self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/input[1]", passWord)
        ## 輸入驗證碼
        self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/input[1]", "111111")
        ## 點擊登入鈕
        self.click_button("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]")
=======
        ## 等待頁面中有帳號輸入欄位
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]"))
            )
        finally:
            ## 輸入帳號
            self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]", "tsuno")
            ## 輸入密碼
            self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/input[1]", "Samuer20000118*")
            ## 輸入驗證碼
            self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/input[1]", "111111")
            ## 點擊登入鈕
            self.click_button("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]")
>>>>>>> aab64432afabd8009bf4f7d404973ee6ed29a290

    def test_03_CreateSubproject(self):
        """
        新增分支計畫資料
        """
        ## 等待頁面中有預算管控目錄鈕
<<<<<<< HEAD
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]"))
        )
        ## 點擊預算管控目錄鈕
        self.click_button("//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
        time.sleep(1)
        ## 點擊分支計畫鈕
        self.click_button("/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/ul[1]/li[1]/ul[1]/div[1]/div[1]/div[2]/div[1]/span[1]")
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[4]/div[2]/button[1]"))
        )
        ## 點擊新增分支計畫鈕
        self.click_button("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[4]/div[2]/button[1]")
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")),
        )
        # subProjectNum = self.driver.find_element(By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[3]/div/div[3]/form/div[3]/div/div/div[2]').get_attribute('value')
        # wait.until(
        #     EC.text_to_be_present_in_element((By.XPATH,'//*[@id="app"]/section/section/main/div/div/div[3]/div/div[3]/form/div[3]/div/div/div[2]'), '')
        # )
        time.sleep(1)
        ## 目前時間轉文字
        now = datetime.now()
        DateTime = datetime.strftime(now, '%Y-%m-%d-%H-%M-%S')
        global subProjectName
        subProjectName = "腳本分支" + DateTime
        ## 輸入分支計畫名稱
        self.send_input("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]", subProjectName)
        ## 點擊完成編輯
        self.click_button("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[2]")
        wait.until(
            EC.text_to_be_present_in_element((By.XPATH, "//*[@id='app']/section/section/main/div/div/div[3]/div/div[1]/span"), subProjectName)
        )
=======
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]"))
            )
        finally:
            ## 點擊預算管控目錄鈕
            self.click_button("//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
            time.sleep(1)
            ## 點擊分支計畫鈕
            self.click_button("/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/ul[1]/li[1]/ul[1]/div[1]/div[1]/div[2]/div[1]/span[1]")
            try:
                element = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[4]/div[2]/button[1]"))
                )
            finally:
                ## 點擊新增分支計畫鈕
                self.click_button("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[4]/div[2]/button[1]")
                try:
                    element = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]"))
                    )
                    subProjectId = self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[3]/div[1]/div[1]/div[2]")
                    element = WebDriverWait(self.driver, 10).until(
                        subProjectId.get_attribute("value")  
                    )
                finally:
                    ## 目前時間轉文字
                    now = datetime.now()
                    DateTime = datetime.strftime(now, '%Y-%m-%d-%H-%M-%S')
                    global subProjectName
                    subProjectName = "腳本測試" + DateTime
                    ## 輸入分支計畫名稱
                    self.send_input("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]", subProjectName)
                    ## 點擊完成編輯
                    self.click_button("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[2]")
>>>>>>> aab64432afabd8009bf4f7d404973ee6ed29a290

    def test_04_CreateProject(self):
        """
        新增計畫資料
        """
<<<<<<< HEAD
        self.click_button("/html/body/div/section/aside/div/div[2]/ul/li[3]/ul/li/ul/div[1]/div/div[2]/div[2]/span[1]")
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/section/section/main/div/div/div[4]/div[2]/button"))
        )
        ## 點擊新增計畫資料鈕
        self.click_button("/html/body/div/section/section/main/div/div/div[4]/div[2]/button")
        ## 等待分支計畫名稱輸入欄
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pane-basic"]/div[2]/form/div[2]/div/div/div[2]/div/div/input'))
        )
        self.click_button('//*[@id="pane-basic"]/div[2]/form/div[2]/div/div/div[2]/div/div/input')
        ## 等待分支計畫名稱選單展開
        wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul'))
        )
        subProjectName_ul = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul')
        options = subProjectName_ul.find_elements(By.TAG_NAME,'li')
        for option in options:
            if subProjectName in option.text:
                option.click()
                break
        
        # projectNum = self.driver.find_element(By.XPATH, '//*[@id="pane-basic"]/div[5]/form/div[2]/div/div/div[2]/div').text
        wait.until(
            # projectNum != '暫無資料'
            lambda driver: not EC.text_to_be_present_in_element((By.XPATH, '//*[@id="pane-basic"]/div[5]/form/div[2]/div/div/div[2]/div'), '暫無資料')
        )
        
        self.send_input('//*[@id="pane-basic"]/div[5]/form/div[1]/div/div[1]/div[2]/div[2]/input', 'あーあ')
        time.sleep(300)

=======
    
>>>>>>> aab64432afabd8009bf4f7d404973ee6ed29a290



# basedir就是存放所有TEST Case的目錄，讓它爬 pattern = '*.py'，所以要做哪個類別的測試就指定哪個前贅
# 路徑盡量放D槽喔，除非你的電腦只有C
basedir = "D:/test_script/"
if __name__ == '__main__':
    # 取得資料夾目錄底下，符合後面任何副檔名為.py，並進行所有test的測試項目
<<<<<<< HEAD
    # test_suite = unittest.defaultTestLoader.discover(
    #     basedir, pattern='*.py')
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
=======
    test_suite = unittest.defaultTestLoader.discover(
        basedir, pattern='*.py')
>>>>>>> aab64432afabd8009bf4f7d404973ee6ed29a290

    # 測試結果加入到 BeautifulReport 套件內
    result = BeautifulReport(test_suite)

    # 結果產生Report 檔案名稱為 filename, 敘述為 description, log_path 預設放在跟目錄底下就行
    result.report(filename='report',
                  description='51test', log_path='D:/test_script/')

# 啟動自動化指令，在終端機輸入: & C:/Users/你的使用者帳號/AppData/Local/Programs/Python/Python+版本號/python.exe d:/資料夾名稱/檔案名稱.py