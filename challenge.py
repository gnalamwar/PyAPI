import json

with open("challenge.json", "r") as clg:
  clgstring = clg.read()
clgstringdecode = json.loads(clgstring)
print(clgstringdecode[3]["name"])
print(clgstringdecode[3]["eyeColor"]) # eye color
print(clgstringdecode[3]["favoriteFruit"]) # favorite fruit
