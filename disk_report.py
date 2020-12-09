#!/usr/bin/python3
import sys
import os
import pandas as pd

print('Running Script....')


def get_size(path):
    # accumulator
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                # recurvise call for each sub/directory
                total += get_size(entry.path)
            else:
              # get size in the total accumulator
                total += entry.stat(follow_symlinks=False).st_size
        except Exception as e:
            print('Exeption: ', e)
            total += 0
    return total


# MAIN ###################
if __name__ == '__main__':
    path = '/home'
    print('total arguments passed: ', len(sys.argv))

    # assigns the directory
    directory = sys.argv[1] if len(sys.argv) >= 2 else path

    # disk usage and directory paths
    usage = []
    paths = []

    # scan all directories and files under (directory)
    for entry in os.scandir(directory):
        # print all directories
        print(entry.path)  # gets full path entry.path
        # check if entry is a directory and ignoring symbolic links
        if (entry.is_dir(follow_symlinks=False)):
            # print(entry.path + ' is a directory')
            # print(get_size(entry.path))
            total = get_size(entry.path)
            print(total)
            paths.append(entry.path)
            usage.append(total)

        # create usage dictionary
        usage_dict = {
            'directory': paths,
            'usage': usage
        }
        # create panda's data frame
        df = pd.DataFrame(usage_dict)

        # create csv file
        print(df)
        df.to_csv('disk_usage.csv')
