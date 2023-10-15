#!/usr/bin/env python3

import sys
import requests

def sendRequest(arg):
    if(arg[1] == '--help' or arg[1] == '-h'):
        print("Usage: isdown <url>")
        print("Example: isdown imadkat.github.io")
    else:
        try:
            if("https" not in arg[1]):
                raise Exception("invalid url: provide full url with \"http(s)\" ")

            response = requests.get(arg[1]);
            if(response.status_code == 200):
                print('\x1b[6;30;42m' + "site {} is up and running".format(arg[1]) + '\x1b[0m')
            else:
                print('\x1b[0;30;41m' + "Looks like the site {} is down".format(arg[1]) + '\x1b[0m')

        except Exception as e:
                print('\x1b[0;30;41m' + e + '\x1b[0m')

# Entry Point
def main():
    argument = sys.argv

    if(len(argument) < 2):
       print('\x1b[0;30;41m' + "invalid argument: provide at least one argument" + '\x1b[0m')
    else:
       sendRequest(argument)

main();