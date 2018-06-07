# coding:utf-8

import unittest
from selenium import webdriver
import time

# class Testaa(unittest.TestCase):
#     u'''测试用例a的集合'''
#     @classmethod
#     def setUpClass(cls):
#         cls.driver = webdriver.Firefox()

#     def setUp(self):
#         self.driver.get("https://www.cnblogs.com/yoyoketang/")


#     def test_01(self):
#         u'''用例1：用例1的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn("悠悠", t)


#     def test_02(self):
#         u'''用例2：用例2的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn("悠悠", t)

#     def test_03(self):
#         u'''用例3：用例3的操作步骤'''
#         t = self.driver.title
#         print(t)
#         self.assertIn("悠悠", t)

#     @classmethod
#     def tearDownClass(cls):
#         cls.driver.quit()

class Test(unittest.TestCase):
    def test01(self):
        '''01'''
        self.assertTrue(True)

    def test02(self):
        '''02'''
        self.assertTrue(True)

    def test03(self):
        '''03'''
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
