import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.chrome.options import Options

url='http://www.baidu.com'

# def get_screenshot_as_file(func):
#         def wrapper(self):
#             try:
#                 func(self)
#             except:
#                 self.dr.get_screenshot_as_file('{}.png'.format(
#                     func.__name__) )
#         return wrapper

class Core(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        Core.dr=webdriver.Firefox()
        # Core.imgs=[]

        #Chrome headless mode
        # chrome_options=Options()
        # chrome_options.add_argument('--headless')
        # Core.ff=webdriver.Chrome(chrome_options=chrome_options)

        Core.dr.get(url)

    @classmethod
    def tearDownClass(cls):
        Core.dr.quit()

if __name__=='__main__':
    unittest.main()







