#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def func():
    fileName = "hlm"
    f = open(fileName)

    reStrTitle = r'^.*(第.{1,4}回)\s+(.*)\s*$'   # 标题
    pTitle = re.compile(reStrTitle)

    reStrContent = r'^\s*(.*)\s*$'               # 内容
    pContent = re.compile(reStrContent)

    for line in f:
        mTitle = pTitle.match(line) 
        mContent = pContent.match(line) 
        if mTitle:
            print("\chapter{", end = "")
            print(mTitle.group(2), end = "")               # 标题文本
            print("}")
            continue
        if mContent:
            pass
            print(mContent.group(1))

if __name__ == '__main__':
    func()



