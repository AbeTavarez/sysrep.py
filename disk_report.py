#!/usr/bin/python3

import sys

print('Running Script....')

if __name__ == '__main__':
    path = '/home'
    print('total arguments passed: ', len(sys.argv))

    # assigns the directory
    directory = sys.argv[1] if len(sys.argv) >= 2 else path
