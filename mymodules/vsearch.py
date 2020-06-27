#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:07:08 2020

@author: naoyatoyoshima
"""


def search4vowels(phrase: str) ->set:
    """入力された単語内の母音を表示する"""
    vowels = set("aiueo")  # set関数で母音の集合を作成
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str) ->set:
    """phrase内のlettersの集合を返す"""
    return set(letters).intersection(set(phrase))
