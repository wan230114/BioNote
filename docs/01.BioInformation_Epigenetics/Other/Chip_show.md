
定量分析方案：

|Pipeline|结果文件|说明|
|-|-|-|
|`--(sequence)-->`|RawData | 原始下机数据|
|`--(qc)-->`| CleanData| 进行质控，去接头 |
|`--(map)-->` |比对结果.bam| 将CleanData比对到参考基因组 |
|`--(call peak)-->` |检峰结果.peak| 通过比对结果进行检峰 |
|`--(merge)-->`|merge.bed|合并样本的Peak，合并所有峰的区域位置|
|`--(cover)-->`|merge.gtf|将bed文件转化为gtf，用于后续定量分析|
|`--(counts)-->`|counts_peak.xls|将各个 比对结果.bam 进行定量 到 merge.gtf|
|`--(diff)-->`|diff_peak.xls|通过表达定量寻找差异peak数|
|`--(find3kgene)-->`|gene.list|通过差异peak查找其上下游3k临近基因|
|`--(anno)-->`|anno_gene.list|对查找到的基因进行注释分析|
