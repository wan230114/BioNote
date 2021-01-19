#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-01-13, 19:00:59
# @ Modified By: Chen Jun
# @ Last Modified: 2021-01-17, 18:24:05
#############################################

# %%

from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_table("./out.map.heat.txt", index_col=0)
df
# %%
xLabel = df.columns
yLabel = df.index

# df.iloc[:, 1].value_counts()[1] * 1
# df.iloc[:, 1].value_counts()[2] * 2

# df.apply(lambda x: x.value_counts()[2])
x1_dt, x2_dt = [], []
y1_dt, y2_dt = [], []

for x in df:
    x1_dt.append(sum(df[x] == 1))
    x2_dt.append(sum(df[x] == 2)*2)
for x in df.index:
    y1_dt.append(sum(df.loc[x] == 1))
    y2_dt.append(sum(df.loc[x] == 2)*2)

print(x1_dt, x2_dt)
print(y1_dt, y2_dt)

# %%
# # %%
# # 数据准备
# # define the x and y axis of the hotmap
# xLabel = ['Tom', 'Dick', 'Harry', 'Slim', 'Jim',
#           "Jeson", "God", "Herry", "Bom", "Tidy"]
# yLabel = ["G%s" % i for i in range(len(xLabel))]

# # prepaer the data, generate the two-dimension data
# data = np.zeros((len(xLabel), len(yLabel)))
# data[[5, 2, 3, 2], [1, 3, 4, 4]] = 1
# df = pd.DataFrame(data, columns=xLabel, index=yLabel)
# # y_dt = x_dt = np.arange(.5, len(xLabel))
# x_dt = df.sum(axis=0)
# y_dt = df.sum(axis=1)


#################### plot main ####################
# definitions for the axes
left, width = 0.1, 0.65
bottom, height = 0.1, 0.65
spacing = 0.005

rect_scatter = [left, bottom, width, height]
rect_histx = [left, bottom + height + spacing, width, 0.2]
rect_histy = [left + width + spacing, bottom, 0.2, height]

# start with a square Figure
# plt.ion()  # 开启实时画图功能
fig = plt.figure(figsize=(8, 8))

ax = fig.add_axes(rect_scatter)

# the scatter plot:
im = ax.imshow(data,
               interpolation='none',
               vmin=0,
               vmax=1,
               aspect='equal',
               cmap=ListedColormap(
                   ["white", "#285942"]
               ))


x_pos = np.arange(0, len(xLabel), 1)
y_pos = np.arange(0, len(yLabel), 1)

ax = plt.gca()
# Major ticks
ax.set_xticks(x_pos)
ax.set_yticks(y_pos)

# Labels for major ticks
ax.set_xticklabels(xLabel)
ax.set_yticklabels(yLabel)

# Minor ticks
ax.set_xticks(np.arange(-.5, 10, 1), minor=True)
ax.set_yticks(np.arange(-.5, 10, 1), minor=True)

# Gridlines based on minor ticks
ax.grid(which='minor', color='#aaaaaa', linestyle='-', linewidth=2)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax_histx = fig.add_axes(rect_histx, sharex=ax)
ax_histy = fig.add_axes(rect_histy, sharey=ax)

# use the previously defined function
# no labels
ax_histx.tick_params(axis="x", labelbottom=False)
ax_histy.tick_params(axis="y", labelleft=False)

ax_histx.bar(x_pos, x_dt, align='center')
ax_histy.barh(y_pos, y_dt, align='center')

ax_histx.set_title('Percent %', y=1.1)
ax_histy.set_title('Percent %', y=1.1)

for ax_tmp in [ax_histx, ax_histy]:
    ax_tmp.spines['top'].set_color('none')
    ax_tmp.spines['right'].set_color('none')
    ax_tmp.spines['left'].set_color('none')
    ax_tmp.spines['bottom'].set_color('none')
    # ax_tmp.spines['left'].set_position(('data', 0))
    # ax_tmp.spines['bottom'].set_position(('data', 0))

plt.show()
# %%


# plt.yticks(range(len(yLabel)), yLabel)
# ax.tick_params(top=True, bottom=False, labeltop=True, labelbottom=False)
# ax.barh(y_pos, y_dt, align='center')
# ax.set_yticklabels([yLabel])
# ax.set_yticks([])
# ax.invert_yaxis()  # labels read top-to-bottom

# now determine nice limits by hand:
# binwidth = 0.25
# xymax = max(np.max(np.abs(x)), np.max(np.abs(y)))
# lim = (int(xymax/binwidth) + 1) * binwidth
# bins = np.arange(-lim, lim + binwidth, binwidth)
# ax_histx.hist(x, bins=bins)
# ax_histy.hist(y, bins=bins, orientation='horizontal')
