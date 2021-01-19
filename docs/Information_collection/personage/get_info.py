#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-01-03, 21:10:56
# @ Modified By: Chen Jun
# @ Last Modified: 2021-01-05, 20:48:10
#############################################

# %%
import requests
from bs4 import BeautifulSoup
import re
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'}


def re_findall(rule, doc):
    return re.compile(rule, re.DOTALL).findall(doc)


def get_html(url):
    # url = "http://www.gibh.cas.cn/rcjy/zgjgwry/index.html"
    res = requests.get(url, headers=headers)
    t = BeautifulSoup(res.content, features="html.parser")
    return t


# %%


def do(zhuye):
    # zhuye = "http://www.gibh.cas.cn/rcjy/zgjgwry/index.html"
    # zhuye = "http://www.gibh.cas.cn/rcjy/zgjgwry/index_1.html"
    t = get_html(zhuye)

    for person in t.find_all(class_="col-md-2 col-sm-3 col-xs-4"):
        url = person.find("a")["href"].replace(
            "../../", "http://www.gibh.cas.cn/")
        name = person.text
        print(f"dealing {name} ...")
        t2 = get_html(url)
        for x in t2.find_all(class_="col-md-12 tem01-people-content"):
            kw = set(re.findall(
                "(?:胚胎|肿瘤)(?:干细胞)*|干细胞|器官",
                x.text))
            if kw:
                find_res[name] = (url, kw)
            printM(f"\n\n<br><br>\n\n---\n### {name}\n")
            printM("关键词：", *kw, f"\n\n链接： [-->{name}]({url})\n\n---")
            text = re_findall("(.*)代表论著", x.text)[0].strip()
            text = re.sub("\n\n*", "  \n", text) + "  "
            text = re.sub("(\n*)(.*[:：])(  \n*)", r"\1**\2**\3", text)
            printM(text)
            out_md.flush()
        time.sleep(random.randint(100, 400)/100)


out_md = open("search.md", "w")
printM = lambda *args, **kwargs: print(*args, **kwargs, file=out_md)
find_res = {}

printM("\n\n---\n## 搜集：")
do(zhuye="http://www.gibh.cas.cn/rcjy/zgjgwry/index.html")
do(zhuye="http://www.gibh.cas.cn/rcjy/zgjgwry/index_1.html")

printM("\n\n<br><br>\n\n---\n## 总结：")
printM("| person | keyword | url |\n| - | - | - | ")

for k in find_res:
    printM("| %s | %s | [%s](%s) |" % (
        k, "、".join(sorted(find_res[k][1])),
        "-->", find_res[k][0]))

out_md.close()
