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
from datetime import datetime
## 在當前終端機顯示log
import logging
## 上傳檔案
import pyautogui
## 其他
import random

## Chrome設定
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_extension('D:\\test_script\\extension_files\\1.6.0_0.crx')
options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})

## 初始化WebDriver
def initialize_driver():
    driver = webdriver.Chrome(options=options)
    action = ActionChains(driver)
    logging_config()
    URL_51 = "https://demo.srgeo.com.tw/TP_PROJECT_MCP_NEW/signin/?token=G67tAAZ5CYm53aNBnyWRUP5Y7mPTgNGx"
    URL_ex = "chrome-extension://bfgblailifedppfilabonohepkofbkpm/index.html"
    driver.get(URL_51)
    driver.execute_script("window.open('','_blank');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(URL_ex)
    driver.maximize_window()
    return driver

## logging訊息匯出設定
def logging_config():
    logging.basicConfig(
        level=logging.INFO, 
        filename='測試訊息.html', 
        filemode='w', 
        format='%(asctime)s - %(levelname)s - %(message)s'+'<br>'
    )

## 腳本執行方式、測試報告匯出
# 單一測試
def single_test(test_case_class, report_filename='測試報告', report_description='51test', log_path='D:/test_script/'):
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case_class)
    result = BeautifulReport(test_suite)
    result.report(filename=report_filename, description=report_description, log_path=log_path)

# 複數測試
def multiple_test(report_filename='測試報告', report_description='51test', log_path='D:/test_script/'):
    basedir = "D:/test_script/"
    test_suite = unittest.defaultTestLoader.discover(basedir, pattern='*.py')
    result = BeautifulReport(test_suite)
    result.report(filename=report_filename, description=report_description, log_path=log_path)

## 點擊按鈕
def click_button(driver, xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()

## 欄位輸入
def send_input(driver, xpath, value):
    input_element = driver.find_element(By.XPATH, xpath)
    input_element.send_keys(value)

## 清空欄位再輸入
def clear_send_input(driver, xpath, value):
    input_element = driver.find_element(By.XPATH, xpath)
    input_element.clear()
    input_element.send_keys(value)