# coding=utf-8

import unittest
import os
from config import config
from utilities.logger import logger

import time,sys
# http://tungwaiyip.info/software/HTMLTestRunner.html
if sys.version_info.major==3:
        # HTMLTestRunner3 是在HTMLTestRunner 上修改的
    import utilities.HTMLTestRunner3 as HTMLTestRunner
else:
    import utilities.HTMLTestRunner as HTMLTestRunner

    #支持截图，2／3都可以
    # https://github.com/GoverSky/HTMLTestRunner_cn
import utilities.HTMLTestRunner_cn as HTMLTestRunner

    # https://github.com/findyou/HTMLTestRunnerCN/tree/dev
import utilities.HTMLTestRunnerCN as HTMLTestRunner

def test_unit():
    test_unit=unittest.TestSuite()
    test_dir=config.Path.test_cases_dir
    discover=unittest.defaultTestLoader.discover(
            test_dir,
            pattern='test*.py',
            # top_level_dir=None
        )

    for test_suite in discover:
        for test_case in test_suite:
            test_unit.addTests(test_case)
    return test_unit

def run(test_unit):
    runner=unittest.TextTestRunner()
    runner.run(test_unit)

def run_with_report(test_unit):
    report_file=config.Path.report_file
    fp=open(report_file,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="title",
        description=u'执行情况')
    runner.run(test_unit)
    fp.close()

def run_with_BeautifulReport(test_unit):
    # python3 使用BeautifulReport，report路径写在BeautifulReport里面
    from utilities.BeautifulReport import BeautifulReport
    result = BeautifulReport(test_unit)
    result.report(filename='report.html', description='测试deafult报告', log_path='report')

def send_mail():
    import mail1

if __name__=='__main__':
    test_unit=test_unit()
    # run(test_unit)
    run_with_report(test_unit)
    # run_with_BeautifulReport(test_unit)



