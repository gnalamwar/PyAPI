#!/usr/bin/python3
import argparse, socket
import requests, pprint
from datetime import datetime
def main():
    global helmetson
    helmetson = requests.get(args.url).json()
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Display API JSON with pretty print')
    parser.add_argument('--url', default="http://api.open-notify.org/astros.json", help='base URL to access')
    #parser.add_argument('-t', metavar='PROTOCOL', type=str, default="UDP", help="this is the protocol that will be used (default UDP)")
    args = parser.parse_args()
    main()
    pprint.pprint(helmetson)
