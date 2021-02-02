#!/usr/bin/python
rooms = {

            'Hall' : {
                  'south' : 'Kitchen',
                  'east'  : 'Dining Room',
                  'north' : 'Family Room',
                  'item'  : 'key',
                },

            'Kitchen' : {
                  'north' : 'Hall',
                  'item'  : 'monster',
                },
            'Dining Room' : {
                  'west' : 'Hall',
                  'south': 'Garden',
                  'north' : 'Pantry',
                  'item' : 'potion',
               },
            'Garden' : {
                  'north' : 'Dining Room',
                  'item' : 'Fountain',
               },
            'Pantry' : {
                  'south' : 'Dining Room',
                  'item' : 'cookie',
            },
            'Family Room' : {
                  'south' : 'Hall',
                  'item' : 'Fire Place'
            }
         }
for room in rooms:
    print(room)
while True:
    roomselected = input("Select a room above : ")
    print(roomselected )

    if roomselected in rooms():
         directionlist = {} 
         for room in rooms: 
             if room == roomselected:
                 pass
             else: 
                 for key in rooms.keys():
                     if rooms[key] == roomselected:
                         directionlist[key].append(room[key])
         print(directionlist)
         print("room found")
    else:
        print("room not found")
        break
