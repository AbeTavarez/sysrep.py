#!/usr/bin/python3

import sys
import os

print('Running Script....')

if __name__ == '__main__':
    path = '/home'
    print('total arguments passed: ', len(sys.argv))

    # assigns the directory
    directory = sys.argv[1] if len(sys.argv) >= 2 else path

    # scan all directories and files under (directory)
    for entry in os.scandir(directory):
        # print all directories
        print(entry.path)  # gets full path entry.path
        # check if entry is a directory and ignoring symbolic links
        if (entry.is_dir(follow_symlinks=False)):
            print(entry.path + ' is a directory')
