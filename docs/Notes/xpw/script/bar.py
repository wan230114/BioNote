#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-04-08, 10:02:07
# @ Modified By: Chen Jun
# @ Last Modified: 2021-04-08, 10:02:15
#############################################


import matplotlib.pyplot as plt
from matplotlib import rc
import pandas as pd

# %%
# 数据导入
try:
    df = pd.read_table("./out_rmats/res_summary.txt", index_col=0)
    # df = df.loc[df.index[::-1]]
    df = df.loc[[
        "MXE",
        "RI",
        "SE",
        "A5SS",
        "A3SS",
    ][::-1]]
    df
    x = df.index
    y = df["SignificantEventsJC"].to_list()
except Exception:
    x = ['A3SS', 'A5SS', 'SE', 'RI', 'MXE']
    y = [687, 486, 4829, 904, 464]

plt.figure(figsize=(4.3, 6.2))
ax = plt.gca()  # 获得坐标轴的句柄
ax.spines['bottom'].set_linewidth(0)  # 设置底部坐标轴的粗细
ax.spines['left'].set_linewidth(5)  # 设置左边坐标轴的粗细
ax.spines['right'].set_linewidth(0)  # 设置右边坐标轴的粗细
ax.spines['top'].set_linewidth(5)  # 设置上部坐标轴的粗细


# creating the bar plot
plt.barh(x, y, color=["#b8d9b3", "#f3c8ad",
                      "#e58b6f", "#c9cacc", "#e28488"],
         height=0.5)

plt

# want a more natural, table-like display
ax.invert_yaxis()
ax.xaxis.tick_top()
ax.tick_params(direction='out', length=6, width=4, colors='black',
               grid_color='black', grid_alpha=0.5,
               labelsize=22)
# plt.tick_params(labelsize=23)
# plt.rcParams.update({'font.weight': 'bold'})
rc('font',
   #    weight="bold",
   #    family='黑体'
   )
# fontproperties = {'family': 'sans-serif',
#                   'sans-serif': ['Helvetica'],
#                   'weight': fontweight,
#                   'size': fontsize}

# plt.xlabel("EventType")
# plt.ylabel("SignificantEventsJC")
plt.show()
