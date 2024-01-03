from imports import *

## 帳號
global account
account = "tsuno"
## 密碼
global passWord
passWord = "Samuer20000118*"
## 角色名稱
global accountName
accountName = '10346'
## 分支計畫名稱
global subProjectName
subProjectName = '12-test-分支'
## 計畫名稱 projectName

logging.basicConfig(level=logging.INFO, filename='測試訊息.html', filemode='w', 
                    format='%(asctime)s - %(levelname)s - %(message)s'+'<br>')

## 設定Chrome的瀏覽器彈出時遵照的規則
## 防止瀏覽器上頭顯示「Chrome正受自動控制」
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension('D:\\test_script\\1.6.0_0.crx')

## 關閉自動記住密碼的提示彈窗
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})

class Test(unittest.TestCase): 
    @classmethod
    ## setUpClass這邊的設定是，可以讓所有Case進行過程中只開啟一次瀏覽器
    ## 執行時會依照這個順序循環一次 setUpClass > test > teardownClass
    def setUpClass(cls):      
        cls.driver = webdriver.Chrome(options = options)
        cls.action = ActionChains(cls.driver)
        cls.URL_51 = "https://demo.srgeo.com.tw/TP_PROJECT_MCP_NEW/signin/?token=G67tAAZ5CYm53aNBnyWRUP5Y7mPTgNGx"
        cls.URL_ex = "chrome-extension://bfgblailifedppfilabonohepkofbkpm/index.html"
        cls.driver.get(cls.URL_51)
        cls.driver.execute_script("window.open('','_blank');")
        cls.driver.switch_to.window(cls.driver.window_handles[1])
        cls.driver.get(cls.URL_ex)
        cls.driver.maximize_window()
        logging.info('測試開始')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('測試結束')

    def click_button(self, xpath):
        button = self.driver.find_element(By.XPATH, xpath)
        button.click()
    
    def send_input(self, xpath, value):
        input = self.driver.find_element(By.XPATH, xpath)
        input.send_keys(value)

    def clear_send_input(self, xpath, value):
        input = self.driver.find_element(By.XPATH, xpath)
        input.clear()
        input.send_keys(value)

    ## 腳本起始
    def test_01_Extension(self):
        """
        設置驗證碼插件
        """   
        logging.info('設置驗證碼插件開始')
        ## 配合chrome插件Request-Interceptor
        self.send_input("/html/body/app-root/div/nav/div/ul/li[3]/sl-tooltip/button/input", "D:\\test_script\\request_interceptor_rules.json")
        self.click_button("/html/body/app-root/div/nav/div/ul/li[5]/sl-tooltip/app-toggle/div")
        self.click_button("/html/body/app-root/div/nav/div/ul/li[4]/sl-tooltip/button")
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        logging.info('設置驗證碼插件結束')
    
    def test_02_Login(self):
        """
        登入履約系統
        """
        logging.info('登入履約系統開始')

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
        
        logging.info('登入履約系統結束')

    def test_04_CreateProject(self):
        """
        新增計畫資料
        """
        logging.info('新增計畫資料開始')

        ## 等待頁面中有預算管控目錄鈕
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]"))
        )
        logging.info('頁面中有預算管控目錄鈕')
        self.click_button("//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
        logging.info('點擊預算管控目錄鈕')
        time.sleep(1)
        ## 點擊計畫資料鈕
        self.click_button("/html/body/div/section/aside/div/div[2]/ul/li[3]/ul/li/ul/div[1]/div/div[2]/div[2]/span[1]")
        logging.info('點擊計畫資料鈕')
        wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/section/section/main/div/div/div[4]/div[2]/button"))
        )
        logging.info('頁面中有新增計畫資料鈕')
        ## 點擊新增計畫資料鈕
        self.click_button("/html/body/div/section/section/main/div/div/div[4]/div[2]/button")
        logging.info('點擊新增計畫資料鈕')
        ## 等待分支計畫名稱輸入欄
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pane-basic"]/div[2]/form/div[2]/div/div/div[2]/div/div/input'))
        )
        logging.info('頁面中有分支計畫名稱輸入欄')
        self.click_button('//*[@id="pane-basic"]/div[2]/form/div[2]/div/div/div[2]/div/div/input')
        logging.info('點擊分支計畫名稱輸入欄')
        ## 等待分支計畫名稱選單展開
        wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul'))
        )
        logging.info('分支計畫名稱選單展開')
        subProjectName_ul = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul')
        options = subProjectName_ul.find_elements(By.TAG_NAME,'li')
        for option in options:
            if subProjectName in option.text:
                option.click()
                break
        logging.info('點擊設定分支計畫名稱')
        # projectNum = self.driver.find_element(By.XPATH, '//*[@id="pane-basic"]/div[5]/form/div[2]/div/div/div[2]/div').text
        wait.until_not(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="pane-basic"]/div[5]/form/div[2]/div/div/div[2]/div'),'暫無資料')
        )
        logging.info('計畫編號不為暫無資料')
        ## 目前時間轉文字
        now = datetime.now()
        DateTime = datetime.strftime(now, '%Y-%m-%d-%H-%M-%S')
        global projectName
        projectName = "腳本計畫" + DateTime
        ## 輸入計畫名稱
        self.send_input('//*[@id="pane-basic"]/div[5]/form/div[1]/div/div[1]/div[2]/div[2]/input', projectName)
        logging.info('輸入計畫名稱')
        ## 選擇會計承辦人員
        self.send_input('//*[@id="pane-basic"]/div[5]/form/div[5]/div/div/div[2]/div/div[1]/input', accountName)
        logging.info('選擇會計承辦人員')
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span'))
        )
        logging.info('會計承辦人員選單展開')
        self.click_button('/html/body/div[3]/div[1]/div[1]/ul/li/span')
        logging.info('點擊設定會計承辦人員')
        ## 輸入預算編列(總施工費)
        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總施工費)')
        ## 輸入預算編列(總設計費)
        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[2]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總設計費)')
        ## 輸入預算編列(總監造費)
        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[3]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總監造費)')
        ## 輸入預算編列(總專管費)
        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[4]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總專管費)')
        ## 輸入預算編列(總工管費)
        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[5]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總工管費)')
        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(By.XPATH, '//*[@id="pane-basic"]/div[9]/button'))
        logging.info('滾動頁面至新增預算按鈕')
        ## 點擊新增一筆
        self.click_button('//*[@id="pane-basic"]/div[9]/button')
        logging.info('點擊新增一筆')
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input'))
        )
        logging.info('頁面中有新增的預算欄位')
        # self.send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input', '測試用預算費用')
        # logging.info('輸入新增費用項目名稱')
        self.click_button('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input')
        wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul'))
        )
        logging.info('新增費用項目名稱選單展開')
        newBudgetName = '測試用預算費用'
        budgetName_ul = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul')
        options = budgetName_ul.find_elements(By.TAG_NAME,'li')
        for option in options:
            if newBudgetName in option.text:
                option.click()
                break
        logging.info('點擊新增費用項目名稱選項')
        # wait.until(
        #     EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span'))
        # )
        # logging.info('新增費用項目名稱選項可點選')
        # self.click_button('/html/body/div[4]/div[1]/div[1]/ul/li[1]/span')
        # logging.info('點擊新增費用項目名稱選項')
        self.send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[6]/td[3]/div/div/div/input', 1000000000)
        logging.info('輸入新增費用項目金額')
        self.clear_send_input('//*[@id="pane-總施工費(施工費)"]/div/form/div[1]/div/div/div[2]/div/input', 1000000000)
        logging.info('輸入總施工費預算編列')
        self.click_button('//*[@id="tab-總設計費(委託設計服務費)"]/div')
        self.clear_send_input('//*[@id="pane-總設計費(委託設計服務費)"]/div/form/div[1]/div/div[1]/div[2]/div/input', 1000000000)
        logging.info('輸入總設計費預算編列')
        self.click_button('//*[@id="tab-總監造費(委託監造技術服務費)"]/div')
        self.clear_send_input('//*[@id="pane-總監造費(委託監造技術服務費)"]/div/form/div[1]/div/div[1]/div[2]/div/input', 1000000000)
        logging.info('輸入總監造費預算編列')
        self.click_button('//*[@id="tab-總專管費(專案管理費)"]/div')
        self.clear_send_input('//*[@id="pane-總專管費(專案管理費)"]/div/form/div[1]/div/div[1]/div[2]/div/input', 1000000000)
        logging.info('輸入總專管費預算編列')
        self.click_button('//*[@id="tab-總工管費(按施工費提列工程管理費)"]/div')
        self.clear_send_input('//*[@id="pane-總工管費(按施工費提列工程管理費)"]/div/form/div[1]/div/div[1]/div[2]/div/input', 1000000000)
        logging.info('輸入總工管費預算編列')
        self.click_button('//*[@id="pane-basic"]/div[11]/div[1]/div/span[2]')
        logging.info('點擊滑動頁籤')
        # time.sleep(300)
        wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tab-測試用預算費用"]/div'))
        )
        logging.info('有新增的費用項目tab')
        wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-測試用預算費用"]/div'))
        )
        logging.info('新增費用項目tab可點')
        self.click_button('//*[@id="tab-測試用預算費用"]/div')
        logging.info('點擊測試用費用項目')
        self.clear_send_input('//*[@id="pane-測試用預算費用"]/div/form/div[1]/div/div[1]/div[2]/div/input', 1000000000)
        logging.info('輸入測試用費用項目預算編列')
        self.send_input('//*[@id="pane-basic"]/div[14]/div/div[2]/div/div/input', 'D:\\test_script\\test_files\\docx檔.docx')
        logging.info('計畫資料上傳檔案')
        self.click_button('//*[@id="app"]/section/section/main/div/div/div[3]/div/div[1]/button')
        logging.info('點擊完成編輯')
        wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-loading-mask'))
        )
        logging.info('等待完成編輯中')
        wait.until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'el-loading-mask'))
        )
        logging.info('等待完成編輯成功')
      





# basedir就是存放所有TEST Case的目錄，讓它爬 pattern = '*.py'，所以要做哪個類別的測試就指定哪個前贅
# 路徑盡量放D槽喔，除非你的電腦只有C
basedir = "D:/test_script/"
if __name__ == '__main__':
    # 取得資料夾目錄底下，符合後面任何副檔名為.py，並進行所有test的測試項目
    # test_suite = unittest.defaultTestLoader.discover(
    #     basedir, pattern='*.py')
    test_suite = unittest.TestLoader().loadTestsFromTestCase(Test)

    # 測試結果加入到 BeautifulReport 套件內
    result = BeautifulReport(test_suite)

    # 結果產生Report 檔案名稱為 filename, 敘述為 description, log_path 預設放在跟目錄底下就行
    result.report(filename='測試報告',
                  description='51test', log_path='D:/test_script/')

# 啟動測試腳本，在終端機輸入: python d:/資料夾名稱/檔案名稱.py