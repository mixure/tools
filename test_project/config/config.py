import os
import time

class Path:
    project_dir='/Users/yeap/local/personal/tools/test_project'

    test_cases_dir=os.path.join(project_dir,'test_cases')

    report_dir=os.path.join(project_dir,'report')

    report_file=os.path.join(report_dir,'{}.html'.format(
        time.strftime('%Y-%m-%d_%H:%M')))

    log_dir=os.path.join(project_dir,'report')

class Log:
    pass


