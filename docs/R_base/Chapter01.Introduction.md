# 1. R语言简介


---
## 1.1. hello world

### 1.1.1. 交互模式运行

```text
$ R
> print("hello")
[1] "hello"
> print("world")
[1] "world"
```

ps: radian 是使用Python开发的R交互模式客户端，强烈推荐使用。


### 1.1.2. 脚本模式运行

将命令保存为文件test.R, 执行：
```bash
echo 'print("hello world")' >test.R

# 1) Rscrip程序
Rscrip test.R

# 2) source函数
R -e 'source("./test.R", echo=T)'

# 3) 从标准输入读取执行（通过 < ）【推荐使用该方式，语法简洁】
R --no-save < test.R

# 4) 从标准输入读取执行（通过 | 管道）
cat test.R|R --no-save

```

对于rmd文件可执行：

```bash
R -e "rmarkdown::render('script.Rmd',output_file='output.html')"
```


---
## 1.2. R 的基本构成

表达式 --> 语句 --> 语句块 --> 函数（方法） --> 包


---
## 1.3. R 中数据存储、运算与基本交互

### 1.3.1. 基本数据类型及表示

常见的数据结构
- 向量 `c()`  ***一维***
- 矩阵 `matrix()`  ***二维***
- 数组 `array()`  ***多维***
- 因子 `factor()`
- 列表 `list()`
- 数据框 `data.frame()`

常见的数据类型
- integer 整型
- numeric 数值型（double）
- character 字符型
- logical 逻辑型
- NULL
- NA missing value


### 1.3.2. 基本数据运算

### 1.3.3. 基本数据“输入”、“输出”

#### 1.3.3.1. 基本输出之打印函数print(x)

需要注意的是，表达式的输出也会打印到标准输出（不同于Python）
```R
name = c("li", "shi", "wu", "zhang", "feng")
name         # [1] "li"    "shi"   "wu"    "zhang" "feng"
print(name)  # [1] "li"    "shi"   "wu"    "zhang" "feng"
```

#### 1.3.3.2. 基本输入之文件外参数传递

test.R
```R
# 所有参数模式
args <- commandArgs()
print("args <- commandArgs()")
print(args)

# 纯净参数模式
args <- commandArgs(T)  # 等效于 args <- commandArgs(trailingOnly = TRUE)
print("args <- commandArgs(T)")
print(args)
```

Shell执行：

```bash
# 只打印结果
Rscript test.R 1 2 3
# 执行并打印交互模式效果
R --no-save --args 1 2 3 <test.R
cat test.R|R --no-save --args 1 2 3
R -e 'source("./test.R", echo=T)' --args 1 2 3
```

## 1.4. 对象、变量、赋值的基本概念

赋值运算符：
- `<-`，较为常用
- `=`，同上一样功能，两者等价。

R语言也是一门面向对象的编程语言，对象绑定过程与Python类似，此处不作过多伸展。

如何多重赋值？【待补充】

示例：
```R
> a <- 'apple'
> a
[1] 'apple'
```


## 1.5. 查看帮助文档
> 认识代码的基本方法：
> - 包含内容是什么？【打印】
> - 本质是什么？
>   - 查看类型
>   - 从哪里来？【是自带函数还是外部导入包】
> - 如何使用？
>   - 包括些什么？【有些什么方法】
>   - 能做什么？【用途及功能】

### 1.5.1. 访问帮助文档：

(Windows下打开本地帮助文档网页；Linux下直接查看文档；)  

```R
?mean  # 获得特定函数的帮助。  
help.search('weighted mean')  # 搜索帮助文件中的单词或短语。  
help(package = 'dplyr')  # 获取某个包的帮助文档。  
```

### 1.5.2. 查看对象属性

```R
str(iris)    # 获取对象结构的摘要。
class(iris)  # 查找对象所属的类。
```


### 1.5.3. 查看和管理环境变量

```R
ls()  # 查看当前环境变量
ls("package:package")  # 查看"package"中的所有对象
rm(x)  # 从环境中删除x。
rm(list = ls())  # 从环境中删除所有变量。
```

您可以使用RStudio中的环境面板浏览环境中的变量。

