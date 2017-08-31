
# This file contains  all the modules used to get/parse  information from a
# webpage. We will split the file into packages later, as each module grows

import urllib.request # Get raw data from a webpage
import sys            # Parse input arguments

# 'help' prints information on how to use the program
def help():
    help_str = '''
    The program expects 1 argument that is the URL to parse.

    Example:
        python3 parse_webpage.py "https://pythonspot.com/en/urllib-tutorial-python-3/"
        '''
    print(help_str)

# Get input arguments that is a webpage
if (len(sys.argv) != 2):
    print("Insufficient Arguments")
    help()
    sys.exit(-1)

url = sys.argv[1]

html = urllib.request.urlopen(url).read()

print(html)
