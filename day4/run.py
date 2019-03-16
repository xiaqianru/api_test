import unittest
import logging
import os

from config import TEST_DIR,REPORT_DESCRIPTION,REPORT_FILE,REPORT_TITLE
from lib.htmlrunner import HTMLTestRunner


def main():
    suite = unittest.defaultTestLoader.discover(TEST_DIR)
    logging.info("{}测试开始{}".format("="*25, "="*25))
    with open(REPORT_FILE,"wb") as f:
        HTMLTestRunner(stream=f,
                       title=REPORT_TITLE,
                       description=REPORT_DESCRIPTION,
                       verbosity=2).run(suite)
    logging.info("{}测试结束{}".format("=" * 25, "=" * 25))

if __name__=="__main__":
    main()