/*
 * Author: Chen Jun
 * Author Email: 1170101471@qq.com
 * Created Date: 2021-05-28, 11:23:06
 * Modified By: 
 * Last Modified: 2021-05-28, 11:23:07
 */



# 1. ENSEMBL 注释ID的转换

## 1.1. 通用方法：clusterProfiler::bitr

概述： 基本很全面的数据库，但是会出现1对多的问题需要解决

问题：

- 转换时会出现1对多的情况。暂时无解

```R
library(clusterProfiler)
library(org.Mm.eg.db)
bitr(c("ENSMUSG00000047675", "ENSMUSG00000071415", "ENSMUSG00000029390"), fromType = "ENSEMBL", toType = c("SYMBOL", "ENTREZID", "GENENAME"), OrgDb = org.Mm.eg.db)
# 'select()' returned 1:many mapping between keys and columns
#              ENSEMBL       SYMBOL  ENTREZID                                GENENAME
# 1 ENSMUSG00000047675         Rps8     20116                    ribosomal protein S8
# 2 ENSMUSG00000047675      Gm15501 100040298              predicted pseudogene 15501
# 3 ENSMUSG00000071415        Rpl23     65019                   ribosomal protein L23
# 4 ENSMUSG00000071415 LOC100044627 100044627               60S ribosomal protein L23
# 5 ENSMUSG00000071415 LOC100862455 100862455               60S ribosomal protein L23
# 6 ENSMUSG00000029390        Tmed2     56334 transmembrane p24 trafficking protein 2
# 7 ENSMUSG00000029390      Gm10698 100862175                    predicted gene 10698
```


---
## 1.2. biomaRt::useEnsembl

```R
library(biomaRt)
ensembl <- useEnsembl(biomart = "genes", dataset = "hsapiens_gene_ensembl")

```

参考：
- 官方文档：[Accessing Ensembl annotation with biomaRt](https://bioconductor.org/packages/release/bioc/vignettes/biomaRt/inst/doc/accessing_ensembl.html)
- 博客：[bioMart进行基因id的转换 - sryjm - 博客园](https://www.cnblogs.com/yanjiamin/p/12054879.html)

