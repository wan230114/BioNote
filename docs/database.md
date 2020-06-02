# 总结

encode

TCGA


# 先导问题
我们有些什么研究，我们为什么需要建立数据库？？

数据库建立有些什么必要性？？ 功能、标准

需要些什么类型数据库？？

## 数据库概览

基因组：
- 国际大型肿瘤基因组研究项目(如 COSMIC 、 TCGA )

蛋白结构：
- PDB ().

GEO数据库？

## 其他
### 方法
- 建立生物数据库  
  - 各种公共数据库  
  - 本地化数据库  

### 数据库检索  
- 各种数据检索工具的开发和使用  
  - Entrez检索体系  
  - BLAST检索体系  

### 生物研究与需求  
- 生物大分子序列分析  
  - 同源序列分析  
    - Homologous sequence analysis
  - 多序列对位排列  
    - Multiple sequence alignment
    - Phylogenetic analysis  
  - 基因结构、功能分析  
    - Mapping (ePCR)、Exon/Intron、Promoter、Regulatory regions……  
  - 蛋白质结构、功能分析  
    - Motif、3-D structure、post-translational modification、interactions……  

---
统计概率模型  
- Hidden Markov model（隐马尔可夫模型）  
基因识别和药物设计  
- Maximum likelihood model（最大似然模型）  
序列进化分析  
- Bayesian network（贝叶斯网络）  
调控网络构建  


# 常见参考基因组

## 参考基因组

hg19

hg38
- hg38比hg19多了一些测序位点，导致整个基因组的位置都发生了偏移。对于一些新发现的有趣的位点可能只在hg38中找得到，hg19没有相关信息，但是对于绝大多数已知的位点，两个ref里都会有相应的位置。很多软件都可以进行两个ref之间互相换算，一般来讲，所有的数据分析都用同一种ref就可以了，没有什么差别。

