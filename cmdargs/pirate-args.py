#!/usr/bin/env python3
import sys

args = sys.argv

if not args: args = []
if not args[1]: args[1] = "Username"
if not args[2]: args[2] = "Passwd"
if not args[3]: args[3] = "IP Address"
if not args[4]: args[4] = "Gateway"

print("Username: " + args[1])
print("Password: " + args[2])
print("IP Address: " + args[3])
print("Gateway: " + args[4])
print("Oh by the way, your script is named:", args[0])

