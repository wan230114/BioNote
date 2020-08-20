# 1. R语言简介

## hello world

### 交互模式运行
```bash
$ R
> print("hello")
[1] "hello"
> print("world")
[1] "world"
```

### 脚本模式运行

将命令保存为文件test.R，文件内容：
```R
print("hello")
print("world")
```

执行：
```bash
Rscrip test.R
R -e 'source("./test.R", echo=T)'
```

## 1.1. 查看帮助文档
> 认识代码的基本方法：
> - 包含内容是什么？【打印】
> - 本质是什么？
>   - 查看类型
>   - 从哪里来？【是自带函数还是外部导入包】
> - 如何使用？
>   - 包括些什么？【有些什么方法】
>   - 能做什么？【用途及功能】

### 1.1.1. 访问帮助文档：
Accessing the help files

(Windows下打开本地帮助文档网页；Linux下直接查看文档；)  

- `?mean`  
    获得特定函数的帮助。  
    Get help of a particular function.
- `help.search('weighted mean')`  
    搜索帮助文件中的单词或短语。  
    Search the help files for a word or phrase.
- `help(package = 'dplyr')`  
    获取某个包的帮助文档。  
    Find help for a package.  

### 1.1.2. 查看对象属性
More about an object
- `str(iris)`  
    获取对象结构的摘要。  
    Get a summary of an object’s structure.
- `class(iris)`  
    查找对象所属的类。  
    Find the class an object belongs to.


### 1.1.3. 查看"package"中的所有对象【待确切补充】

```R
ls()  # 查看当前环境变量
ls("package:package")  # 查看"package"中的所有对象
```

## 1.3. 变量、赋值、对象

赋值运算符：
- `<-`，较为常用
- `=`，同上一样功能，两者等价。

## 1.4. 基本打印函数print(x)

需要注意的是，表达式的输出也会打印到标准输出（不同于Python）
```R
name = c("li", "shi", "wu", "zhang", "feng")
name         # [1] "li"    "shi"   "wu"    "zhang" "feng"
print(name)  # [1] "li"    "shi"   "wu"    "zhang" "feng"
```


## 1.5. 基本数据类型

常见的数据结构
- 向量 c() # 一维
- 矩阵 matrix() # 二维
- 数组 array() # 多维
- 因子 factor()
- 列表 list()
- 数据框 data.frame()

常见的数据类型
- integer 整型
- character 字符型
- numeric 数值型（double）
- logical 逻辑型
- NULL
- NA missing value

