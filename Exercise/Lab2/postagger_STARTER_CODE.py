"""
USE: python <PROGNAME> (options) 
OPTIONS:
    -h : print this help message and exit
    -d FILE : use FILE as data to create a new lexicon file
    -l FILE : create OR read lexicon file FILE
    -t FILE : apply lexicon to test data in FILE
"""
################################################################

import sys, re, getopt
# Command line options handling, and help
# For the Command Line formate:
'''
     > python postagger_STARTER_CODE.py -l traning_data.txt -t test_data.txt
'''

class Commandline:
    def __init__(self):
        opts, args = getopt.getopt(sys.argv[1:], 'hd:l:t:')
        # This command 'h' doesn't require the parameters and foe the d,l,
        opts = dict(opts)
        if '-h' in opts:
            self.printHelp()
        if len(args)>0:
            print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
            self.printHelp()
        if '-l' not in opts:
            print("\n** ERROR: must specify lexicon file name (opt: -l) **", file=sys.stderr)
            self.printHelp()
        # read the file which
        self.read_file(opts)

    def printHelp(self):
        help = __doc__.replace('<PROGNAME>', sys.argv[0], 1)
        print('-' * 60, help, '-' * 60, file=sys.stderr)
        sys.exit()

    def read_file(self,opts):
        summary_dict = dict()
        with open(opts['-l'],'r')  as train_file:
            for line in train_file:
                # Use the Regex to split the vocabulary
                result = re.findall(
                    r"(?:\w+)?[.']?[\w]+/\w+|[%'`.]{1,2}/\w+|[.,]/[.,]|\w+\\/\w+/\w+|",  # TODO: something wrong in there
                    line)
                print(result)
                # for item in result:
                #     # for each string(item) we should use the Regex to seperate them and divide them into different tokens
                #     item_pre = re.findall(r"\w+(?!/)", item)
                #     item_aft = re.findall(r"(?!/)\w+", item)





if __name__ == '__main__':
    config = Commandline()









