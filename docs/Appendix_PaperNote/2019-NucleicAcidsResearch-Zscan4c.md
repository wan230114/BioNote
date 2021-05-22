文献：


Zscan4c activates endogenous retrovirus MERVL and cleavage embryo genes | Nucleic Acids Research | Oxford Academic

https://academic.oup.com/nar/article/47/16/8485/5531184

> Zscan4c activates endogenous retrovirus MERVL and cleavage embryo genes  
> Zscan4c激活内源性逆转录病毒MERVL并裂解胚胎基因？

# Content

背景：
- 内源性逆转录病毒（ERV）约占小鼠基因组的10％。它们通常在分化的体细胞中沉默，但在各个胚胎发育阶段均差异表达。少数小鼠胚胎干细胞（ESC），如2细胞裂解的胚胎，高表达ERV MERVL。但是，ERVs的作用及其激活机制在这些细胞中仍然知之甚少。

研究内容：
- 在这项研究中，我们调查了阶段特异性表达的ERV的调节和功能，特别关注全能标记MT2 / MERVL。我们显示，转录因子Zscan4c充当MT2 / MERVL和2-细胞/ 4-细胞胚胎基因的激活剂。Zscan4c的锌指结构域在此过程中起重要作用。

意外发现：
- 此外，Zscan4c与MT2相互作用，并通过促进MT2的增强子活性来调节MT2附近的2细胞/ 4细胞基因。此外，MT2激活伴随着增强的H3K4me1，H3K27ac和H3K14ac在MT2上的沉积。Zscan4c还通过SCAN域与GBAF染色质重塑复合物相互作用，以进一步激活MT2增强子活性。两者合计，我们描绘了一个以前无法识别的调控轴，Zscan4c通过表观遗传调控与MT2 / MERVL基因座及其附近的基因相互作用并激活它。

> **简介：**  
> 分析小鼠早期胚胎的单细胞测序数据，探究了不同 ERV 在小鼠卵裂期胚胎中的表达特点，发现 MERVL 在 2 细胞、4 细胞时期有一个高表达；

## INTRODUCTION

ERV —— 内源性逆转录病毒：  
- 覆盖约10％的小鼠和人类基因组。 

ERVs：
- 【ERV和ERVs是什么关系？】
- 功能：在哺乳动物中，ERVs的抑制机制和功能现在广泛在各种组织和细胞如脑（研究4）和 **胚胎干细胞（ESC）** 。
- 抑制什么？
- 机制：ERVs已知由KRAB-锌指蛋白，其介导异染色质形成涉及的H3K9me2/3和DNA甲基化（被抑制5，7-11）。甲基化过程涉及多种蛋白。但是，少数ERV仍在散发的ESC中表达。例如，ERV3家族成员MERVL在2细胞期胚胎和少数ESC中表达（17）。一旦被表达，ERVs参与宿主基因表达的调控（18，19），并可能提供新的转录因子结合位点，并起促进基因表达的增强子或启动子的作用（20）。【ERV的表达将为转录因子提供新的结合位点，并起促进基因表达的增强子或启动子的作用】

内源性逆转录病毒MERVL：
- 在小鼠 2 细胞胚胎中基因组开始激活转录（合子基因组激活），最早激活的转录本就包括内源性逆转录病毒 MERVL（MERVL 是在 2 细胞胚胎中高度表达的内源性逆转录病毒，属于 ERV3 家族中的一员）

---
研究发现：
- **Zscan4c 可以激活 MERVL 和卵裂期胚胎基因**

> Zscan4c: 

---
概括：

Zscan4c --激活--> MERVL和卵裂期胚胎基因

## Method

### 实验部分：略

### 生物信息部分

—— **(ChIP-seq) data analysis**

- pair-ended 25 million reads (150 bp)  
（25M 150bp reads 双末端测序）

- The adapter sequences of ChIP-seq data were removed with
Cutadapt (31) and reads with Phred score <5 were excluded
for analysis.  
（用<font color='red'>Cutadapt</font>除去ChIP-seq数据的adapter序列，并排除Phred得分<5的读数以进行分析。）

- Bowtie2 (32) was used to map reads to mm10 with the parameter ‘–very-sensitive’.  
（<font color='red'>Bowtie2</font>使用参数 “–very-sensitive” 将reads map到 mm10。）

- ChIP-seq signal enrichment was obtained by bamCompare from Deeptools (33) with parameter ‘–scaleFactorsMethodreadCount –minMappingQuality 1 –operation ratio –pseudocount 1’.
（ChIP-seq信号富集通过来自<font color='red'>Deeptools</font>的bamCompare获得，参数为...）

