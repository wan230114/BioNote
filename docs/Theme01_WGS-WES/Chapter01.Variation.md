WGS基本流程介绍
---

以下流程均省略实验阶段的建库测序，从原始数据产出后分析开始说明。


---
# 1. 变异检测

变异检测流程图文字版：

- 原始测序数据
- 数据质控 （数据量，质量统计）
- 与参考基因组比对 （测序深度，覆盖度统计）
- 变异检测与注释
    - InDel 检测与注释
    - SNP 检测与注释
    - SV & CNV 检测与注释
- SNP 频率差异分析
- 定位候选区间
- 候选区间内基因GO、KEGG功能注释


信息分析的主要步骤如下：
- （1） 对下机得到的Raw data进行质控得到Clean data；
- （2） 将Clean data比对到参考基因组上；
- （3） 根据比对结果，进行SNP、InDel、SV和CNV的检测及注释。


---
## 1.1. 原始序列数据

高通量测序（如illumina HiSeqTM /MiSeqTM等测序平台）测序得到的原始图像数据文件经碱基识别（Base Calling）分析转化为原始测序序列（Sequenced Reads），我们称之为Raw Data或Raw Reads，结果以FASTQ（简称为fq）文件格式存储，其中包含测序序列（reads）的序列信息以及其对应的测序质量信息。

FASTQ格式文件中每个read由四行描述，如下：

```
@K00124:82:H2MH5BBXX:1:1101:31389:1158 2:N:0:0
TAGCCACATAGAAACCAACAGCCATATAACTGGTAGCTTTAAGCGGCTCACCTTTAGCATCAACAGGCCACAACCAACCAGAACGTGAAAAAGCGTCCTGCGTGTAGCGAACTGCGATGGGCATACAGATCGGAAGAGCGTCGTGTAGGG
+
AAFFFKKKKKKKKFKKKFFKKAAFKKKKKFKKKKFKKA,FKKKKKKKKKAKKFKKKKKKKAKKKKKKFFKKKKF<FFKKKKKKKKKKKKKFKKFKKF7FFFFFKFKKKFKKKKKKKKF<FFKKKKFKKKKKFKFKFKKFK<<F,A7,AFK
```

- 其中第一行以“@”开头，随后为illumina 测序标识符（Sequence Identifiers）和描述文字（选择性部分）；
- 第二行是碱基序列；
- 第三行以“+”开头，随后为illumina 测序标识符（选择性部分）；
- 第四行是对应序列的测序质量。

# 2. 测序数据质量评估
## 2.1. 测序质量分布检查

# 3. 项目简介
## 3.1. 拟南芥、苹果变异检测
2018/10-2018/10  

项目描述：  
- 本项目中，我使用公司流程对下机数据进行测序数据质量评估、过滤得到CleanData；  
- 再通过BWA软件（参数：mem -t 4 -k 32 -M）比对到参考基因组，并将比对结果经 SAMTOOLS 去除重复（参数：rmdup）；  
- 接下来，使用SAMTOOLS（mpileup -m 2 -F 0.002 -d 1000）进行个体SNP和Indel的检测分析，使用BreakDancer进行SV的检测分析；  
- 使用CNVnator(参数：-call 100)进行CNV分析；  
- 最后通过一些脚本统计各类变异数据，进行数据可视化。  
- 总结而言：质控、比对、callSNP、变异检测。  
