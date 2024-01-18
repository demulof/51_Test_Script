from imports import *
from infoSetting import *

logging_config()

class Test(unittest.TestCase): 
    @classmethod
    def setUpClass(cls):
        cls.driver = initialize_driver()
        cls.wait = WebDriverWait(cls.driver, 10)
        logging.info('「新增計畫資料」測試開始')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('「新增計畫資料」測試結束')

    def click_button(self, xpath):
        click_button(self.driver, xpath)
    
    def send_input(self, xpath, value):
        send_input(self.driver, xpath, value)

    def clear_send_input(self, xpath, value):
        clear_send_input(self.driver, xpath, value)

    def test_01_Extension(self):
        """
        設置驗證碼插件
        """   
        logging.info('設置驗證碼插件開始')
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
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]"))
        )
        self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[1]/div[1]/div[2]/input[1]", account)
        self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[2]/div[1]/div[2]/input[1]", passWord)
        self.send_input("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[2]/div[1]/input[1]", "111111")
        self.click_button("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[1]")
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]"))
        )
        logging.info('登入履約系統結束')

    def test_03_CreateProject(self):
        """
        新增計畫資料
        """
        logging.info('新增計畫資料開始')   
        self.click_button("//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
        logging.info('點擊預算管控目錄鈕')

        time.sleep(1)
        self.click_button("/html/body/div/section/aside/div/div[2]/ul/li[3]/ul/li/ul/div[1]/div/div[2]/div[2]/span[1]")
        logging.info('點擊計畫資料鈕')

        self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/section/section/main/div/div/div[4]/div[2]/button"))
        )
        logging.info('頁面中有新增計畫資料鈕')

        self.click_button("/html/body/div/section/section/main/div/div/div[4]/div[2]/button")
        logging.info('點擊新增計畫資料鈕')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pane-basic"]/div[2]/form/div[2]/div/div/div[2]/div/div/input'))
        )
        logging.info('頁面中有分支計畫名稱輸入欄')

        self.click_button('//*[@id="pane-basic"]/div[2]/form/div[2]/div/div/div[2]/div/div/input')
        logging.info('點擊分支計畫名稱輸入欄')

        self.wait.until(
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

        self.wait.until_not(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="pane-basic"]/div[5]/form/div[2]/div/div/div[2]/div'),'暫無資料')
        )
        logging.info('計畫編號不為暫無資料')

        now = datetime.now()
        dateTime = datetime.strftime(now, '%Y-%m-%d-%H-%M-%S')
        global projectName
        projectName = "腳本計畫" + dateTime
        self.send_input('//*[@id="pane-basic"]/div[5]/form/div[1]/div/div[1]/div[2]/div[2]/input', projectName)
        logging.info('輸入計畫名稱')

        self.send_input('//*[@id="pane-basic"]/div[5]/form/div[5]/div/div/div[2]/div/div[1]/input', accountName)
        logging.info('選擇會計承辦人員')

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul/li/span'))
        )
        logging.info('會計承辦人員選單展開')

        self.click_button('/html/body/div[3]/div[1]/div[1]/ul/li/span')
        logging.info('點擊設定會計承辦人員')

        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[1]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總施工費)')

        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[2]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總設計費)')

        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[3]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總監造費)')

        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[4]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總專管費)')

        self.clear_send_input('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[5]/td[3]/div/div/div/input', 1000000000)
        self.click_button('//*[@id="pane-basic"]/div[7]/div[1]/span')
        logging.info('輸入預算編列(總工管費)')

        self.driver.execute_script('arguments[0].scrollIntoView(true);', self.driver.find_element(By.XPATH, '//*[@id="pane-basic"]/div[9]/button'))
        logging.info('滾動頁面至新增預算按鈕')

        self.click_button('//*[@id="pane-basic"]/div[9]/button')
        logging.info('點擊新增一筆')
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input'))
        )
        logging.info('頁面中有新增的預算欄位')

        self.click_button('//*[@id="pane-basic"]/div[8]/div[3]/table/tbody/tr[6]/td[2]/div/div/div/input')
        self.wait.until(
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

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="tab-測試用預算費用"]/div'))
        )
        logging.info('有新增的費用項目tab')

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="tab-測試用預算費用"]/div'))
        )
        logging.info('新增費用項目tab可點')

        self.click_button('//*[@id="tab-測試用預算費用"]/div')
        logging.info('點擊測試用費用項目')

        self.clear_send_input('//*[@id="pane-測試用預算費用"]/div/form/div[1]/div/div[1]/div[2]/div/input', 1000000000)
        logging.info('輸入測試用費用項目預算編列')

        self.send_input('//*[@id="pane-basic"]/div[14]/div/div[2]/div/div/input', 'D:\\test_script\\files\\docx檔.docx')
        logging.info('計畫資料上傳檔案')

        self.click_button('//*[@id="app"]/section/section/main/div/div/div[3]/div/div[1]/button')
        logging.info('點擊完成編輯')

        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'el-loading-mask'))
        )
        logging.info('等待完成編輯中')

        WebDriverWait(self.driver, 300).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, 'el-loading-mask'))
        )
        logging.info('等待完成編輯成功')
      
if __name__ == '__main__':
    single_test(Test)