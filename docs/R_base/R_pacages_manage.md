# R包的管理及安装汇总

总结：
```R
install.packages('dplyr', repo="http://mirrors.tuna.tsinghua.edu.cn/CRAN")
# Download and install a package from CRAN.
library(dplyr)
# Load the package into the session, making all
# its functions available to use.
dplyr::select
# Use a particular function from a package.
data(iris)
# Load a built-in dataset into the environment.
```

## 1. R包的查看

```R
# 查看你已经安装了哪些包。
installed.packages()
# 查看自己的机器可以安装哪些包！
available.packages()

# 查看包版本：
# packageVersion("包名")
packageVersion("stringr")
```

导入自定义安装包环境变量：
```bash
export R_LIBS_USER=$PATH:/TJPROJ1/DENOVO/PROJECT/chenjun/R_lib/R_3.5.1
export R_LIBS=$PATH:/TJPROJ1/DENOVO/PROJECT/chenjun/R_lib/R_3.5.1
```

## 2. R包的下载源：
R中安装程序包选择国内CRAN镜像方法 – 苏岳宁博客
- http://suyuening.com/archives/1506.html

常用下载源
- http://mirrors.tuna.tsinghua.edu.cn/CRAN （常用，较稳定）
- http://mirrors.ustc.edu.cn/CRAN


## 3. R包的安装

### 3.1. install.packages()的CRAN源安装
从CRAN中安装R包

语法：
```R
########安装R包的几种方式#############

# 修改清华镜像站
site="https://mirrors.tuna.tsinghua.edu.cn/CRAN"
# 修改中科大镜像站
site2="http://mirrors.ustc.edu.cn/CRAN"
install.packages("ggplot2", repo=site)
install.packages("ggplot2", "repos" = c(site2, site))


#完全可以多个R包一起安装
ins_pac = c("DO.db", "fgsea", "qvalue", "ggforce",
            "DOSE", "ggraph", "GOSemSim", "biomaRt",
            "enrichplot", "GenomicFeatures", "gridBase",
            "rtracklayer", "TxDb.Hsapiens.UCSC.hg19.knownGene")
install.packages("ins_pac", repo=site)
```

多个源安装：【待精确补充】
```R
install.packages("包名",
                 "repos"=c(CRAN="下载源"),
                 lib='自定义安装路径')
```

- 示例
```R
install.packages("RColorBrewer", "repos" = c(CRAN="http://mirrors.ustc.edu.cn/CRAN"), lib='/home/chenjun/software/R_lib')
install.packages("MatrixEQTL", "repos" = c(CRAN="http://mirrors.ustc.edu.cn/CRAN"), lib='/TJPROJ1/DENOVO/PROJECT/chenjun/R_lib/R_3.5.1')
install.packages("MatrixEQTL", "repos" = c(CRAN="http://www.bios.unc.edu/research/genomic_software/Matrix_eQTL/"), lib='/TJPROJ1/DENOVO/PROJECT/chenjun/R_lib')
```

### 3.2. BiocInstaller::biocLite() 安装
有时候很多生物学的包无法直接安装成功，使用biocLite可安装成功。

代码总结：

通过网络导入 bioconductor 包
```R
source("https://bioconductor.org/biocLite.R")
biocLite("phangorn")
```

安装 BiocInstaller 包
```R
install.packages('BiocInstaller', repos='http://bioconductor.org/packages/3.7/bioc')
library("BiocInstaller")
options(BioC_mirror="http://mirrors.ustc.edu.cn/bioc/")
biocLite("phangorn", lib='/ifs/TJPROJ3/Plant/chenjun/software/R/R_3.6.0_package')
biocLite("synbreed", lib='/ifs/TJPROJ3/Plant/chenjun/software/R/R_3.6.0_package')
biocLite("snpStats", lib='/home/chenjun/software/R_lib')
```

- 参考 【设置 biocLite的安装源】  
    R包选择镜像以及本地安装 - wangyunpeng_bio的博客 - CSDN博客  
    https://blog.csdn.net/qq_29300341/article/details/53229215

- 安装报错解决 【google搜索关键词】
    > ERROR: dependency ‘snpStats’ is not available for package ‘LDheatmap’ * removing ‘/home/chenjun/software/R_lib/LDheatmap’  
    > ERROR: dependency ‘LDheatmap’ is not available for package ‘synbreed’ * removing ‘/home/chenjun/software/R_lib/synbreed’
    > - R：无法安装snpStats包
    > - https://www.biostars.org/p/202152/

    【解决报错： biocLite.R'】
    R语言 | 可以愉快的更新最新版R了！
    http://www.360doc.com/content/18/1012/22/47596298_794245943.shtml

### 3.3. BiocManager::install() 生物学包管理

```R
##BiocManager
chooseCRANmirror()
install.packages("BiocManager")

#安装的软件包可以更新到当前版本
BiocManager::install()

#使用version()查看Bioconductor版本
BiocManager::version()
```


### 3.4. devtools::install_github() 安装github中的包

- 准备：devtools包的安装

```R
# 判断devtools工具是否存在，选择是否需要安装，因为很大。
require(devtools)
if (!requireNamespace("devtools", quietly = TRUE))
    install.packages("devtools")
```

- 远程安装

```R
library("devtools")

# 安装phyloseq包
install_github("joey711/phyloseq")
library(phyloseq)

# 安装ggvegan包
devtools::install_github("gavinsimpson/ggvegan")
install_github("ggvegan")

# 其他
devtools::install_github("calligross/ggthemeassist")
# 安装开发版(连github不稳定有时间下载失败，多试几次可以成功)
devtools::install_github("phyloseq", build_vignettes = TRUE)
# 安装新功能最优版
devtools::install_github("phyloseq", ref = "optimization")
```

- 本地安装：
> 我们下载github上的包，可能经常性的打不开，R中无法下载，甚至手动克隆都有可能随时中断。
> 无法下载得到github包，或者无法安装后，将github包手动下载下来，解压之后定位文件夹名称后安装
```R
install.packages("C:/Users/wentao/Desktop/hrbrthemes-master/", repos = NULL, type = "source")
install.packages("C:/Users/wentao/Desktop/microbiomeutilities-master/", repos = NULL, type = "source")
library(microbiomeutilities)
```
图形化界面的本地安装操作方法：  
[零基础玩转R：如何安装已下载到本地的包](https://mp.weixin.qq.com/s/RJ4-1i8QvtpO3Ay_XWeQOg)


### 3.5. install_version()安装固定版本
```R
install_version("igraph", version = "0.6.5",
                repo="http://mirrors.tuna.tsinghua.edu.cn/CRAN/")
```


## 4. R包的载入

### 4.1. R包载入方式


```R
# 常规载入
library("包名")
require("包名")

# 通过变量指定载入
pkg <- "包名"
library(pkg, character.only=TRUE)

# 多个包一起载入
# Load packages into session
cran_packages <- c("ggplot2", "gridExtra")
bioc_packages <- c("dada2", "msa", "phyloseq")
sapply(c(cran_packages, bioc_packages), require, character.only = TRUE)

```

> **R中 library 和 require 的区别**  
> - 在一个函数中，如果一个包不存在，执行到library将会停止执行，require则会继续执行。
> - require将会根据包的存在与否返回true或者false，
> 参考：
> - [r - What is the difference between require() and library()? - Stack Overflow](https://stackoverflow.com/questions/5595512/what-is-the-difference-between-require-and-library)
> - [R中library和require的区别 - todoit - 博客园](https://www.cnblogs.com/todoit/archive/2012/10/24/2736514.html)


---
### 4.2. 查看载入的包

```R
# 查看默认载入的包
getOption("defaultPackages")  # 查看启动R时自动载入的包
# 查看R中载入的包
sessionInfo()  # 查看R中载入的包
```

### 4.3. 查看包安装目录
查看已经安装的包目录
```R
.libPaths()  # 查看包的安装目录
library()  # 查看已经安装的包目录
```
