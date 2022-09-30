# module for command line and arguments
import sys
# module for command line arguments parser
import getopt 
from datetime import datetime

argv=sys.argv
arg_search_words = ""
search_words = ""
# arg_help = "{0} -f <firstdate> -l <lastdate> ".format(argv[0])
arg_help = "{0} -s <search_words> ".format(argv[0])
    
    
try:
    opts, args = getopt.getopt(argv[1:], "h:s:", ["help", "search_words="])
except:
    print(arg_help)
    sys.exit(2)

for opt, arg in opts:
    if opt in ("-h", "--help"):
        # print the help message
        print(arg_help)  
        sys.exit(2)
    elif opt in ("-s", "--search_words"):
        arg_search_words = arg
        # convert string to date
        search_words = arg_search_words

