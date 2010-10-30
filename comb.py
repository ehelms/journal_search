import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)).split("/journal_search")[0])

from journal_search.search import search, combiner
from journal_search.tests import test_runner

if __name__ == '__main__':
    if 'test' in sys.argv:
        test_runner.run()
    elif 'search' in sys.argv:
        if len(sys.argv) > 2:
            search.run(int(sys.argv[2]))
        else:
            search.run()
    elif 'combine' in sys.argv:
        combiner.run()
    else:
        print "Invalid arguments"
