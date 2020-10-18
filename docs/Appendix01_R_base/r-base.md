# 入门
## 访问帮助文档



## 工作路径的获取与设定

`getwd()`
> Find the current working directory (where inputs are found and outputs are sent).

`setwd('C://file/path')`
> 更改当前工作目录。使用RStudio中的项目将工作目录设置为您正在使用的文件夹。

## 基本数据类型
Types

在R中的常见数据类型之间进行转换。始终可以从表中的较高值转换为较低值。
Converting between common data types in R. Can always go from a higher value in the table to a lower value.  

|     Types      |              Literal              |                                  summary                                  |
| -------------- | --------------------------------- | ------------------------------------------------------------------------- |
| `as.logical`   | `TRUE, FALSE, TRUE`               | Boolean values (TRUE or FALSE).                                           |
| `as.numeric`   | `1, 0, 1`                         | Integers or floating point numbers.                                       |
| `as.character` | `'1', '0', '1'`                   | Character strings. Generally preferred to factors.                        |
| `as.factor`    | `'1', '0', '1', levels: '1', '0'` | Character strings with preset levels. Needed for some statistical models. |

---
示例：
```R
TRUE
1
"1"
factor(c("A","B"),levels=c("A","B","C","D","E"))
factor(c("A","B","F"),levels=c("A","B","C","D","E"))
```

结果：
```
[1] TRUE
[1] 1
[1] "1"
[1] A B
Levels: A B C D E
[1] A    B    <NA>
Levels: A B C D E
```

## 基本数据结构
Data Structure

### 向量
Vectors

#### 创建向量
Creating Vectors

|      Statement      |   result    |           summary           |
| ------------------- | ----------- | --------------------------- |
| `c(2, 4, 6)`        | `2 4 6`       | Join elements into a vector |
| `2:6`               | `2 3 4 5 6`   | An integer sequence         |
| `seq(2, 3, by=0.5)` | `2.0 2.5 3.0` | A complex sequence          |
| `rep(1:2, times=3)` | `1 2 1 2 1 2` | Repeat a vector             |
| `rep(1:2, each=3)`  | `1 1 1 2 2 2` | Repeat elements of a vector |

#### 向量相关的函数
Vector Functions

| Statement |        summary        |
| --------- | --------------------- |
| `sort(x)`   | Return x sorted.      |
| `rev(x)`    | Return x reversed.    |
| `table(x)`  | See counts of values. |
| `unique(x)` | See unique values.    |

#### 向量的索引和切片
Selecting Vector Elements

注意：向量索引是从1开始计算的，非0。
Note: The vector index is calculated from 1, not 0.  


By Position
| Statement |             summary              |
| --------- | -------------------------------- |
| `x[4]`      | The fourth element.              |
| `x[-4]`     | All but the fourth.              |
| `x[2:4]`    | Elements two to four.            |
| `x[-(2:4)]` | All elements except two to four. |

By Value

|       Statement        |             summary             |
| ---------------------- | ------------------------------- |
| `x[c(1, 5)]`           | Elements one and five.          |
| `x[x == 10]`           | Elements which are equal to 10. |
| `x[x < 0]`             | All elements less than zero.    |
| `x[x %in% c(1, 2, 5)]` | Elements in the set 1, 2, 5.    |

Named Vectors

|  Statement   |          summary           |
| ------------ | -------------------------- |
| `x['apple']` | Element with name 'apple'. |


Example:
```R
> x <- seq(0,100,10)
> x
 [1]   0  10  20  30  40  50  60  70  80  90 100

> x[1]
[1] 0

> x[c(1,5)]
[1]  0 40

> x<=30
 [1]  TRUE  TRUE  TRUE  TRUE FALSE FALSE FALSE FALSE FALSE FALSE FALSE

> x[x<=30]
[1]  0 10 20 30
```

### Matrices
- Create
  - `m <- matrix(x, nrow = 3, ncol = 3)`: Create a matrix from x.
- Select
  - `m[2, ]`: Select a row.
  - `m[ , 1]`: Select a column.
  - `m[2, 3]`: Select an element.
- Method
  - `t(m)`: Transpose
  - `m %*% n`: Matrix Multiplication 【待吸收？怎么计算的】
  - `solve(m, n)`: Find x in: m * x = n 【待吸收？怎么用的】

Example:
```R
> 1:9
[1] 1 2 3 4 5 6 7 8 9

> m <- matrix(1:9, nrow = 3, ncol = 3)

> m
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9

```
```R
> m <- matrix(1:9, nrow = 3, ncol = 3)
> m
     [,1] [,2] [,3]
[1,]    1    4    7
[2,]    2    5    8
[3,]    3    6    9
> n = m+1
> n
     [,1] [,2] [,3]
[1,]    2    5    8
[2,]    3    6    9
[3,]    4    7   10
> m %*% n
     [,1] [,2] [,3]
[1,]   42   78  114
[2,]   51   96  141
[3,]   60  114  168
```

### Lists

`l <- list(x = 1:5, y = c('a', 'b'))`: A list is a collection of elements which can be of different types.

列表是可以是不同类型的元素的集合。

- `l[[2]]`: Second element of l.
- `l[1]`: New list with only the first element.
- `l$x`: Element named x.
- `l['y']`: New list with only element named y.

### Data Frames

`df <- data.frame(x = 1:3, y = c('a', 'b', 'c'))`: A special case of a list where all elements are the same length.

列表的一种特殊情况，其中所有元素的长度都相同。

|  x  |  y  |
| --- | --- |
| 1   | a   |
| 2   | b   |
| 3   | c   |


Example:
```R
> df <- data.frame(x = 1:3, y = c('a', 'b', 'c'))

> df
  x y
1 1 a
2 2 b
3 3 c

> df$x
[1] 1 2 3

> df[[2]]
[1] a b c
Levels: a b c
```

#### Understanding a data frame

Method:
- `View(df)`: See the full data frame.
- `head(df)`: See the first 6 rows.

#### Matrix subsetting

```R

df[ , 2]
df[2, ]
df[2, 2]

```
## Programming

### For Loop

```R
for (variable in sequence){
    Do something
}
```

Example:
```R
for (i in 1:4){
j <- i + 10
print(j)
}
```

### If Statements

```R
if (condition){
    Do something
} else {
    Do something different
}
```

Example:
```R
i <- 10
if (i > 3){
    print('Yes')
} else {
    print('No')
}
```

### While Loop

```R
while (condition){
    Do something
}
```

Example:
```R
i = 0
while (i < 5){
    print(i)
    i <- i + 1
}
```

## Functions
### Custom
```R
function_name <- function(var){
    Do something
    return(new_variable)
}
```

Example:
```R
square <- function(x){
    squared <- x*x
    return(squared)
}
square(9)
```

### Maths Functions

|   Statements   |             summary             |
| -------------- | ------------------------------- |
| `log(x)`       | Natural log.                    |
| `exp(x)`       | Exponential.                    |
| `max(x)`       | Largest element.                |
| `min(x)`       | Smallest element.               |
| `round(x, n)`  | Round to n decimal places.      |
| `signif(x, n)` | Round to n significant figures. |
| `cor(x, y)`    | Correlation.                    |
| `sum(x)`       | Sum.                            |
| `mean(x)`      | Mean.                           |
| `median(x)`    | Median.                         |
| `quantile(x)`  | Percentage quantiles.           |
| `rank(x)`      | Rank of elements.               |
| `var(x)`       | The variance.                   |
| `sd(x)`        | The standard deviation.         |


## Reading and Writing Data
—— Also see the readr package.

|             Input              |              Ouput              |                                          Description                                           |
| ------------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------------- |
| `df <- read.table('file.txt')` | `write.table(df, 'file.txt')`   | Read and write a delimited text file.                                                          |
| `df <- read.csv('file.csv')`   | `write.csv(df, 'file.csv')`     | Read and write a comma separated value file. This is a special case of read.table/write.table. |
| `load('file.RData')`           | `save(df, file = 'file.Rdata')` | Read and write an R data file, a file type special for R.                                      |

## Conditions

| Statements |         summary          |
| ---------- | ------------------------ |
| a == b     | Are equal                |
| a > b      | Greater than             |
| a >= b     | Greater than or equal to |
| a != b     | Not equal                |
| a < b      | Less than                |
| a <= b     | Less than or equal to    |
| is.na(a)   | Is missing               |
| is.null(a) | Is null                  |

