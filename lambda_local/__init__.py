'''
python-lambda-local: Main module

Copyright 2015 HDE, Inc.
Licensed under MIT.
'''

from __future__ import print_function
import argparse
from main import run
import sys
from multiprocessing import Process


def main():
    args = parse_args()
    try:
        p = Process(target=run, args=(args,))
        p.start()
        p.join()
    except:
        e = sys.exc_info()
        print(e[1])


def parse_args():
    parser = argparse.ArgumentParser(description="Run AWS Lambda function" +
                                     " written in Python on local machine.")
    parser.add_argument("file", metavar="FILE", type=str,
                        help="Lambda function file name")
    parser.add_argument("event", metavar="EVENT", type=str,
                        help="Event data file name.")
    parser.add_argument("-l", "--library", metavar="LIBRARY_PATH",
                        type=str, help="Path of 3rd party libraries.")
    parser.add_argument("-f", "--function", metavar="HANDLER_FUNCTION",
                        type=str, default="handler",
                        help="Lambda function handler name. \
Default: \"handler\".")
    parser.add_argument("-t", "--timeout", metavar="TIMEOUT", type=int,
                        default=3,
                        help="Seconds until lambda function timeout. \
Default: 3")
    return parser.parse_args()

if __name__ == "__main__":
    main()
