#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:07:08 2020

@author: naoyatoyoshima
"""


vowels = ["a", "e", "i", "o","u"]

word = input("単語を入力してください。母音を探します。")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)