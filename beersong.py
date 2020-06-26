#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:37:39 2020

@author: naoyatoyoshima
"""


word = "bottles"
for beer_num in range(99,0,-1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        if (beer_num -1) == 1:
            word = "bottle"
        print(beer_num, word, "of beer on the wall.")
    print()