#!/usr/bin/python3
import json

def main():
    ## Open a file. 
    with open("datacenter.json", "r") as datacenter:
        datacenterstring = datacenter.read()

    ## display our decoded string.
    print(datacenterstring)
    print(type(datacenterstring))
    print("\nThe code above is string data. Python cannot easily work with this data type.")

    ## Creaye a json string.
    datacenterdecoded = json.loads(datacenterstring)

    ## This is now dictionary
    print(type(datacenterdecoded))

    ## Display servers in the dataceneter.
    print(datacenterdecoded)

    ## Display 2nd server in a row2.
    print(datacenterdecoded["row2"][1])

    ## Wrire code to display last server in row3.
    print(datacenterdecoded['row3'][3])

if __name__ == "__main__": 
    main()
