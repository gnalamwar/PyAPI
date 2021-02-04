#!/usr/bin/env python3
vendors = ['cisco', 'juniper', 'big_ip', 'f5', 'arista', 'hp']

print("Currently the value of vendor:", vendors)

print("\nThe results of Sorted() function :", sorted(vendors))

sortedvendors = sorted(vendors)

print("Our sorted vendor list looks like this: " + str(sortedvendors))

backsortvendors = sorted(vendors, reverse = True)

print('Our Reverse Sorted vendors looks like this: ', backsortvendors)


vendorsdeux = ['CISCO', 'JUNIPER', 'cisco', 'juniper', 'BIG_IP', 'big_ip', \
'f5', 'arista', 'HP', 'F5', 'hp', 'ARISTA']

print('Our new vendordeux list looks like this: ', vendorsdeux)

print('Our sorted vendor list looks like this: ', sorted(vendorsdeux))

