#!/usr/bin/python
import json

def main():

    with open("challenge2.json", "r") as data:
        datastring = data.read()

    datadecoded = json.loads(datastring)
    print(datadecoded)
    print(type(datadecoded))

    # 
    for person in datadecoded:
        print(person["name"])
        print(person["email"])
        print(person["phone"])
        print(person["address"])
        friendslist = {}
        for friend in person["friends]"["name"]
            friendlist.append(friend)
        print(friendslist)

if __name__ == "__main__":
    main()
