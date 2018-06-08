#! /usr/bin/env python3
# coding=utf-8
import unittest
from utilities.BeautifulReport import BeautifulReport
from utilities.logger import logger
import os
from tomorrow import threads
from config import config


def add_case(case_path=config.Path.test_cases_dir, rule="test*.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                  pattern=rule,
                                                  top_level_dir=None)
    return discover

@threads(3)
def run(test_suit):
    result = BeautifulReport(test_suit)
    result.report(filename='report.html', description='测试deafult报告', log_path='report')

if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    for i in cases:
        print(i)
        run(i)
