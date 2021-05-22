# 1. 上游分析软件

|        流程        |     软件      |
| ------------------ | ------------- |
| 测序数据质量评估   | FastQC、      |
| 与参考基因组比对   | Bowtie2、BWA  |
| peak峰calling      | MACS          |
| motif分析          |               |
| peak峰相关基因注释 | R包ChIPseeker |
| 差异peak分析       |               |
| 相关基因功能分析   |               |


```bash
macs2 callpeak \
    -t ${REP1_TA_FILE}.tagAlign.gz \
    -c ${CONTROL_TA_PREFIX}.tagAlign.gz \
    -f BED \
    -n ${PEAK_OUTPUT_DIR}/${CHIP_TA_PREFIX} \
    -g ${GENOMESIZE} \
    -p 1e-2 \
    --nomodel \
    --shift 0 \
    --extsize ${FRAGLEN} \
    --keep-dup all -B --SPMR
```

# 2. 下游分析软件
## 2.1. deeptools
简介：  
- deepTools 是一套基于python开发的工具，适用于有效处理分析高通量测序数据，可用于ChIP-seq, RNA-seq 或 MNase-seq。
- BAM和bigWig文件处理、质量控制工具、热图和汇总图、杂项

命令汇总：  
- Tools for BAM and bigWig file processing
  - multiBamSummary
  - multiBigwigSummary
  - correctGCBias
  - bamCoverage
  - bamCompare
  - bigwigCompare
  - computeMatrix
  - alignmentSieve
- Tools for QC
  - plotCorrelation
  - plotPCA
  - plotFingerprint
  - bamPEFragmentSize
  - computeGCBias
  - plotCoverage
- Heatmaps and summary plots
  - plotHeatmap
  - plotProfile
  - plotEnrichment
- Miscellaneous
  - computeMatrixOperations
  - estimateReadFiltering

#### 2.1.1. Tools for BAM and bigWig file processing
(BAM和bigWig文件处理工具) 
- multiBamSummary
- multiBigwigSummary
- correctGCBias
- bamCoverage
- bamCompare
- bigwigCompare
- computeMatrix
- alignmentSieve

#### 2.1.2. Tools for QC
- plotCorrelation
- plotPCA
- plotFingerprint
- bamPEFragmentSize
- computeGCBias
- plotCoverage

#### 2.1.3. Heatmaps and summary plots
- plotHeatmap
- plotProfile
- plotEnrichment

#### 2.1.4. Miscellaneous
- computeMatrixOperations
- estimateReadFiltering

---
参考：

- [ ] [deepTools 3.3.0文档](https://deeptools.readthedocs.io/en/develop/content/list_of_tools.html)【官方文档】
- [ ] [deepTools 使用指南 - 简书](https://www.jianshu.com/p/2b386dd437d3)【很详细的一个命令汇总（使用表格），有大量挖掘和总结的地方】
- [ ] [高通量测序数据处理学习记录（四）：DeepTools学习笔记 - 简书
](https://www.jianshu.com/p/7cc5df9f7900)【关于所有命令的一个中文概述，可以从此处继续吸收信息，还未啃完】


## 2.2. bedtools
简介：
- 格式转换，bam转bed（bamToBed），bed转其他格式（bedToBam，bedToIgv）；
- 对基因组坐标的逻辑运算，包括：交集（intersectBed，windowBed），”邻集“（closestBed），补集（complementBed），并集（mergeBed），差集（subtractBed）;
- 计算覆盖度（coverage）（coverageBed，genomeCoverageBed）；

bam --> bw  
https://deeptools.readthedocs.io/en/develop/content/tools/bamCoverage.html  
https://deeptools.readthedocs.io/en/develop/content/feature/effectiveGenomeSize.html  

## 2.3. rose

ROSE是最经典的超级增强子预测软件，由Richard A. Young大牛团队开发，源代码的网址如下

http://younglab.wi.mit.edu/super_enhancer_code.html

在下面这篇文章中介绍了超级增强子的定义和发现过程，文章标题如下

Master Transcription Factors and Mediator Establish Super-Enhancers at Key Cell Identity Genes

发表在cell杂志上，链接如下

https://www.cell.com/fulltext/S0092-8674(13)00392-900392-9)


—— 来源： [使用ROSE鉴定超级增强子 - 简书](https://www.jianshu.com/p/f573f72bc4be)

