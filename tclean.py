#!/usr/bin/python env
# -*- coding: utf-8 -*-
#
# Created by jim on 03/02/2021

'''

Small useful program to remove control chars from files,
commissioned by MB to help strip out unnecessary Chars

'''

# imports
import sys

# globals
prog_version = 1.0
prog_name = 'tclean.py'


def main(filenames):
    filenames.remove(prog_name)  # remove progname from list
    data = readfile(filenames[0])
    if len(filenames) > 1:  # if length of filenames is more than 1 person has supplied writefile
        writefile(filenames[1], data)
    else:  # if not output file print to screen
        for i in data:
            print(i)


def readfile(filename):  # read file and return hex cleaned data
    cleaned = []
    try:
        with open(filename, 'r') as filehandle:
            lines = filehandle.readlines()
            for line in lines:
                line = ''.join([c for c in line if 31 < ord(c) < 127])  # clean any chars out of 1Fh - 7Fh
                cleaned.append(''.join([line, '\r\n']))  # append to cleaned list and add removed carriage return
        return cleaned
    except IOError:  # error handling for permissions/missing file
        print("Cannot open {}".format(filename))


def writefile(filename, data):  # output file function
    try:
        with open(filename, 'w') as filehandle:
            filehandle.writelines(data)
    except IOError:  # error handling for permissions/missing output file
        print("Cannot open {}".format(filename))


if __name__ == '__main__':

    sys_argv = []  # list for sys argvs

    if len(sys.argv) > 1:  # if cmdline arg exist
        sys_argv = sys.argv
        main(sys_argv)
    else:
        print("No cmdline args...\nexiting...")
