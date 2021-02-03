#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        print(got_dj)
        #pprint.pprint(got_dj)
        for house in got_dj["allegiances"]:
            #print("Allegiance :", requests.get(house).json()["name"])
            houseresp = requests.get(house)
            house_dj = houseresp.json()
            house_name =  house_dj["name"]
            print("Allegiance :", house_name)

        for book in got_dj["books"]:
            bookresp = requests.get(book)
            book_dj = bookresp.json()
            book_name = book_dj["name"]
            print("Books :", book_name)
            # All above commands can be replace with below one liner.
            #print("Books :", requests.get(book).json()["name"])

if __name__ == "__main__":
        main()

