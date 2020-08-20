# paste函数

```R
> paste(c("1", "2", "3"), c("a", "b", "c"),sep='-', collapse='_')
[1] "1-a_2-b_3-c"
```

# 字符串相关操作

[[R字符串] 字符串长度、分割、拼接、截取、替代、匹配和大小写替换_memory专栏-CSDN博客_r 字符串截取](https://blog.csdn.net/sinat_25873421/article/details/79234578)

```R
> a <- "test.txt"
> substr(a, 1, nchar(a) - 4)
[1] "test"
```

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
    quote = F,  # 不带引号写出
    row.names = F, 
    col.names = F
)
a <- read.csv(fi)
write.table(unique(sort(na.omit(a$SYMBOL))),
    file = paste(fi, "_SYMBOL.txt", sep = ""),
    quote = F,  # 不带引号写出
    row.names = F, 
    col.names = F
)
```

# 矩阵操作
## 如何从矩阵筛选特定的行或列

试定义如下矩阵，取出包括B和C的行，形成新的矩阵？
```
1   A   123
2   A   122
3   B   144
4   C   133
```

## 如何筛选某一列大于特定条件的值

```R
a <- as.matrix(read.table("WGY-target.bam__vs__HCT116.bam.diff.txt", header = T, stringsAsFactors = F, sep = "\t", row.names = 1))
a_select <- a[abs(as.numeric(a[, 2])) > 1, ] # 转换字符串为浮点数，比较大于1的值，筛选出其行
genelist <- rownames(a_select) # 得到genelist
genelist
write.table(genelist, file='gene.txt', quote = F, row.names = F, col.names = F)                                                                                         
```


# 异常处理

```R
for (x in c("all", "up", "down"))
{
  print(paste("\nNow -->",x))
  result = tryCatch({
    print("do somethings")
  }, warning = function(w) {
    print(paste("Waring", w))
  }, error = function(e) {
    print(paste("ERRO", e))
  })
}
```

## 环境变量相关函数

`get("str")` 获取字符串对应的环境变量

```bash
> a <- "hello"
> a
[1] "hello"
> get("a")
[1] "hello"
```