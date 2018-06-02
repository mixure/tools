# coding=utf-8

import unittest
import os

test_unit=unittest.TestSuite()
dir_=os.path.dirname(
            os.path.abspath(__file__))
test_dir=os.path.join(dir_,'test_cases')
discover=unittest.defaultTestLoader.discover(
            test_dir,
            pattern='test3.py',
            # top_level_dir=None
        )

for test_suite in discover:
    for test_case in test_suite:
        test_unit.addTests(test_case)

if __name__=='__main__':
    # runner=unittest.TextTestRunner()
    # runner.run(test_unit)

    # test report
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

    #  https://github.com/findyou/HTMLTestRunnerCN/tree/dev
    # import utilities.HTMLTestRunnerCN as HTMLTestRunner

    report_dir=os.path.join(dir_,'report')
    report_file=os.path.join(report_dir,'{}.html'.format(
        time.strftime('%Y-%m-%d_%H:%M')))
    fp=open(report_file,'wb')
    runner=HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title="title",
        description=u'执行情况')
    runner.run(test_unit)
    fp.close()
