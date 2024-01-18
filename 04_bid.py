from imports import *
from infoSetting import *

logging_config()

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = initialize_driver()
        cls.wait = WebDriverWait(cls.driver, 10)
        logging.info('「新增標案資料」測試開始')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('「新增標案資料」測試結束')

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

    def test_03_CreateBid(self):
        """
        新增標案資料
        """
        logging.info('新增標案資料開始')
        self.click_button("//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
        logging.info('點擊預算管控目錄鈕')

        time.sleep(1)
        self.click_button('//*[@id="app"]/section/aside/div/div[2]/ul/li[3]/ul/li/ul/div[2]/div/div[2]/div[1]/span[1]')
        logging.info('點擊標案資料鈕')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[4]/div[2]/button'))
        )
        logging.info('頁面中有新增標案鈕')

        self.click_button('//*[@id="app"]/section/section/main/div/div/div[4]/div[2]/button')
        logging.info('點擊新增標案鈕')

        self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/article/div'))
        )
        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/article/div'))
        )
        logging.info('頁面中loading出現並結束(讀取完成)')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[1]/div/div/div[2]/div[1]/div/input')
        logging.info('點擊計畫名稱輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul'))
        )
        logging.info('計畫名稱選單展開')

        projectName_ul = self.driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul')
        options = projectName_ul.find_elements(By.TAG_NAME,'li')
        for option in options:
            if projectName in option.text:
                option.click()
                break
        logging.info('點擊設定計畫名稱')

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/section/section/main/div/article/section[4]/div[1]/button[2]'))
        )
        logging.info('標案基本資料可點擊(計畫基本資料帶入成功)')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/div[1]/button[2]')
        logging.info('點擊標案基本資料頁籤')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div/button'))
        )
        logging.info('跳出提醒彈窗')

        self.click_button('/html/body/div[2]/div/div[2]/div/div[2]/div/button')
        logging.info('點擊確認')

        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, '/html/body/div[2]'))
        )
        logging.info('提醒彈窗消失')

        now = datetime.now()
        dateTime = datetime.strftime(now, '%Y-%m-%d-%H-%M-%S')
        global bidName
        bidName = "腳本測試" + dateTime
        self.send_input('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[3]/div/div/div[2]/div[1]/div[2]/input', bidName)
        logging.info('輸入標案名稱')

        self.send_input('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[5]/div/div/div[2]/div/input', '會計科目測試')
        logging.info('輸入會計科目')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[11]/div/div/div[2]/div[1]/div[2]/input')
        logging.info('點擊承辦人員輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul'))
        )
        logging.info('承辦人員選單展開')

        time.sleep(1)

        promoter_ul = self.driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/ul')
        options = promoter_ul.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if accountName in option.text:
                self.wait.until(
                    EC.element_to_be_clickable(option)
                )
                option.click()
                break
        logging.info('點擊承辦人員選項')

        self.send_input('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[12]/div/div[1]/div[2]/div[1]/textarea', '標案概述測試')
        logging.info('輸入標案概述')

        self.send_input('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[13]/div/div/div[2]/div[1]/textarea', '預期成果測試')
        logging.info('輸入預期成果')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[14]/div/div/div[2]/div[1]/div[1]/input')
        logging.info('點擊工程標案屬性輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul'))
        )
        logging.info('工程標案屬性選單展開')
        
        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul/li[1]'))
        )
        logging.info('工程標案屬性可點擊')

        random_bidAttribute = random.randint(1,2)
        self.click_button(f'/html/body/div[4]/div[1]/div[1]/ul/li[{random_bidAttribute}]')
        logging.info('點擊工程標案屬性')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[15]/div/div/div[2]/div[1]/div[1]/input')
        logging.info('點擊工程標案屬性類型輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul'))
        )
        logging.info('工程標案屬性類型選單展開')

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[1]/div[1]/ul/li[1]'))
        )
        logging.info('工程標案屬性類型可點擊')

        if random_bidAttribute == 1:
            random_bidAttributeType = random.randint(1,8)
            self.click_button(f'/html/body/div[5]/div[1]/div[1]/ul/li[{random_bidAttributeType}]')
        
        else:
            random_bidAttributeType = random.randint(1,6)
            self.click_button(f'/html/body/div[5]/div[1]/div[1]/ul/li[{random_bidAttributeType}]')
        logging.info('點擊工程標案屬性類型')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[16]/div/div/div[2]/div[1]/div[1]/div[2]/button')
        logging.info('點擊工程標案地點編輯標記紐')

        self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="pane-point"]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input'))
        )
        logging.info('縣市輸入欄可點擊')

        self.click_button('//*[@id="pane-point"]/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/input')
        logging.info('點擊縣市輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul'))
        )
        logging.info('縣市選單展開')

        city_ul = self.driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/ul')
        options = city_ul.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if cityName in option.text:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                self.wait.until(
                    EC.element_to_be_clickable(option)
                )
                option.click()
                break
        logging.info('點擊縣市')

        time.sleep(0.5)

        self.click_button('//*[@id="pane-point"]/div[2]/div/div[2]/div[1]/div/div[2]/div/div/input')
        logging.info('點擊鄉鎮區輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul'))
        )
        logging.info('縣市選單展開')
        
        area_ul = self.driver.find_element(By.XPATH, '/html/body/div[7]/div[1]/div[1]/ul')
        options = area_ul.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if areaName in option.text:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                self.wait.until(
                    EC.element_to_be_clickable(option)
                )
                option.click()
                break
        logging.info('點擊鄉鎮區')

        time.sleep(0.5)

        self.click_button('//*[@id="pane-point"]/div[2]/div/div[2]/div[1]/div/div[3]/div/div[1]/input')
        logging.info('點擊街路輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul'))
        )
        logging.info('街路選單展開')
        
        road_ul = self.driver.find_element(By.XPATH, '/html/body/div[8]/div[1]/div[1]/ul')
        options = road_ul.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if roadName in option.text:
                self.driver.execute_script("arguments[0].scrollIntoView();", option)
                self.wait.until(
                    EC.element_to_be_clickable(option)
                )
                option.click()
                break
        logging.info('點擊街路')

        self.send_input('//*[@id="pane-point"]/div[2]/div/div[2]/div[1]/div/div[4]/div/input', remainingAddresses)
        logging.info('輸入剩餘地址')

        self.click_button('//*[@id="pane-point"]/div[2]/div/div[3]/div[2]/div[1]/div/input')
        time.sleep(0.5)
        logging.info('點擊其他處讓座標帶入')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[16]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/button')
        logging.info('點擊下一步')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pane-point"]/div[2]/div/div[3]/table/tbody/tr/td[2]/div/a/i'))
        )
        logging.info('頁面中有垃圾桶icon(進入到下一步)')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[16]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[2]/button')
        logging.info('點擊確認鈕')

        self.send_input('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[4]/div/div[2]/div/div/input', 'D:\\test_script\\files\\docx檔.docx')
        logging.info('標案資料上傳檔案')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/div[1]/button[3]')
        logging.info('點擊機關及設計單位基本資料頁籤')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[1]/div/div/div[2]/div[1]/div[1]/input'))
        )
        logging.info('業務單位選項出現')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[1]/div/div/div[2]/div[1]/div[1]/input')
        logging.info('點擊業務單位欄位')

        promoterUnit = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, 'el-cascader-panel'))
        )
        options = promoterUnit.find_elements(By.TAG_NAME, 'li')
        for option2nd in options:
            if promoterUnit_2nd in option2nd.text:
                option2nd.click()
                logging.info('點擊業務單位第二層選項')
                options = promoterUnit.find_elements(By.TAG_NAME, 'li')
                for option3rd in options: 
                    if promoterUnit_3rd in option3rd.text:
                        option3rd.click()
                        logging.info('點擊業務單位第三層選項')
                        options = promoterUnit.find_elements(By.TAG_NAME, 'li')
                        for option4th in options:
                            if promoterUnit_4th in option4th.text:
                                option4th.click()
                                logging.info('點擊業務單位第四層選項')
                                break

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[3]/div/div/div[2]/div[1]/input')
        self.send_input('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[3]/div/div/div[2]/div[1]/input', promoterNum)
        logging.info('輸入業務單位電話')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[4]/section/div[2]/form/div[2]/div/div/div[2]/div[1]/div/input')
        logging.info('點擊業務單位聯絡人輸入欄')

        self.wait.until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul'))
        )
        logging.info('業務單位聯絡人選單展開')

        time.sleep(1)

        contactPerson_ul = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/ul')
        options = contactPerson_ul.find_elements(By.TAG_NAME, 'li')
        for option in options:
            if accountName in option.text:
                self.wait.until(
                    EC.element_to_be_clickable(option)
                )
                option.click()
                break
        logging.info('點擊業務單位聯絡人選項')

        self.click_button('//*[@id="app"]/section/section/main/div/article/section[3]/div[2]/button[3]')
        logging.info('點擊完成編輯鈕')

        self.wait.until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app"]/section/section/main/div/article/section[3]/div[1]/span'), bidName)
        )
        logging.info('頁面中的標題變為該標案名稱')
        
if __name__ == '__main__':
    single_test(Test)