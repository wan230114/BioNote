#!/usr/bin/env Rscript
#############################################
# @ Author: Chen Jun
# @ Author Email: 1170101471@qq.com
# @ Created Date: 2021-07-01, 17:47:59
# @ Modified By: Chen Jun
# @ Last Modified: 2021-12-25, 19:05:04
#############################################

info <- c(a = 1000, b = 100, c = 400, d = 200, e = 1230)
info <- info[order(-info)]
# info <- c(info[1:4], Others = sum(info[5:length(info)]))
names <- names(info)
names
color <- c("#000000", "#d2d2d2", "#e9e9e9", "#a3a3a2", "#ffffff")
library(plotrix)

pie3D(info,
    labels = names,
    labelcex = 1.1,
    labelrad = 1.4,
    # labelcol="red",
    # explode=0.05,
    col = color,
    theta = 1,
    radius = 1,
    start = 1.58
)
