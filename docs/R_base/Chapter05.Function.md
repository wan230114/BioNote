常用函数

```R
nrow(df)  # 统计行数
```


# 高阶函数

```R
# 将字符串当做语句或表达式执行
eval(parse(text = "print(123)"))
eval(parse(text = "a = 1"))
```

```R
f <- function(x, ...){ print(ls()) }
f(1, y=2)
# ???
```

# 管道用法

```R
# 将左边数据传递给右边函数
c(1, 2, 3) %>% max
```