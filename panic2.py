#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:31:14 2020

@author: naoyatoyoshima
"""


phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

new_phrase = "".join(plist[1:3]) #onをスライス
new_phrase = new_phrase + "".join([plist[5],plist[4],plist[7],plist[6]])
#追加する各文字（スペース、t,a,p)を選択

print(plist)
print(new_phrase)