# micRNA分析简介

## miRNA的基本概念
miRNA (microRNA)是一组由基因组编码的长度约 20～23 个核苷酸的非编码 RNA，通过和靶基因 mRNA 碱基配对引导沉默复合体 (RISC) 降解 mRNA 或阻碍其翻译。在 miRNA 公共数据库 miRBase (http://www.mirbase.org/)中已经有 1W 多条来自不同物种的 miRNA 序列 [^1]。

[^1]: ——参考：你问我答 | miRNA的5p和3p  
https://www.sohu.com/a/226493148_464200

## 研究micRNA的意义：
- 有研究表明，micRNA的差异表达与某些癌症的发生有关，可以作为标志物检测。

## miRNA命名规则

物种-microRNA类别-序号

命名包含三部分内容，即物种，microRNA类别，序号。三者间用短线连接。
1. 物种一般用三个小写字母表示，如hsa,mmu和rno分别代表人，小鼠和大鼠。
2. MicroRNA类别 是指所命名的microRNA是pre-miRNA还是mature miRNA。
   - pre-miRNA 用 mir 表示，
   - mature miRNA 用 miR 表示。
3. 序号为一阿拉伯数字，代表microRNA发现的先后。一般而言，数字越小，发现越早。

示例：
- hsa-mir-7-1, hsa-mir-7-2, hsa-mir-7-3

---
注：
- 有些pre-miRNA可以产生两个mature miRNA。对应pre-miRNA茎环结构5' 和3' 序
列的mature miRNA分别加后缀-5p和-3p以示区分，如hsa-miR-769-5p和hsa-miR-
769-3p。

## miRNA的产生过程

那它是怎么来的呢？ [^1]

是由约 70 个碱基大小形成发夹结构的单链 RNA 前体 （pre-miRNA），经过 Dicer 酶酶切加工后，成为长约 20~24nt 的成熟 miRNA，如下图所示：  
![图 1](img/miRNA_20200528_11_46_38.png)  

### 3p还是5p，有必要区分吗？

有的 miRNA 前体两个臂分别产生一条有功能的成熟 miRNA，他们分别靶向不同的位点。这时候就要来进行区分了，一般以 “-5p” 和“-3p”分别命名。如 hsa-miR-21-5p 和 hsa-miR-21-3p，分别表明从 hsa-mir-21 前体的 5’端臂和 3’端臂加工而来的。表达水平较高的 miRNA 后面不加任何符号，而表达水平较低的 miRNA 后面加上 * 号，如 hsa-miR-21*, 有时带 “*” 的 miRNA 就根本不出现。

而发夹状结构的 miRNA 前体转录本以 “mir” 命名，其编号以 “MI” 编号，如人的 miRNA 21 的前体 ID 为 hsa-mir-21，Accession 为 MI0000077。如下图所示。

### 3p/5p 功能不一样

看到发表在19 July 2019的文章Strand-specific miR-28-3p and miR-28-5p have differential effects on nasopharyngeal cancer cells proliferation, apoptosis, migration and invasion，全文提供实验验证了miR-28-3p and miR-28-5p的生物学功能不一样。

但是我们作为数据分析人员，很难有这么复杂的背景知识，有时候仅仅是把表达矩阵给过滤，大家都懂的过滤操作。

In some cases, two mature miRNAs can be excised from the same stem-loop pre-miRNA

These "5p" and "3p" miRNAs are biologically different in terms of stability and functionality. In humans, two mature miRNAs, miR-28-3p and miR-28-5p, are derived from 3′ and 5′ ends of pre-miR-28, respectively. miR-28-3p and miR-28-5p targets several cancer-related genes and is hence involved in cell proliferation, migration, invasion and epithelial–mesenchymal transition (EMT)

作者：生信技能树
链接：https://www.jianshu.com/p/e1686a147ea9
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## miRNA数据库

如何查miR-224的序列,首先要用到miRbase这个数据库(http://www.mirbase.org/),mirbase数据库是做miRNA研究最“经典”的数据库 [^2]。

[^2]: 3p还是5p，有必要区分吗？  
http://www.360doc.com/content/18/0312/22/46316053_736493196.shtml

# 分析流程
上游：
> fastq --> bam --> all_id  
> 关键点在于GTF（hisat2要用短的仅几十bp的miRNA的gtf，不能用mRNA；bomwa比对也要用到；）  

下游：
> 联合分析，从两个样本里面进行联合分析miRNA, mRNA, 取差异还是交集？  


micRNA分析流程：
- miRNA数据下载
- miRNA数据整理
- miRNA差异分析、热图、火山图
- miRNA转录因子预测
- miRNA的GO富集分析
- miRNA靶基因预测
- mRNA数据下载
- mRNA数据整理
- mRNA差异分析、热图、火山图
- miRNA靶基因和差异mRNA取交集
- 调控网络构建
- GO和KEGG富集分析

---
【我的疑惑？】
- 我在网上看到有的分析方法需要用到bowtie进行比对等操作，为什么这个流程不需要？
- 

## miRNA芯片数据下载
NCBI-GEO

Home - GEO - NCBI  
https://www.ncbi.nlm.nih.gov/geo/



## miRNA数据整理

Id转换

数据分组


## miRNA差异分析、热图、火山图

miRNA差异分析

miRNA热图

miRNA火山图

miRNA的TF富集分析

## miRNA转录因子预测


## miRNA的GO富集分析

miRNA的GO富集分析

## miRNA靶基因预测

miRNA靶基因预测

## mRNA数据下载

mRNA芯片数据下载

## mRNA数据整理


## mRNA差异分析、热图、火山图


## miRNA靶基因和差异mRNA取交集

miRNA靶基因和差异mRNA取交集

调控网络

## 调控网络构建


## GO和KEGG富集分析

# 附：学习资料

google学术关键词：

mirna analysis

## 论文1
【待吸收】
Genome-Wide miRNA Analysis Identifies miR-188-3p as a Novel Prognostic Marker and Molecular Factor Involved in Colorectal Carcinogenesis | Clinical Cancer Research  
https://clincancerres.aacrjournals.org/content/23/5/1323.full

## 论文2
内容提取
- 新型miRNA预测的工具
  - miRDeep和miRDeep star [6]

compilation of Web-based research tools for miRNA analysis | Briefings in Functional Genomics | Oxford Academic  
https://academic.oup.com/bfg/article/16/5/249/3053315

