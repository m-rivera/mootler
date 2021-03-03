#!/usr/bin/env python
"""
Read Moodle activity .csv files and output requested lists or interactive plots

"""
import sys
import argparse

def main(args):
    print(args.activity_file)
    print(args.users_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("activity_file", help="CSV file of the activities.")
    parser.add_argument("users_file", default=None, help="CSV file of users whose activity is analised. (optional)")
    parser.add_argument("-s","--string", default=None, help="Substring to be searched for.")
    parser.add_argument("-c","--context", default=None, help="Substring of the column title in which activities are searched.")

    user_input = sys.argv[1:]
    args = parser.parse_intermixed_args(user_input)
    main(args)
