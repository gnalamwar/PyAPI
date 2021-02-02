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


#for key in rooms.values():
#    print(key)
#
#directions= []
#  for x in rooms[currentRoom].keys():
#      if x != "item":
#          directions.append(x)
#  print("You can go", ", ".join(directions))


while True:
    roomselected = input("Select a room above : ")
    print(roomselected )

    if roomselected in rooms():
         directionlist = []
         for x in rooms[roomselected].keys(): 
            if x != 'item':
              directionlist.append(x)
         print("You can go: ", directionlist)
         print("room found")
    else:
        print("room not found")
        break
