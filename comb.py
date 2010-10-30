import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split("/journal_search")[0])
#sys.path.append("/home/edhelms/workspace/ResearchScripts")

from journal_search import slr
from journal_search.tests import test_runner

if __name__ == '__main__':
    if 'test' in sys.argv:
        test_runner.run()
    elif 'search' in sys.argv:
        slr.run_search(int(sys.argv[2]))
    else:
        print "Invalid arguments"
