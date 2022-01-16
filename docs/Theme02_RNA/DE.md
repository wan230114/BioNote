<!--
  * Author: Chen Jun
  * Author Email: 1170101471@qq.com
  * Created Date: 2021-05-28, 10:45:42
  * Modified By: Chen Jun
  * Last Modified: 2021-10-13, 11:23:10
-->

# 1. 标准化方法


## 1.1. 使用场景

- [168-跟着刘小泽一起回顾标准化方法 | BIOINFOPLANET](https://www.jieandze1314.com/post/cnposts/168/)

|                             标准化方法                             | 组内样本内比较 | 组内重复样本比较 | 组间样本间比较 | 考虑测序深度 | 考虑基因长度 | 考虑RNA组成 |
|:------------------------------------------------------------------:|:--------------:|:----------------:|:--------------:|:------------:|:------------:|:-----------:|
|        RPM/CPM (Reads/Counts per million mapped reads) /RPM        |                |        1         |                |      1       |              |             |
|                  TPM （Transcripts per million）                   |       1        |        1         |                |      1       |      1       |             |
| RPKM/FPKM (Reads/Fragments per kilo base per million mapped reads) |       1        |                  |                |      1       |      1       |             |
|                     DESeq2’s median of ratios                      |                |        1         |       1        |      1       |              |      1      |
|               EdgeR’s trimmed mean of M values (TMM)               |       1        |        1         |       1        |      1       |      1       |      1      |

表头详细解读：（假设测序获得4个样 A1, A2, B1, B2 。分组为 A组:A1, A2; B组: B1, B2）
- 组内样本内比较: 组内样本的某个单个测序数据的基因间比较。如A1内某几个基因比较。
- 组内重复样本比较: 组内样本间重复数据比较，评价重复性好坏方法。如A1和A2相比如何。
- 组间样本间比较: 差异分析，组间比较。如 (A1 A2) vs (B1 B2)


补充说明
- 计算TPM、FPKM的一个原因是：比较一个样本内的两个基因时，担心基因长度会造成影响。
- EdgeR应该是考虑问题最多的标准化方法

问题1： 为什么TPM和RPKM都是考虑了测序深度和基因长度，但RPKM却不能进行组内重复样本间比较呢？
- 这是因为RPKM或者RPKM算出来的标准化后的数值和TPM不同：每个样本中的TPM的总和都是一样的，而FPKM则不相等【先看这篇： 标准化进行时】：The total number of RPKM/FPKM normalized counts for each sample will be different.
- 总和不同当然不能直接进行比较了

问题2： 10X单细胞数据中的count需要计算TPM、FPKM等吗？
- 答案是不需要：https://kb.10xgenomics.com/hc/en-us/articles/115003684783-How-to-calculate-TPM-RPKM-or-FPKM-instead-of-counts-


---
## 1.2. 计算公式

DESeq2
- [Count normalization with DESeq2 使用 DESeq2 进行计数标准化](https://hbctraining.github.io/DGE_workshop/lessons/02_DGE_count_normalization.html)
- [Analyzing RNA-seq data with DESeq2](https://bioconductor.org/packages/release/bioc/vignettes/DESeq2/inst/doc/DESeq2.html)
  

# 2. 差异分析

- [什么，你一定要基于FPKM标准化表达矩阵做单细胞差异分析 - 云+社区 - 腾讯云](https://cloud.tencent.com/developer/article/1701617)
    - 单细胞差异分析，竟然可以分析单样本间的比较，是否可以用来做常规chip单样本的比较呢？【现在我理解了，因为它们都是10X】

