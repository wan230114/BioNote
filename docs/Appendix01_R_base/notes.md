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



# read文件的一些细节

```R
read.table(inmat, header = T, stringsAsFactors = F, sep = "\t", row.names = 1)

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


## 数据分组统计

```R
# 构造一个很简单的数据，一组人的性别、年龄和身高，可以用aggregate函数来求不同性别的平均年龄和身高
x <- data.frame(
  name=c("张三","李四","王五","赵六"),
  sex=c("M","M","F","F"),
  age=c(20,40,22,30),
  height=c(166,170,150,155)
)
aggregate(x[,3:4], by=list(sex=x$sex), FUN=mean)
```

## 文件名去除后缀操作

```R
finame <- "1.txt.txt"
finame_tmp <- unlist(strsplit(finame, ".", fixed = TRUE))
if (length(finame_tmp) > 1) {
    a <- paste(finame_tmp[1:length(finame_tmp) - 1], sep = ".", collapse = ".")
} else {
    a <- finame
}
a
```

## 表的查找

查看是否在一个向量内

```R
c("19", "24") %in% c("19", "18", "17")
# [1]  TRUE FALSE
```

## 如何做到批量替换

```R
df <- data.frame(row.names=c("3", "4", "5"), v=c("a", "b", "c"))
df

# select <- df$v %in% inlist
# select
# # c(2, 1) 变为 c("b", "a")
# df[select,]

df[c("5","4"),]

```


# 绘图相关

## 如何设置图片自动调整大小

使用ggplot2, `units = "in"`

```R
require(ggplot2)

# Bogus data
x <- rnorm(10000)
y <- as.factor(round(rnorm(10000, mean = 10, sd = 2), 0))
df <- data.frame(vals = x, factors = y)

myplot <- ggplot(data = df, aes(x = vals)) +
    geom_density() +
    facet_wrap(~factors)

ggsave(filename = "foo.pdf", plot = myplot, width = 8, height = 10, units = "in")
```


## 排序操作

```R
order(c(140,101,111))  # [1] 2 3 1
df <- data.frame(k=c("a", "b", "c"), v=c(1, 2, 3))
df

```

## 挑选以什么开头的数据

```R
grepl("A_", c("A_1", "A_2", "B_1", "C_1"))
# [1]  TRUE  TRUE FALSE FALSE
```

## apply / map /

apply: 将一行或一列传入函数计算
lapply: 将一行和一列传入函数计算

```R
m1 <- matrix(C<-(1:6),nrow=2, ncol=3)
m1
#      [,1] [,2] [,3]
# [1,]    1    3    5
# [2,]    2    4    6
sum_negative <- function(x) {return(-sum(x))}
apply(m1, 1, sum_negative)  # 传行 [1]  -9 -12
apply(m1, 2, sum_negative)  # 传列 [1]  -3  -7 -11
apply(m1, c(1, 2), sum_negative)
#      [,1] [,2] [,3]
# [1,]   -1   -3   -5
# [2,]   -2   -4   -6
# 以下计算类似于apply(m1, c(1, 2), sum_negative)
lapply(m1, sum_negative)  # 输出格式为列表
sapply(m1, sum_negative)  # 输出格式为向量

apply(m1, 2, function(x) { cat(x[1], x[2], " --- ", x+1,  "---\n"); return(x+1) })
# apply注意事项，使用该方法得到的矩阵被转置了


data(iris)
head(iris, 2)
#   Sepal.Length Sepal.Width Petal.Length Petal.Width Species
# 1          5.1         3.5          1.4         0.2  setosa
# 2          4.9         3.0          1.4         0.2  setosa
tapply(iris$Sepal.Length, iris$Species, sum)
# apply()家族还有多个衍生函数，包括vapply、mapply、rapply等...

```