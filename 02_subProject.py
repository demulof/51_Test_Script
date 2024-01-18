from imports import *
from infoSetting import *

logging_config()

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = initialize_driver()
        cls.wait = WebDriverWait(cls.driver, 10)
        logging.info('「新增分支計畫」測試開始')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('「新增分支計畫」測試結束')

    def click_button(self, xpath):
        click_button(self.driver, xpath)
    
    def send_input(self, xpath, value):
        send_input(self.driver, xpath, value)

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
        開啟並登入履約系統
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

    def test_03_CreateSubproject(self):
        """
        新增分支計畫資料
        """        
        logging.info('新增分支計畫資料開始')
        self.click_button("//body/div[@id='app']/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/div[1]/div[1]")
        logging.info('點擊預算管控目錄鈕')

        time.sleep(1)
        self.click_button("/html[1]/body[1]/div[1]/section[1]/aside[1]/div[1]/div[2]/ul[1]/li[3]/ul[1]/li[1]/ul[1]/div[1]/div[1]/div[2]/div[1]/span[1]")
        logging.info('點擊分支計畫鈕')

        self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[4]/div[2]/button[1]"))
        )
        logging.info('頁面中有新增分支計畫鈕')

        self.click_button("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[4]/div[2]/button[1]")
        logging.info('點擊新增分支計畫鈕')

        self.wait.until(
            EC.presence_of_all_elements_located((By.XPATH, "/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]")),
        )
        logging.info('頁面中有分支計畫名稱輸入欄')

        time.sleep(1)
        now = datetime.now()
        dateTime = datetime.strftime(now, '%Y-%m-%d-%H-%M-%S')
        global subProjectName
        subProjectName = "腳本測試" + dateTime
        self.send_input("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[3]/form[1]/div[1]/div[1]/div[1]/div[2]/div[1]/input[1]", subProjectName)
        logging.info('輸入分支計畫名稱')

        self.click_button("/html[1]/body[1]/div[1]/section[1]/section[1]/main[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/button[2]")
        logging.info('點擊完成編輯鈕')

        self.wait.until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[3]/div/div[1]/span'), subProjectName)
            )
        logging.info('頁面中的標題變為該分支計畫名稱')

if __name__ == '__main__':
    single_test(Test)