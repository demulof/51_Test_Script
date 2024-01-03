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
from datetime import datetime
from selenium.common.exceptions import StaleElementReferenceException
import random
## 在當前終端機顯示log
import logging
## 自動開啟檔案
import platform
import subprocess