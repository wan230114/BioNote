# paste函数

```R
> paste(c("1", "2", "3"), c("a", "b", "c"),sep='-', collapse='_')
[1] "1-a_2-b_3-c"
```

# 字符串相关操作

[[R字符串] 字符串长度、分割、拼接、截取、替代、匹配和大小写替换_memory专栏-CSDN博客_r 字符串截取](https://blog.csdn.net/sinat_25873421/article/details/79234578)


# 参数传递

```R
args <- commandArgs(trailingOnly = TRUE)
a <- args[1] # in.bed  a<-"HX_5637.bed"
```

# 常见操作
## 去除NA、去重、排序

```R
args <- commandArgs(trailingOnly = TRUE)
fi <- args[1]
# fi <- "GX-SiHa.peakanno.csv"
a <- read.table(fi)

write.table(unique(sort(na.omit(a$ENSEMBL))),
    file = paste(fi, "_ENSEMBL.txt", sep = ""),
    quote = F,
    row.names = F,
    col.names = F
)
```