#!/usr/bin/python3

import sys


if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("please print an arguement for the subreddit to search")
    else:
        res = recurse(sys.argv[1])
        if res is not None:
            print(len(res))
        else:
            print("None")
