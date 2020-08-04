# 2. R中的数据结构

常见的数据结构
- 向量: c() # 一维
- 矩阵: matrix() # 二维
- 数组: array() # 多维
- 因子: factor()
- 列表: list()
- 数据框: data.frame()

## 向量

存储一维数组

### c()函数对向量的基本创建

- 创建方法：
  - `c(value1, value2, value3, ...)`
- 返回：
  - 与values相同的对象

```R
name = c("li", "shi", "wu", "zhang", "feng")
name         # [1] "li"    "shi"   "wu"    "zhang" "feng"
print(name)  # [1] "li"    "shi"   "wu"    "zhang" "feng"
typeof(name) # [1] "character"
```

注：当存在字符串类型时，将自动直接全部升级为字符串类型
```R
c(1,2,3)    # [1] 1 2 3
typeof(c(1,2,3))    # [1] "double"
c(1,2,"3")  # [1] "1" "2" "3"
typeof(c(1,2,"3"))  # [1] "character"
```

c()还可以用于拼接多个向量：
```R
> c(c(1,2,3), c(4,5,6))
[1] 1 2 3 4 5 6
```

### seq()函数创建
用法与Python的range()函数类似，不同之处在于可以使步长为非整数值

示例：
```R
seq(from=5, to=10, by=1)  # [1]  5  6  7  8  9 10
seq(5, 10, 1)   # [1]  5  6  7  8  9 10
seq(10, 5, -1)  # [1] 10  9  8  7  6  5
seq(1, 5, 0.5)  # [1] 1.0 1.5 2.0 2.5 3.0 3.5 4.0 4.5 5.0
```