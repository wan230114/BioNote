#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# %%
import matplotlib.pyplot as plt
import numpy as np
# from matplotlib.colors import ListedColormap

# ! 1) 生成数据
np.random.seed(100)
N = 10
M = 11
dt1 = np.random.randint(0, 180, size=(N, M))  # circle
dt2 = np.random.randint(0, 100, size=(N, M))/100  # heatmap

# ! 2) 画图前数据处理
R1 = dt1/dt1.max()/2  # 除以2得到半径大小
# lable
xlabels = ["".join(np.random.choice(list("ABCDE"), size=3)) for _ in range(M)]
ylabels = ["".join(np.random.choice(list("PQRSTUVXYZ"), size=7))
           for _ in range(N)]
# 获取x坐标集，y坐标集
x, y = np.meshgrid(np.arange(M), np.arange(N))
circles = [plt.Circle((j, i), radius=r, fill=False)
           for r, j, i in zip(R1.flat, x.flat, y.flat)]

# ! 3) 绘图
fig, ax = plt.subplots()

# heatmap
im = ax.imshow(dt2,
               # interpolation='none',
               # vmin=0,
               # vmax=1,
               # aspect='equal',
               # cmap=ListedColormap(["white", "#285942"])
               cmap="YlGn"
               )
fig.colorbar(im)
ax.set_aspect(1)  # 设置正方形

# 添加圆
for circle in circles:
    ax.add_artist(circle)

# 添加坐标轴标签
ax.set(xticks=np.arange(M), yticks=np.arange(N),
       xticklabels=xlabels, yticklabels=ylabels)
ax.set_xticks(np.arange(M+1)-0.5, minor=True)
ax.set_yticks(np.arange(N+1)-0.5, minor=True)

# 增加线条
ax.grid(which='minor')
# plt.grid(linestyle='--')
plt.show()
