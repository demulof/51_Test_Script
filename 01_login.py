from imports import *
from infoSetting import *

logging_config()

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = initialize_driver()
        cls.wait = WebDriverWait(cls.driver, 10)
        logging.info('「系統登入」測試開始')
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info('「系統登入」測試結束')

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

if __name__ == '__main__':
    single_test(Test)