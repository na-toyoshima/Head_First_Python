#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:07:08 2020

@author: naoyatoyoshima
"""


vowels = set("aiueo")
#set関数で母音の集合を作成

word = input("単語を入力してください。母音を探します。")
#文字入力

found = vowels.intersection(set(word))
#set(word)でword内の文字列を集合に変換し、vowelとの共通文字をfoundに格納
for vowel in found:
    # foundのなかの文字を1つずつvowelに格納
    print(vowel)