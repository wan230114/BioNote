# hisat2 的一些细节问题

## 索引建立过程

问题：
> hisat2建立索引时，是否可以不需要gtf文件，而只用fasta文件？  
> - 如果可以，那么后续进行比对是否可以手动添加gtf？（否则，怎么能精确做到RNA-seq精确map到fasta的基因上呢？）
> - 如果不行，那么后续进行比对是否就不用用到gtf文件了？【待补充】


范本：（不用gtf建立索引）
```bash
name=ChlSab1.1
genome=/home/gzsc/downloads/ChlSab1.1/fa/Chlorocebus_sabaeus.ChlSab1.1.dna_sm.toplevel.fa
index=/home/gzsc/downloads/ChlSab1.1/index
gene=/home/gzsc/downloads/ChlSab1.1/gtf/Chlorocebus_sabaeus.ChlSab1.1.100.gtf
#hisat2_extract_exons.py $gene >$index/hisat2/$name'.exon'
#hisat2_extract_splice_sites.py $gene >$index/hisat2/$name'.ss'
#hisat2-build -p 30 --ss $index/hisat2/$name'.ss' --exon $index/hisat2/$name'.exon' $genome $index/hisat2/$name 1>$index/hisat2/index.log 2>&1
hisat2-build -p 30 $genome $index/hisat2/$name 1>$index/hisat2/index.log 2>&1
```

---

### 研究思路

1. 先看已存在的hisat2常规索引方法？
2. google得到hisat2的原理？【比较费时，暂时跳过】
3. 自行测试
   - 截取一条染色体分别做
   - 直接用人的参考基因组进行做


答案：
1. 查看以前做过的流程：

类1：

索引部分：（使用的人的基因组现成的索引）
【疑惑: 这个索引是如何完成的，怎么用到的gtf？已解决】

```bash
hisat2 -p 20 --dta -x /home/gzsc/genomic/Homo_sapiens/UCSC/hg38/current/current_index/hisat2/Homo_sapiens -1 cleandata/B2_L4_304304.R1_val_1.fq.gz -2 cleandata/B2_L4_304304.R2_val_2.fq.gz -S 01.hisat/B2_L4_304304.sam &> 01.hisat/B2_L4_304304.log
```


类2：
```bash
export PATH=/PUBLIC/software/RNA/HISAT2/hisat2-2.0.4/:$PATH
export PATH=/PUBLIC/source/RNA/tools/:$PATH
hisat2-build -p 20 genome.fa genome
```

```bash
hisat2 -p 8 -t -x $refindex -1 clean_data/F3_1_1_1.clean.fq -2 clean_data/F3_1_1_2.clean.fq --no-unal   --un-conc hisat_dir  --dta-cufflinks |samtools view -bS  - > hisat/F3_1_1.bam
```

### 搜索的意外发现

---
**两者都要做**

> 通过咨询一些朋友，他们说：
> - 这个转录本的index不知道干啥
> - 基因组比对先对基因组index

原文：  
—— [hisat2构建基因组index - 简书](https://www.jianshu.com/p/1093ef5da0fa)

选用：gencode的GRCm38.fasta和gtf  
第一步：转录本的index：  
```bash
extract_exons.py gencode.vM19.annotation.gtf > genome.exon
extract_splice_sites.py gencode.vM19.annotation.gtf > genome.ss
hisat2-build -p 20 GRCm38.chr.fa --ss genome.ss --exon genome.exon genome_tran
```
第二步：基因组的index：  
```bash
hisat2-build -p 20 genome.fa genome
```
---

**两者差异不大，但如果下游做的较细致，建议做一下转录本**

hisat2的index选择？ - 知乎
https://www.zhihu.com/question/275475868/answer/383738281

---


### 结果说明

最好还是在建立索引使用gtf，后面的下游分析还是挺重要。不要硬着头皮去做无gtf的直接mapping。