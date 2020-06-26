#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:24:21 2020

@author: naoyatoyoshima
"""
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

plist.pop(0)
plist.pop(2)
for i in range(4):
    plist.pop()
for i in range(4):
    plist.pop(2)
plist.insert(2,"p")
plist.insert(2,"a")
plist.insert(2,"t")
plist.insert(2," ")

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)