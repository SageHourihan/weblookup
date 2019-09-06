'''
This program is an update to websiteLookup.py using argparse

1xx (Informational): The request was received, continuing process
2xx (Successful): The request was successfully received, understood and accepted
3xx (Redirection): Further action needs to be taken in order to complete the request
4xx (Client Error): The request contains bad syntax or cannot be fulfilled
5xx (Server Error): The server failed to fulfill an apparently valid request

Developed by: Sage Hourihan 
Date: 7/12/19
'''
# impoting modules
import argparse
import webbrowser
from urllib.request import urlopen

def lookup():

    # creating parser and adding arguments 
    parser = argparse.ArgumentParser(description='gets website status code')
    parser.add_argument('-w', '--website', help="enter website in command line")
    parser.add_argument('-f', '--file', help="enter file name. file must be in same folder as script")
    parser.add_argument('-v', '--verbose', action="store_true", help="prints output to comand line")
    args = parser.parse_args()

    # if statements and flags 

    if args.verbose:

        if args.website:
            website = [args.website]
            for x in website:
                try:
                    w = urlopen(x)
                    wc = w.getcode()
                    res = "Website: " + x + " Status code: " + str(wc)
                    f = open('statusCodes.txt', 'a+')
                    f.write(res + "\n")
                    f.close()
                    print(res)
                except Exception as e:
                    print(x, ":", e)
                    continue
        if args.file:
            file = args.file
            fhand = open(file, "r")
            contents = fhand.read()
            strng = contents.split(",")

            for x in strng:
                try:
                    w = urlopen(x)
                    wc = w.getcode()
                    res = "Website: " + x + " Status code: " + str(wc)
                    f = open('statusCodes.txt', 'a+')
                    f.write(res + "\n")
                    f.close()
                    print(res)
                except Exception as e:
                    print(x, ":", e)
                    continue
    else:
        if args.website:
            website = [args.website]
            for x in website:
                try:
                    w = urlopen(x)
                    wc = w.getcode()
                    res = "Website: " + x + " Status code: " + str(wc)
                    f = open('statusCodes.txt', 'a+')
                    f.write(res + "\n")
                    f.close()
                except Exception as e:
                    print(x, ":", e)
                    continue
        if args.file:
            file = args.file
            fhand = open(file, "r")
            contents = fhand.read()
            strng = contents.split(",")

            for x in strng:
                try:
                    w = urlopen(x)
                    wc = w.getcode()
                    res = "Website: " + x + " Status code: " + str(wc)
                    f = open('codes.txt', 'a+')
                    f.write(res + "\n")
                    f.close()
                except Exception as e:
                    print(x, ":", e)
                    continue