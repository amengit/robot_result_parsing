import csv
import os.path
import tempfile
from robot.api import SuiteVisitor


class CollectKws(SuiteVisitor):
    """
    This library is for collecting kws from test case to see kw usage statistics
    usage: add prerebotmodifier option to rfcli command:
    --prerebotmodifier CollectKws
    CollectKws.py must be in the module search path.
    e.g.: python -m robot.rebot --prerebotmodifier CollectKws output.xml
    or python -m robot.rebot --prerebotmodifier CollectKws:CDC_keyword_statistics.tsv output.xml
    """
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self, filename='keyword_statistics.tsv'):
        outpath = os.path.join(tempfile.gettempdir(), filename)
        print('tempdir is {}'.format(outpath))
        self.outfile = open(outpath, 'wb+')
        self.tsv_writer = csv.writer(self.outfile, delimiter='\t')

    def start_suite(self, suite):
        self.tsv_writer.writerow(['Test suite', '{}'.format(suite.longname)])

    def start_test(self, test):
        self.tsv_writer.writerow(['', 'Test case', '{}'.format(test.longname)])

    def start_keyword (self, kw):
        self.tsv_writer.writerow(['', '', 'Keyword', '{}'.format(kw.name), '{}'.format(kw.elapsedtime)])

    def close(self):
        self.outfile.close()
